def solve_q4():
    print("=== Question 4: Konigsberg Bridge Problem ===")
    
    # Graph Representation (Adjacency List)
    # Nodes: A, B, C, D
    # Edges based on standard problem:
    # A-B: 2 bridges
    # A-C: 2 bridges
    # A-D: 1 bridge
    # B-D: 1 bridge
    # C-D: 1 bridge
    
    graph = {
        'A': ['B', 'B', 'C', 'C', 'D'],
        'B': ['A', 'A', 'D'],
        'C': ['A', 'A', 'D'],
        'D': ['A', 'B', 'C']
    }
    
    print("Graph Degrees:")
    odd_degree_nodes = 0
    for node, neighbors in graph.items():
        degree = len(neighbors)
        print(f"  Node {node}: Degree {degree}")
        if degree % 2 != 0:
            odd_degree_nodes += 1
            
    print(f"\nNumber of Odd Degree Nodes: {odd_degree_nodes}")
    
    # 1. Is it possible to walk all bridges once and return? (Euler Cycle)
    print("\n1. Possible to traverse all bridges and return (Euler Cycle)?")
    if odd_degree_nodes == 0:
        print("   YES. (All degrees are even)")
    else:
        print("   NO. (Exists nodes with odd degrees)")
        
    # 3. Euler's Rule
    print("\n3. Euler's Rule:")
    print("   - Eulerian Cycle (Start and End same): Graph is connected and EVERY node has an EVEN degree.")
    print("   - Eulerian Path (Start and End different): Graph is connected and EXACTLY 2 nodes have ODD degree.")
    
    # 4. Example of Eulerian Cycle
    print("\n4. Example of Eulerian Cycle:")
    print("   Graph: Triangle (A-B, B-C, C-A)")
    print("   Degrees: A(2), B(2), C(2). All even.")
    print("   Path: A -> B -> C -> A")

if __name__ == "__main__":
    solve_q4()
