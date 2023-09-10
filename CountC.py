try:
    t = int(input())
    while t:
        n = int(input())
        num = []
        y = input().split()
        for i in range(0, n):
            y[i] = int(y[i])
        num.append(y)
        y.reverse()
        z = " ".join(map(str, y))
        print(z)
        y.reverse()
        k = y[3::3]
        for j in range(0, len(k)):
            k[j] = k[j]+3
        q = " ".join(map(str, k))
        print(q)
        l = y[5::5]
        for p in range(0, len(l)):
            l[p] = l[p]-7
        w = " ".join(map(str, l))
        print(w)
        f = y[3:8]
        sum = 0
        for t in range(0, len(f)):
            sum = sum + f[t]
        print(sum)
        t = t-1
except:
    pass
