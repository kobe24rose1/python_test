'''
1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다. 
이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 
기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.

첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력된다.

10 3
13 15 34 23 45 65 33 11 26 42
'''

import sys
sys.stdin = open('input.txt', 'rt')
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
