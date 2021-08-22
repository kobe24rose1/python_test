# 최소값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arr_min = float('inf')  # 가장 큰 값으로 초기화
for i in range(len(arr)):
    if arr[i] < arr_min:
        arr_min = arr[i]
print(arr_min)