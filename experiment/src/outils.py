from collections import Counter
from scipy.special import kl_div
import matplotlib.pyplot as plt

def draw_distribution(config, data, nbins, outfile, divisor=None):
    fig, axs = plt.subplots()
    fig.set_figwidth(10)
    axs.hist(data, bins=nbins, edgecolor="white")
    plt.savefig(outfile)

    M = len(data)
    counter = Counter(data)

    observation = [c for _,c in sorted(counter.items())]
    expectation = [M/nbins] * nbins

    if observation == []:
        observation = [0] * nbins

    if M == 0:
        proba = [0 for _ in observation]
    else:
        proba = [c/M for c in observation]

    KL = sum(list(kl_div(proba, [1/16] * 16)))

    if divisor != None:
        observation = [x/divisor for x in observation]
        expectation = [x/divisor for x in expectation]

    print(f"Number of samples: {M}")
    print("  PROBA : ", end="")
    for p in proba:
        print(f"{p*100:.3f} ", end="")
    print()
    print(f"KL: {KL}")


def nibble_tobits(x):
    assert 0 <= x <= 15
    x0 = x & 1
    x1 = (x >> 1) & 1
    x2 = (x >> 2) & 1
    x3 = (x >> 3) & 1
    return x0, x1, x2, x3

def bits_tonibble(x0, x1, x2, x3):
    return (x3 << 3) | (x2 << 2) | (x1 << 1) | (x0)

def mul4(x):
    x0, x1, x2, x3 = nibble_tobits(x)
    y0 = x2
    y1 = x2 ^ x3
    y2 = x0 ^ x3
    y3 = x1
    y = bits_tonibble(y0, y1, y2, y3)
    return y

def mul2(x):
    x0, x1, x2, x3 = nibble_tobits(x)
    y0 = x3
    y1 = x0 ^ x3
    y2 = x1
    y3 = x2
    y = bits_tonibble(y0, y1, y2, y3)
    return y

def mul13(x):
    x0, x1, x2, x3 = nibble_tobits(x)
    y0 = x0 ^ x1 ^ x2
    y1 = x3
    y2 = x0
    y3 = x0 ^ x1
    y = bits_tonibble(y0, y1, y2, y3)
    return y

def mul9(x):
    x0, x1, x2, x3 = nibble_tobits(x)
    y0 = x0 ^ x1
    y1 = x2
    y2 = x3
    y3 = x0
    y = bits_tonibble(y0, y1, y2, y3)
    return y