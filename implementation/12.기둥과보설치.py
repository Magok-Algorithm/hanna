#12. 기둥과 보 설치


# 설치 or 삭제가 가능한 경우를 확인하는 함수
def makingRule(answer):
  for x, y, a in answer:
    # 기둥
    if a == 0:
      # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
      if (y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer
          or [x, y - 1, 0] in answer):
        continue
      else:
        return False
    # 보
    elif a == 1:
      # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결
      if ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer
          or [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
        continue
      else:
        return False
  return True


def solution(n, build_frame):
  answer = []
  for x, y, a, b in build_frame:
    # 설치하는 경우
    if b == 1:
      answer.append([x, y, a])
      if makingRule(answer) == False:
        answer.remove([x, y, a])
    # 삭제하는 경우
    elif b == 0:
      answer.remove([x, y, a])
      if makingRule(answer) == False:
        answer.append([x, y, a])

  return sorted(answer)
