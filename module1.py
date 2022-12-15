def random_abc(a, n, m):
    import random
    ABC = a
    for i in range(n):
        ryadok = ""
        for a in range(m):
            alf = random.choice(ABC)
            ryadok = ryadok + alf
        print(ryadok)
