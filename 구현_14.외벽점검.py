#14. 외벽점검

# 완전탐색: 취약 지점 case (탐색 시작 지점별로 case가 달라짐) x 친구들이 이동할 수 있는 거리 case
#          => 투입되는 친구의 수가 가장 적은 case 찾기
# 반시계방향으로 탐색하는 case를 따로 고려하지 않음 (1->5나 5->1나 같은 case)

import itertools


def solution(n, weak, dist):

  weakSize = len(weak)  # 취약 지점의 개수
  # 취약 지점의 위치를 일자 형태로 변경(취약 지점간 거리를 쉽게 계산하기 위해)
  for i in range(weakSize):
    weak.append(weak[i] + n)

  # 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없을 때 최소값
  answer = len(dist) + 1

  # 탐색 시작 지점별 취약 지점 case
  for startPos in range(weakSize):
    # 친구들이 이동할 수 있는 거리 case
    for moveDist in itertools.permutations(dist, len(dist)):
      friendCnt = 1  # 투입하는 친구 수
      pos = startPos
      # 탐색 시작 지점과 다음 탐색 지점 사이 거리 - 친구들이 이동 가능한 거리 비교: 탐색 가능여부 따지기
      for i in range(1, weakSize):  # 다음 탐색 지점(weak[1])부터
        nextPos = startPos + i
        distDiff = weak[nextPos] - weak[pos]
        # 먼저 탐색하는 친구가 탐색할 수 없는 거리면
        if distDiff > moveDist[friendCnt - 1]:
          # 다음 친구가 그 다음 취약 지점부터 탐색
          friendCnt += 1
          pos = nextPos
          # 더이상 투입될 친구가 없으면
          if friendCnt > len(dist):
            break
      answer = min(answer, friendCnt)

  if (answer > len(dist)):
    return -1

  return answer
