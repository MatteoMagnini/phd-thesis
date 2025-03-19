import numpy as np
import matplotlib.pyplot as plt


def recombinant_growth(n0=2, t_final=20, alpha=1.):
    """
    Combinatorial growth model.
    :param n0: starting value
    :param t_final: final time
    :param alpha: growth rate
    :return:
    """
    t_values = np.arange(t_final + 1)
    n_values = np.zeros(t_final + 1)
    n_values[0] = n0

    for t in range(t_final):
        n_values[t + 1] = n_values[t] + alpha * (n_values[t] ** 2)

    plt.figure(figsize=(8, 5))
    plt.plot(t_values, n_values, marker='o', linestyle='-', color='b', label='N(t)')
    plt.yscale('log')
    plt.xlabel("Time t")
    plt.ylabel("N(t)")
    plt.title(f"Weitzman model (n0={n0}, α={alpha})")
    plt.legend()
    plt.grid(True)
    plt.show()


recombinant_growth(alpha=0.05)
