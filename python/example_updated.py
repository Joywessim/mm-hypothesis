import random
from math import cos, sin, pi, floor
from typing import List, Tuple


def example_updated(sampleparam: int, rgparam: int) -> Tuple[List[List[float]], List[List[float]], List[List[float]], int]:
    """Generate sample points from a sphere and a line.

    Parameters
    ----------
    sampleparam : int
        Controls the number of generated points.
    rgparam : int
        Seed for the random number generator.
    """
    random.seed(rgparam)
    count = int(floor(pi * sampleparam))
    theta = [pi * random.random() for _ in range(count)]
    phi = [2 * pi * random.random() for _ in range(count)]

    spheresample = [
        [0.5 * sin(t) * cos(p), 0.5 * sin(t) * sin(p), 0.5 * cos(t)]
        for t, p in zip(theta, phi)
    ]

    sz = int(floor(0.5 * sampleparam))
    r = [2 * (random.random() - 0.5) for _ in range(sz)]
    ind = [i for i, val in enumerate(r) if val >= 0.5 or val <= -0.5]
    linesample = [[r[i], 0.0, 0.0] for i in ind]

    sample = spheresample + linesample
    sample.extend([[0.5, 0.0, 0.0], [-0.5, 0.0, 0.0]])
    samplesize = len(sample)
    return sample, spheresample, linesample, samplesize
