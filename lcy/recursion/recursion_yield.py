

def count_participation_one(n,m):
    """
    >>> count_participation_one(6,4)
    9
    """
    if n == 0:  
        """n=0时表示正确划分了"""
        return 1
    elif m == 0:
        return 0
    elif n < 0:
        return 0
    else:
        with_m=count_participation_one(n-m,m)
        without_m=count_participation_one(n,m-1)
        return with_m+without_m



def count_participation_two(n,m):
    """
    >>> count_participation_two(6,4)
    9
    """
    if m == 0 or n < 0:
        return 0
    else:
        exact_match=0
        if n==m:
            exact_match=1
        with_m=count_participation_two(n-m,m)
        without_m=count_participation_two(n,m-1)
        return exact_match+with_m+without_m


def list_participation(n,m):
    """
    >>> for p in list_participation(6,4):print(p)
    [4, 2]
    [4, 1, 1]
    [3, 3]
    [3, 2, 1]
    [3, 1, 1, 1]
    [2, 2, 2]
    [2, 2, 1, 1]
    [2, 1, 1, 1, 1]
    [1, 1, 1, 1, 1, 1]
    """
    if m == 0 or n < 0:
        return []
    else:
        exact_match=[]
        if n==m:
            exact_match=[[m]]
        with_m=[[m]+x for x in list_participation(n-m,m)]
        without_m=list_participation(n,m-1)
        return exact_match+with_m+without_m


def string_participation(n,m):
    """
    >>> for p in string_participation(6,4):print(p)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if m == 0 or n < 0:
        return []
    else:
        exact_match=[]
        if n==m:
            exact_match=[str(m)]
        with_m=[str(m)+' + ' +x for x in string_participation(n-m,m)]
        without_m=string_participation(n,m-1)
        return exact_match+with_m+without_m


def yield_participation(n,m):
    """
    >>> for p in yield_participation(6,4):print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
   
    if n > 0 and m > 0:
        if n==m:
            yield str(m)
        for p in yield_participation(n-m,m):
            yield p +' + '+str(m)
        yield from yield_participation(n,m-1)
        
 
