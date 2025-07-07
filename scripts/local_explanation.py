import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import euclidean_distances

np.random.seed(42)

def black_box_predict(X):
    return (X[:, 1] > np.sin(X[:, 0]) + 0.5 * np.cos(2 * X[:, 0])).astype(int)

x_interest = np.array([[1.5, np.sin(1.5) + 0.5 * np.cos(2 * 1.5)]])

n_samples = 500
X_sampled = x_interest + np.random.normal(0, 0.75, size=(n_samples, 2))
y_sampled = black_box_predict(X_sampled)

dists = euclidean_distances(X_sampled, x_interest)
weights = np.exp(-(dists ** 2) / 0.75**2).flatten()

model_local = LogisticRegression()
model_local.fit(X_sampled, y_sampled, sample_weight=weights)

xx, yy = np.meshgrid(np.linspace(-1, 4, 500), np.linspace(-2, 3, 500))
grid = np.c_[xx.ravel(), yy.ravel()]
Z = black_box_predict(grid).reshape(xx.shape)

fig, ax = plt.subplots(figsize=(8, 6))

ax.contourf(xx, yy, Z, alpha=0.3, cmap='cool')

scatter = ax.scatter(X_sampled[:, 0], X_sampled[:, 1],
                     c=y_sampled, cmap='cool',
                     s=60 * weights, edgecolors='k', alpha=0.8)

ax.scatter(x_interest[0, 0], x_interest[0, 1],
           color='red', s=120, edgecolors='k', marker='*', label='Point of Interest')

coef = model_local.coef_[0]
intercept = model_local.intercept_[0]
slope = -coef[0] / coef[1]
intercept_y = -intercept / coef[1]
x_vals = np.array(ax.get_xlim())
y_vals = slope * x_vals + intercept_y
ax.plot(x_vals, y_vals, color='black', linestyle='--', linewidth=2, label='Local Decision Boundary')

ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.legend(loc='upper right')
ax.set_title("LIME: Local Explanation of a Black Box Model")

plt.tight_layout()
plt.savefig("lime_figure3_replicated.svg", format="svg")
plt.savefig("lime_figure3_replicated.pdf", format="pdf")
plt.show()
