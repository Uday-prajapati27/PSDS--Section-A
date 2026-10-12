# LABSHEET 9
# Minimum operations to make all elements equal to zero

def solve(N, A):
    # Check if all elements are equal
    for i in range(1, N):
        if A[i] != A[0]:
            return -1

    # All elements are equal
    return abs(A[0])


# Number of test cases
T = int(input("Enter number of test cases: "))

for test_case in range(1, T + 1):

    print("\nTest Case", test_case)

    # Array size
    N = int(input("Enter array size: "))

    # Array elements
    A = list(map(int, input("Enter array elements: ").split()))

    # Calculate answer
    result = solve(N, A)

    # Display result
    print("Minimum operations:", result)
