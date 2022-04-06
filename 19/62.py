TARGET = 30
results = {}
def gameResult(s, k):
    if (s, k) in results: return results[(s, k)]
    if s + k >= TARGET: return 0
    nextCodes = [gameResult(s + 1, k), gameResult(s * 2, k),
                 gameResult(s, k + 1), gameResult(s, k * 2)]
    negative = [c for c in nextCodes if c <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(nextCodes)
    results[(s, k)] = res
    return res

nswr = []
for S in range(1, 30):
    for K in range(1, 30):
        r = gameResult(S, K)
        if r == -1:
            nswr.append((S, K))
print(len(set(nswr)))

nswr = []
for S in range(1, 30):
    K = 6
    r = gameResult(S, K)
    if r == 2:
        nswr.append((S, K))
print(set(nswr))

nswr = []
for S in range(1, 30):
    for K in range(1, 30):
        r = gameResult(S, K)
        if r == -2:
            nswr.append((S, K))
print(len(set(nswr)))




