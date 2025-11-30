def binomial_coefficient(n, r, depth=0, counter=None):
    """
    Calculates C(n, r) recursively based on the formula:
    C(n, r) = 
      0 if r > n
      1 if n == r
      1 if r == 0
      C(n-1, r) + C(n-1, r-1) otherwise
    """
    if counter is None:
        counter = {'count': 0}
    
    counter['count'] += 1
    indent = "  " * depth
    print(f"{indent}Call: C({n}, {r})")
    
    if r > n:
        return 0
    if n == r:
        return 1
    if r == 0:
        return 1
    
    # Recursive step
    res = binomial_coefficient(n-1, r, depth+1, counter) + \
          binomial_coefficient(n-1, r-1, depth+1, counter)
    
    return res

def solve_q1():
    print("=== Question 1: Binomial Coefficient ===")
    n = 5
    r = 3
    print(f"Calculating C({n}, {r})...")
    
    counter = {'count': 0}
    result = binomial_coefficient(n, r, counter=counter)
    
    print(f"\nResults for n={n}, r={r}:")
    print(f"Return Value: {result}")
    print(f"Total Recursive Calls: {counter['count']}")

if __name__ == "__main__":
    solve_q1()
