'''
대표값 구하기
N명의 학생의 수학점수가 주어진다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성.
평균과 가장 가까운 점수가 여러 개일 경우 점수가 높은 학생의 번호를 답으로 하고, 
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 한다.

10
45 73 66 87 92 67 75 79 75 80

'''

import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a) / n)
min = 2147000000
for i, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        res = i + 1
        score = x
    elif tmp == min:
        if x > score:
            score = x
            res = i + 1
print(ave, res)
    



