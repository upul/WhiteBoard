import random
import math


def estimate_pi(n_samples=202400):
    in_circle = 0
    for _ in range(n_samples):
        x, y = random.random(), random.random()
        if (x**2 + y**2) <= 1:
            in_circle += 1
    return 4.0 * (in_circle / n_samples)


if __name__ == '__main__':
    for _ in range(10):
        assert abs(math.pi - estimate_pi()) < 0.001
