# 1. sort() 사용

n = int(input())
cards = []
for i in range(n):
  cards.append(int(input()))

cards.sort()

result = 0
for i in range(n - 1):
  sum = cards[i] + cards[i + 1]
  result += sum
  cards[i + 1] = sum
  
  
  
# 2. 우선순위 큐-힙 자료구조 사용(파이썬 heapq 모듈: 최소힙으로 구현됨)

import heapq

n = int(input())
cards = []
for _ in range(n):
  heapq.heappush(cards, int(input()))

result = 0
while len(cards) != 1: # heap에 최종 결과값이 남을 때까지 
  # 가장 작은 크기의 카드 두 개 꺼내기
  first = heapq.heappop(cards)
  second = heapq.heappop(cards)
  sum = first + second
  result += sum
  # 카드 두 개의 합을 다시 넣기 
  heapq.heappush(cards, sum)

