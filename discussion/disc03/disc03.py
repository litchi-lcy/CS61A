def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        print(n%10)
        swipe(n//10)
        print(n%10)
       

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n<=2:
        return n 
    else:
        return n * skip_factorial(n - 2)
    

def is_prime(n):
    def check(i):
        if i == 1 :
            return True
        elif n % i == 0 :
            return False
        else:
            return check(i-1)
    return check(n-1)



def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    n = n // 2
    return 1 + hailstone(n)

def odd(n):
    if n == 1:
        return 1
    n = 3 * n + 1
    return 1+ hailstone(n)
    "*** YOUR CODE HERE ***"  



def seven(player_number,over_digit):
    def game(player,digit,way):
        print('player' + str(player) + 'say' + str(digit))
        if digit == over_digit:
            return 
        elif digit % 7 == 0 or has_seven(digit):
            way = -way
            player = (player + way) % player_number
        else :
            player = (player + way) % player_number
        if player == 0:
            player = 5
        return game(player,digit+1,way)
    return game(1,1,1)
    
def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    return has_seven(n//10)


