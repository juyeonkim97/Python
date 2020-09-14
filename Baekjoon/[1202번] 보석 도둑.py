#그리디 알고리즘
#백준 1202번

import queue
from sys import stdin, stdout
N, K = stdin.readline().split()
N = int(N)
K = int(K)
A = []
for i in range(N):
	x, y = stdin.readline().split()
	x = int(x)
	y = int(y)
	A.append([x, y])
for i in range(K):
	A.append([int(stdin.readline()), 2000000])
A.sort()
ans = 0
pq = queue.PriorityQueue(N)
for x in A:
	if x[1] != 2000000:
		pq.put(-x[1])
	else:
		if (not(pq.empty())):
			t = -pq.get()
			ans += t
print (ans)
