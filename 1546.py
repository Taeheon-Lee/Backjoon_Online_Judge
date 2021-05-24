"Question 1546"

input()
score = list(map(int, input().split()))
max_score = max(score)
print(sum(score) / max_score * 100 / len(score))
