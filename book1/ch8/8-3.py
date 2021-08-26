# 보텀업(반복문)
# 재귀는 함수호출을 하므로 오버헤드가 발생할 수 있다.
# 반복문을 이용하면 오버헤드를 줄여 조금 더 성능이 좋음
# 다이나믹프로그래밍의 전형적인 형태


d = [0] * 100

d[1] = 1
d[2] = 1

n = 99
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
