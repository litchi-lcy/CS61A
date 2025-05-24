def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10

    race(11,15)进行无限循环 
    minutes=0: tortoise=0, hare=0 → 进入循环
    minutes=1: tortoise=11, hare=15（因为1%10=1<5）→ 11 < 15 → 继续
    minutes=2: tortoise=22, hare=30 → 22 < 30 → 继续
    minutes=3: tortoise=33, hare=45 → 33 < 45 → 继续
    minutes=4: tortoise=44, hare=60 → 44 < 60 → 继续
    minutes=5: tortoise=55, hare=75 → 55 < 75 → 继续
    minutes=6: tortoise=66, hare=75（6%10=6≥5，不增加）→ 66 < 75 → 继续
    minutes=7: tortoise=77, hare=75 → 77 > 75 → 此时 tortoise - hare=2，非零，循环继续？
    哦，这里发现问题！原循环条件是 minutes == 0 or tortoise - hare，
    即当 tortoise > hare 时，tortoise - hare 是正数，非零，条件为True，
    循环继续。但此时 tortoise 已经超过了 hare，而题目要求的是
    “first catches up to the hare”，即当 tortoise 第一次等于 hare 时
    停止。如果 tortoise 直接超过，而没有等于的情况，循环会一直运行，
    导致无限循环。

    >>>race(3,5)
    >>>25
    """

    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes




def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i=1
    while i<=n:
        if i%3==0 and i%5==0:
            print("fizzebuzz")
        elif i%3==0 and i%5!=0:
            print("fizz")
        elif i%5==0 and i%3!=0:
            print("buzz")
        else:
            print(i)
        i=i+1
