#problem 1
n, k = map(int, input("Enter the value of n & k : ").split())
arr = list(map(int, input("Enter the array elements : ").split()))

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i]
    window_sum -= arr[i - k]

    max_sum = max(max_sum, window_sum)

print("Sum of maximum subarray of size K : ", max_sum)


#problem 2
s = input("Enter your String : ").strip()
left = 0
max_length = 0
seen = set()

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    max_length = max(max_length, right - left + 1)

print("Longest substrings without repeating characters: ", max_length)


#problem 3 
import heapq

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))

INF = float('inf')

dist = [[INF] * (k + 1) for _ in range(n + 1)]

dist[1][0] = 0

pq = [(0, 1, 0)]

while pq:
    cost, node, edges = heapq.heappop(pq)

    if cost != dist[node][edges]:
        continue

    if node == n:
        print(cost)
        break

    if edges == k:
        continue

    for neighbor, weight in graph[node]:
        new_cost = cost + weight
        new_edges = edges + 1

        if new_cost < dist[neighbor][new_edges]:
            dist[neighbor][new_edges] = new_cost
            heapq.heappush(pq, (new_cost, neighbor, new_edges))

else:
    print(-1)
