def permutation(iterable, n, prefix=None):
    prefix = prefix or []
    if n == 0:
        print(prefix, end=',')
        return
    for i in iterable:
        prefix.append(i)
        permutation(iterable, n-1, prefix)
        prefix.remove(i)

permutation('123456789', 2)