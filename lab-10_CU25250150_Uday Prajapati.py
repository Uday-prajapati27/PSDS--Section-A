# LABSHEET 10
# Count pairs having equal sum of digits


# Function to calculate sum of digits
def digit_sum(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total


# Function to count special pairs
def solve(N, nums):
    count = {}
    answer = 0

    for num in nums:
        s = digit_sum(num)

        # If this digit sum appeared before,
        # current number forms pairs with all of them
        if s in count:
            answer += count[s]
            count[s] += 1
        else:
            count[s] = 1

    return answer


# Input
N = int(input("Enter array size: "))

nums = list(map(int, input("Enter array elements: ").split()))

# Calculate answer
result = solve(N, nums)

# Output
print("Number of special pairs:", result)
