def interlaced_spiral(s):
    n = int((s - 1) ** .5) + 1
    for x, r in enumerate(range(n, 0, -2)):
        for y in range(x, x+r-(r>1)):
            for _ in range(4):
                yield x * n + y
                if r == 1: return
                x, y = y, n-x-1
