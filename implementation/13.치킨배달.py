#13. 치킨 배달

import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")

# 데이터 입력받기
n, m = map(int, input().split())
cityMap = []
for _ in range(n):
  cityMap.append(list(map(int, input().split())))

# 집, 치킨집 좌표
house = []
chicken = []
for i in range(n):
  for j in range(n):
    if cityMap[i][j] == 1:
      house.append((i, j))
    elif cityMap[i][j] == 2:
      chicken.append((i, j))

# 치킨집 조합
chickencombi = []
for i in combinations(chicken, m):
  chickencombi.append(i)

# 치킨 거리의 합 계산
def get_chickenDist_sum(chickencombi):
  chickenDistSum = 0
  # 모든 집집마다
  for hx, hy in house:
    # 집과 가장 가까운 치킨집 사이 거리(치킨거리) 구하기
    chickinDist = 1e9
    for cx, cy in chickencombi:
      chickinDist = min(chickinDist, abs(hx - cx) + abs(hy - cy))  #Q. 
    chickenDistSum += chickinDist
  return chickenDistSum

# 치킨 거리의 합 중 최소값 찾기
result = 1e9
for combi in chickencombi:
  result = min(result, get_chickenDist_sum(combi))

print(result)
