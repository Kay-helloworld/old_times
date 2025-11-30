def solve_q5():
    print("=== Question 5: Digital Analysis Hashing ===")
    
    ids = [
        "0392018",
        "0392124",
        "0392238",
        "0252714",
        "0392468"
    ]
    
    print("IDs:", ids)
    num_students = len(ids)
    num_digits = len(ids[0])
    
    # Calculate Skewness for each position N1..N7
    # ski = sum(j=0..9) |aij - 1/10|
    # aij = count(digit j in col i) / num_students
    
    skewness = []
    
    print("\nCalculating Skewness (sk) for each column:")
    for i in range(num_digits):
        counts = {str(d): 0 for d in range(10)}
        col_digits = [s[i] for s in ids]
        
        for d in col_digits:
            counts[d] += 1
            
        sk = 0
        for d in range(10):
            aij = counts[str(d)] / num_students
            sk += abs(aij - 0.1)
            
        skewness.append(sk)
        print(f"  N{i+1} ({col_digits}): sk = {sk:.2f}")
        
    # Select columns with lowest skewness
    # We need 2 digits for address space 99.
    
    indexed_skewness = list(enumerate(skewness))
    # Sort by skewness ascending
    indexed_skewness.sort(key=lambda x: x[1])
    
    best_cols = [indexed_skewness[0][0], indexed_skewness[1][0]]
    best_cols.sort() # Keep original order, e.g., N5, N6
    
    print(f"\nSelected Columns (Lowest Skewness): N{best_cols[0]+1}, N{best_cols[1]+1}")
    
    # Calculate Addresses
    print("\nCalculated Addresses:")
    for s in ids:
        addr = s[best_cols[0]] + s[best_cols[1]]
        print(f"  ID {s} -> Address: {addr}")

if __name__ == "__main__":
    solve_q5()
