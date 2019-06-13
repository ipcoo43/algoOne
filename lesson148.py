# 평균 점수

scores = []
for i in range(5):
    score = int(input('>>> ').strip())
    if score < 40:
        score = 40
    scores.append(score)
avg = round(sum(scores)/5)
print('result : ',avg)