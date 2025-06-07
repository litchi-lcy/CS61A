def deep_map_mut(func, lnk):
    """Mutates a deep link lnk by replacing each item found with the
    result of calling func on the item. Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

>>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print(link1)
    <3 <4> 5 6>
    >>> # 禁止在调用 `deep_map_mut` 函数之前创建新的 `Link` 对象
    >>> Link.__init__, hold = lambda *args: print("请不要创建任何新的 `Link` 对象。"), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    if lnk is Link.empty:
        return
    elif isinstance(lnk.first, Link):
        deep_map_mut(func, lnk.first)
    else:
        lnk.first = func(lnk.first)
    deep_map_mut(func, lnk.rest)