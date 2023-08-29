# 33.퇴사

# 입력
n = int(input())
time = []
pay = []
for _ in range(n):
  t, p = map(int, input().split())
  time.append(t)
  pay.append(p)

# 최대 수익을 저장하는 dp 테이블
dp = [0 for _ in range(n + 1)]

# 알고리즘
# 순방향으로 진행 시 경우의 수가 더 많음 -> 역방향으로 진행하면서 dp 테이블 값 구하기
# 7일차에 상담이 불가능할 경우 -> 다음날 기준 최대 수익값인 dp[7]를 가져와야 됨 -> dp[7] 초기화 필요
for i in range(n - 1, -1, -1):
  if i + time[i] > n:  # 상담에 필요한 일수가 퇴사일을 넘어가면
    dp[i] = dp[i + 1]  # 상담 X -> 다음날 기준 최대 수익 가져옴
  else:
    dp[i] = max(
      dp[i + 1],  # 상담 X 
      dp[time[i] + i] + pay[i]  # 상담 O
    )

print(dp[0])
