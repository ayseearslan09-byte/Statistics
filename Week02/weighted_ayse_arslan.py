import random
def weighted_srs(data, n, weights=None, with_replacement=False):
    if with_replacement or weights is None:
        return random.choices(data, weights=weights, k=n) if with_replacement else random.sample(data, n)
    res, d_lst, w_lst = [], list(data), list(weights)
    for _ in range(n):
        idx = random.choices(range(len(d_lst)), weights=w_lst, k=1)[0]
        res.append(d_lst.pop(idx))
        w_lst.pop(idx)
    return res
