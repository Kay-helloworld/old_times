class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree (Order m = 2*t or similar, but here we use Order m directly)
        # Wait, standard B-Tree definition varies.
        # Question says "Order 3".
        # Order m means max children = m.
        # Max keys = m - 1.
        # Min children = ceil(m/2).
        # Min keys = ceil(m/2) - 1.
        self.m = t # Order

    def insert(self, k):
        root = self.root
        # If root is full, tree grows in height
        if len(root.keys) == self.m - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == self.m - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        # Split x.children[i]
        t = self.m # Order
        # Split point: usually median.
        # For Order 3: Max keys=2. Insert 3rd key -> Split.
        # Keys: [k1, k2, k3] -> k2 goes up. Left:[k1], Right:[k3].
        # Mid index = (m-1)//2 ?
        # Order 3: max keys 2. When we have 3 keys (temporary), we split.
        # Actually my implementation above checks `len == m-1` (full) BEFORE descending.
        # So we split a full node (2 keys) into 1 key + 1 key? No, that's not right.
        # Standard algorithm: Split when full (2*t-1 keys).
        # But "Order m" definition is simpler: Max m children, m-1 keys.
        
        # Let's adjust for Order m specifically.
        # Max keys = m-1.
        # Split happens when we try to insert into a full node (or proactively).
        # Mid index for Order 3 (keys 0,1,2) -> index 1 is median.
        
        y = x.children[i]
        z = BTreeNode(y.leaf)
        
        # Calculate split index
        # If y has m-1 keys, and we are about to add one, effectively we are splitting a node that WOULD have m keys.
        # But proactive splitting splits a node that HAS m-1 keys?
        # Wait, for Order 3, max keys = 2.
        # If we split a node with 2 keys [10, 80], we can't really split it yet without the new key?
        # Actually, standard B-Tree insertion often allows temporary overflow or splits proactively.
        # Let's use the proactive split: "If we encounter a full node on the way down, split it."
        # Full node has m-1 keys.
        # Order 3: Full = 2 keys. [10, 80].
        # Split [10, 80]: 10 goes left, 80 goes right? No, one must go up.
        # But we only have 2 keys. We can't split 2 keys into 1 up, 1 left, 1 right (needs 3 keys).
        # Ah, Order 3 B-Tree (2-3 Tree) behavior:
        # Insert into leaf. If leaf has 3 items, split.
        # Proactive splitting (top-down) usually requires t >= 2 (Order 4+).
        # For Order 3, we usually do bottom-up splitting.
        
        # Let's rewrite to use Bottom-Up insertion for accuracy with Order 3.
        pass

    def print_tree(self, x, level=0):
        print(f"Level {level}: {x.keys}")
        for child in x.children:
            self.print_tree(child, level + 1)

# Re-implementing with Bottom-Up approach for Order 3 (2-3 Tree style)
class BTreeOrder3:
    def __init__(self):
        self.root = BTreeNode(True)
        self.m = 3 # Order 3

    def insert(self, k):
        print(f"\n--- Inserting {k} ---")
        root = self.root
        # Try to insert into root
        new_child, median = self._insert_node(root, k)
        if new_child:
            # Root split
            new_root = BTreeNode(False)
            new_root.keys = [median]
            new_root.children = [root, new_child]
            self.root = new_root
            print(f"Root split! New root: {self.root.keys}")

    def _insert_node(self, node, k):
        # Returns (new_node, median_key) if split occurred, else (None, None)
        
        if node.leaf:
            # Insert into leaf
            node.keys.append(k)
            node.keys.sort()
            if len(node.keys) >= self.m: # Max keys is m-1. If len == m, overflow.
                return self._split(node)
            return None, None
        else:
            # Find child
            i = 0
            while i < len(node.keys) and k > node.keys[i]:
                i += 1
            
            new_child, median = self._insert_node(node.children[i], k)
            if new_child:
                # Child split, merge median into current node
                node.keys.insert(i, median)
                node.children.insert(i + 1, new_child)
                if len(node.keys) >= self.m:
                    return self._split(node)
            return None, None

    def _split(self, node):
        # Split node with m keys (Overflow)
        # Order 3: Node has 3 keys [k0, k1, k2].
        # Median is k1.
        # Left: [k0], Right: [k2].
        mid_idx = len(node.keys) // 2
        median = node.keys[mid_idx]
        
        right_node = BTreeNode(node.leaf)
        right_node.keys = node.keys[mid_idx+1:]
        node.keys = node.keys[:mid_idx]
        
        if not node.leaf:
            right_node.children = node.children[mid_idx+1:]
            node.children = node.children[:mid_idx+1]
            
        return right_node, median

    def display(self):
        self._display(self.root, 0)
        
    def _display(self, node, level):
        print(f"Level {level}: {node.keys}")
        if not node.leaf:
            for child in node.children:
                self._display(child, level + 1)

def solve_114_btree():
    print("=== 114年 B-Tree (Order 3) Insertion Simulation ===")
    keys = [10, 80, 2, 9, 45, 62]
    btree = BTreeOrder3()
    
    for k in keys:
        btree.insert(k)
        btree.display()
        
    print("\n=== Final Result ===")
    print(f"Root Keys: {btree.root.keys}")

if __name__ == "__main__":
    solve_114_btree()
