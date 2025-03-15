def count_lucky_ticket3():
    """для 6-значных билетов"""
    count = 0
    for a1 in range(10):
        for a2 in range(10):
            for a3 in range(10):
                summA = a1+a2+a3
                for b1 in range(10):
                    for b2 in range(10):
                        b3 = summA-(b1+b2)
                        if 0 <= b3 < 10:
                            count += 1
    return count


def count_lucky_ticket(N, summA=0, summB=0):
    """в общем случае"""
    if N == 0:
        if summA == summB:
            return 1
        else:
            return 0
    count = 0
    for a in range(10):
        for b in range(10):
            count += count_lucky_ticket(N-1, summA=summA+a, summB=summB+b)
    return count

