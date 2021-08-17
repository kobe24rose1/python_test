# 두 개의 자연수 n과 k가 주어졌을 때, n의 약수들 중 k번째로 작은 수를 출력하는 프로그램을  작성하시오

import sys
sys.stdin = open('AA/input.txt', 'rt')
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
