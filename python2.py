import heapq

n = int(input())
a = list(map(int, input().split()))
q = int(input())
ops = []
T_list = []

# 初始化堆
heap = [(-a[i], i) for i in range(n)]
heapq.heapify(heap)
t = sum([heap[i][0] * (i+1) for i in range(n)])

for _ in range(q):
    i, j = map(int, input().split())
    i -= 1  # 将下标转为0-based
    # 更新堆
    heapq.heappush(heap, (-j, i))
    while heap[0][1] < 0:
        heapq.heappop(heap)
    # 计算新的 T 值
    t = sum((i+1) * -heap[i] for i in range(n))
    T_list.append(t)

# 输出每次操作后的 T 值
for t in T_list:
    print(t)
