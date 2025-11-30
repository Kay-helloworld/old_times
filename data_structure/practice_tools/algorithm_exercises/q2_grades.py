def solve_q2():
    print("=== Question 2: Grade Analysis ===")
    
    # Probabilities
    probs = {
        'A': 0.05, # >= 90
        'B': 0.30, # 80-89
        'C': 0.50, # 70-79
        'D': 0.10, # 60-69
        'F': 0.05  # < 60
    }
    
    print("Probabilities:", probs)
    
    # 1. Original IF-ELSE Analysis
    # if S<60 (F) -> 1 cmp
    # else if S<70 (D) -> 2 cmp
    # else if S<80 (C) -> 3 cmp
    # else if S<90 (B) -> 4 cmp
    # else (A) -> 4 cmp
    
    exp_cmp_original = (
        probs['F'] * 1 +
        probs['D'] * 2 +
        probs['C'] * 3 +
        probs['B'] * 4 +
        probs['A'] * 4
    )
    
    print(f"\n1. Original IF-ELSE Expected Comparisons:")
    print(f"   E = 0.05*1 + 0.10*2 + 0.50*3 + 0.30*4 + 0.05*4")
    print(f"   E = {exp_cmp_original:.2f}")
    
    # 2. Optimized Binary Search Tree (Huffman-like)
    # Goal: Place high probability items closer to root.
    # Split to balance weight.
    # Total = 1.0.
    # Split at 80? (Left: <80 [F,D,C] = 0.65, Right: >=80 [B,A] = 0.35)
    
    # Tree Structure:
    # Root: S < 80
    #   Left (S < 80): Check S < 70
    #       Left (S < 70): Check S < 60
    #           Left: F (3 cmps: <80, <70, <60)
    #           Right: D (3 cmps)
    #       Right (S >= 70): C (2 cmps: <80, <70)
    #   Right (S >= 80): Check S < 90
    #       Left (S < 90): B (2 cmps: <80, <90)
    #       Right (S >= 90): A (2 cmps)
    
    exp_cmp_opt = (
        probs['F'] * 3 +
        probs['D'] * 3 +
        probs['C'] * 2 +
        probs['B'] * 2 +
        probs['A'] * 2
    )
    
    print(f"\n2. Optimized Tree Expected Comparisons:")
    print(f"   Structure: Root(80) -> Left(70) -> Left(60)")
    print(f"                          -> Right(C)")
    print(f"                       -> Right(90)")
    print(f"   E = F(0.05)*3 + D(0.1)*3 + C(0.5)*2 + B(0.3)*2 + A(0.05)*2")
    print(f"   E = {exp_cmp_opt:.2f}")
    
    # 3. Data Structure for Simplification
    print(f"\n3. Data Structure Suggestion:")
    print(f"   Use a Lookup Table (Array).")
    print(f"   Since scores are 0-100, we can map Score/10 to a Grade.")
    print(f"   Array size 11 (0-10). Index = Score // 10.")
    print(f"   Indices 0-5 -> 'F', 6 -> 'D', 7 -> 'C', 8 -> 'B', 9,10 -> 'A'.")
    print(f"   Time Complexity: O(1).")

if __name__ == "__main__":
    solve_q2()
