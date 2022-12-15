def phone_number(n):
    import random
    spisok = []
    number = '0123456789'
    ukr_number = '+38'
    operator = '098'
    for i in range(n):
        numer = ukr_number + operator
        for a in range(7):
            y = random.choice(number)
            numer += y

        spisok.append(numer)
    return (spisok)
