import random

def bian(N):
    # 分而二以象两
    L = round(random.random() * (N - 2) + 1)
    # L = random.randint(4, 44)
    # L = 32
    R = N - L

    #挂一以象三
    x = 1
    L = L - 1

    # 揲之以四以象四时
    if L < 4:
        y = L
    else:
        if L % 4 == 0:
            y = 4
        else:
            y = L % 4

    if R < 4:
        z = R
    else:
        if R % 4 == 0:
            z = 4
        else:
            z = R % 4

    ce = x + y + z
    return N - ce, ce


def quYao():
    yuce1, ce1 = bian(49)
    yuce2, ce2 = bian(yuce1)
    yuce3, ce3 = bian(yuce2)
    ce = ce1 + ce2 + ce3
    n = 49 - ce
    # return n / 4
    return int(yuce3 / 4)


def quGua():
    gua = [quYao() for _ in range(6)]
    return gua


# For the output of quGua()
print(quGua())

# For the statistics part
gua = [quYao() for _ in range(1000)]
print(max(gua), min(gua))
