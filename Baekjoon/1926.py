import sys

# 이번 문제는 재귀 깊이가 10만도 부족한 문제였다. 10만으로 설정했을 때, 런타임 에러가 나서 늘려주었다.
sys.setrecursionlimit(1000000)


# 그림의 크기와 개수를 탐색하는 dfs 함수.
def dfs(painting, i, j, n, m):
    # 그림의 크기를 계산할 글로벌 변수.
    global painting_size
    if i < 0 or i >= n or j < 0 or j >= m or painting[i][j] != '1':
        return painting_size

    painting[i][j] = '0'
    # 크기를 계산해주어야 하므로 더해주고 함수의 마지막에 반환한다.
    painting_size += 1

    dfs(painting, i + 1, j, n, m)
    dfs(painting, i - 1, j, n, m)
    dfs(painting, i, j + 1, n, m)
    dfs(painting, i, j - 1, n, m)

    return painting_size


n, m = map(int, input().split())
painting = [list(input().split()) for _ in range(n)]
cnt = 0
size_lst = []

for i in range(n):
    for j in range(m):
        painting_size = 0
        if painting[i][j] == '1':
            size_lst.append(dfs(painting, i, j, n, m))
            cnt += 1
print(cnt)
# 그림이 없을 때 최댓값을 처리해주지 않아 런타임 에러가 났었다.
try:
    print(max(size_lst))
except:
    print(0)
