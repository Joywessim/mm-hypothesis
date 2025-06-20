from typing import Iterable, List


def center(data: Iterable[Iterable[float]]) -> List[List[float]]:
    """Center data by subtracting the mean of each column."""
    data = [list(row) for row in data]
    if not data:
        return []
    n = len(data[0])
    means = [0.0] * n
    for row in data:
        for j, val in enumerate(row):
            means[j] += val
    m = len(data)
    means = [mval / m for mval in means]
    centered = []
    for row in data:
        centered.append([val - means[j] for j, val in enumerate(row)])
    return centered
