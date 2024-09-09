import sys
import itertools

read = sys.stdin.readline
res = []
T = int(read())
for _ in range(T):
    max_score = 0
    max_score_count = 0
    N, M = map(int, read().split())

    score_method = [0]*100
    for _ in range(M):
        v, a, b = map(int, read().split())
        score_method[10*a+b] += v

    for case in itertools.permutations([i for i in range(1, N+1)], N):
        score = 0
        for i in range(N-1):
            for j in range(i+1, N):
                score += score_method[case[i]*10+case[j]]
        if score > max_score:
            max_score = score
            max_score_count = 1
        elif score == max_score:
            max_score_count += 1

    res.append(str(max_score) + " " + str(max_score_count))
print('\n'.join(res))