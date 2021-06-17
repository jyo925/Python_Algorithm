import sys

# 중복순열 구하기
# 상태트리와 스택 그려보기
sys.stdin = open("input.txt", 'r')


def DFS(L):
    global cnt
    if L == m:  # 중복 순열이 완성되었을 때
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
