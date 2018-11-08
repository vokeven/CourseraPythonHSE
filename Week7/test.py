def make_min(*, lo, hi):
    def inner(first, *args):
        res = hi
        for arg in (first,) + args:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)
    return inner


bounded_min = make_min(lo=0, hi=255)
print(bounded_min(-5, 12, 13))