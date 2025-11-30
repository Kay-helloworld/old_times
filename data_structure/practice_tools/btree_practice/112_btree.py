class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTreeOrder3:
    def __init__(self):
        self.root = BTreeNode(True)
        self.m = 3 # Order 3 (2-3 Tree)

    def insert(self, k):
        print(f"\n--- Inserting {k} ---")
        root = self.root
        if len(root.keys) == self.m - 1: # Pre-emptive split not strictly 2-3 tree standard but easier
             # Actually, let's stick to the bottom-up split logic from before which worked well
             pass
        
        new_child, median = self._insert_node(self.root, k)
        if new_child:
            new_root = BTreeNode(False)
            new_root.keys = [median]
            new_root.children = [self.root, new_child]
            self.root = new_root
            print(f"Root split! New root: {self.root.keys}")

    def _insert_node(self, node, k):
        if node.leaf:
            node.keys.append(k)
            node.keys.sort()
            if len(node.keys) >= self.m:
                return self._split(node)
            return None, None
        else:
            i = 0
            while i < len(node.keys) and k > node.keys[i]:
                i += 1
            new_child, median = self._insert_node(node.children[i], k)
            if new_child:
                node.keys.insert(i, median)
                node.children.insert(i + 1, new_child)
                if len(node.keys) >= self.m:
                    return self._split(node)
            return None, None

    def _split(self, node):
        mid_idx = len(node.keys) // 2
        median = node.keys[mid_idx]
        right_node = BTreeNode(node.leaf)
        right_node.keys = node.keys[mid_idx+1:]
        node.keys = node.keys[:mid_idx]
        if not node.leaf:
            right_node.children = node.children[mid_idx+1:]
            node.children = node.children[:mid_idx+1]
        return right_node, median

    def delete(self, k):
        print(f"\n--- Deleting {k} ---")
        self._delete(self.root, k)
        # If root is empty and has a child, shrink tree
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]
            print("Tree height decreased!")

    def _delete(self, node, k):
        t = 2 # Min degree for B-Tree logic, but for Order 3 (2-3 Tree), min keys = 1.
        # 2-3 Tree logic:
        # 1. Find k.
        # 2. If in internal node, swap with predecessor/successor in leaf.
        # 3. Delete from leaf.
        # 4. Fix underflow (0 keys).
        
        idx = self._find_key(node, k)
        
        if idx < len(node.keys) and node.keys[idx] == k:
            if node.leaf:
                node.keys.pop(idx)
            else:
                # Internal node: replace with predecessor
                pred = self._get_pred(node, idx)
                node.keys[idx] = pred
                self._delete(node.children[idx], pred)
        else:
            if node.leaf:
                print(f"Key {k} not found")
                return
            
            # Determine child to descend
            # idx is already correct child index
            child = node.children[idx]
            
            # Ensure child has enough keys (proactive merge/borrow? or reactive?)
            # Reactive is standard for 2-3 trees.
            self._delete(child, k)
            
            if len(child.keys) == 0: # Underflow
                self._fix_underflow(node, idx)

    def _find_key(self, node, k):
        idx = 0
        while idx < len(node.keys) and node.keys[idx] < k:
            idx += 1
        return idx

    def _get_pred(self, node, idx):
        curr = node.children[idx]
        while not curr.leaf:
            curr = curr.children[-1]
        return curr.keys[-1]

    def _fix_underflow(self, parent, idx):
        # Child at parent.children[idx] has 0 keys.
        # Try to borrow from siblings (idx-1 or idx+1)
        
        # Try Left Sibling
        if idx > 0:
            left_sibling = parent.children[idx-1]
            if len(left_sibling.keys) > 1: # Can borrow
                print(f"Borrowing from left sibling")
                child = parent.children[idx]
                child.keys.insert(0, parent.keys[idx-1])
                parent.keys[idx-1] = left_sibling.keys.pop()
                if not left_sibling.leaf:
                    child.children.insert(0, left_sibling.children.pop())
                return

        # Try Right Sibling
        if idx < len(parent.children) - 1:
            right_sibling = parent.children[idx+1]
            if len(right_sibling.keys) > 1: # Can borrow
                print(f"Borrowing from right sibling")
                child = parent.children[idx]
                child.keys.append(parent.keys[idx])
                parent.keys[idx] = right_sibling.keys.pop(0)
                if not right_sibling.leaf:
                    child.children.append(right_sibling.children.pop(0))
                return
                
        # Merge
        # If can't borrow, merge with sibling.
        # Prefer merging with left sibling
        if idx > 0:
            print(f"Merging with left sibling")
            left_sibling = parent.children[idx-1]
            child = parent.children[idx]
            left_sibling.keys.append(parent.keys.pop(idx-1)) # Pull down separator
            left_sibling.keys.extend(child.keys)
            if not child.leaf:
                left_sibling.children.extend(child.children)
            parent.children.pop(idx) # Remove empty child
        else:
            print(f"Merging with right sibling")
            right_sibling = parent.children[idx+1]
            child = parent.children[idx]
            child.keys.append(parent.keys.pop(idx)) # Pull down separator
            child.keys.extend(right_sibling.keys)
            if not child.leaf:
                child.children.extend(right_sibling.children)
            parent.children.pop(idx+1)

    def display(self):
        self._display(self.root, 0)
        
    def _display(self, node, level):
        print(f"Level {level}: {node.keys}")
        if not node.leaf:
            for child in node.children:
                self._display(child, level + 1)

def solve_112_btree():
    print("=== 112年 B-Tree (2-3 Tree) Simulation ===")
    btree = BTreeOrder3()
    
    # Insert Phase
    inserts = [60, 70, 50, 10, 20, 80, 95, 90]
    for k in inserts:
        btree.insert(k)
        btree.display()
        
    print("\n=== Deletion Phase ===")
    
    # Delete 50
    btree.delete(50)
    btree.display()
    
    # Delete 20
    btree.delete(20)
    btree.display()
    
    # Delete 80
    btree.delete(80)
    btree.display()

if __name__ == "__main__":
    solve_112_btree()
