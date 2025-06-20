from math import sqrt
from typing import Iterable, List, Tuple


def ball(data: Iterable[Iterable[float]], p: Iterable[float], r: float) -> Tuple[List[List[float]], List[bool]]:
    """Return points within radius ``r`` of center ``p``.

    Parameters
    ----------
    data : iterable of iterables
        Points in the dataset.
    p : iterable
        Center point.
    r : float
        Radius of the ball.

    Returns
    -------
    v : list of points
        Points within the ball.
    B : list of bool
        Membership mask for each point in ``data``.
    """
    center = list(p)
    r2 = r * r
    v = []
    mask = []
    for row in data:
        dist2 = sum((c - cp) ** 2 for c, cp in zip(row, center))
        inside = dist2 < r2
        mask.append(inside)
        if inside:
            v.append(list(row))
    return v, mask
