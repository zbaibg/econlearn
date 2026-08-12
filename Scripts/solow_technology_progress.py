import numpy as np
import matplotlib.pyplot as plt

# Solow model with labor-augmenting technology:
#   Y = K^alpha (A L)^(1-alpha)
# Per worker:
#   y = A^(1-alpha) k^alpha
# Per effective worker x = k/A:
#   dx/dt = s x^alpha - (delta + g_A) x

alpha = 0.35
s = 0.25
delta = 0.05
g_A = 0.02
A0 = 1.0
x0 = 0.5
T = 140.0
dt = 0.02

# Balanced-growth fixed point in effective-worker coordinates.
x_star = (s / (delta + g_A)) ** (1.0 / (1.0 - alpha))

t = np.arange(0.0, T + dt, dt)
A = A0 * np.exp(g_A * t)
x = np.empty_like(t)
x[0] = x0

for i in range(len(t) - 1):
    dx = s * x[i] ** alpha - (delta + g_A) * x[i]
    x[i + 1] = x[i] + dt * dx

k = A * x
y = A * x**alpha

g_x = s * x ** (alpha - 1.0) - (delta + g_A)
g_k = g_A + g_x
g_y = g_A + alpha * g_x

# Counterfactual with no technological progress, using the same initial
# per-worker capital and A0=1.
x_zero_star = (s / delta) ** (1.0 / (1.0 - alpha))
x_zero = np.empty_like(t)
x_zero[0] = x0
for i in range(len(t) - 1):
    dx = s * x_zero[i] ** alpha - delta * x_zero[i]
    x_zero[i + 1] = x_zero[i] + dt * dx

y_zero = x_zero**alpha
g_y_zero = alpha * (s * x_zero ** (alpha - 1.0) - delta)

# 1) Production-function shift at fixed per-worker capital k.
k_grid = np.linspace(0.05, 20.0, 800)
fig, ax = plt.subplots(figsize=(8, 5))
for A_level in [1.0, 1.5, 2.0]:
    y_grid = A_level ** (1.0 - alpha) * k_grid**alpha
    ax.plot(k_grid, y_grid, label=rf'$A={A_level:g}$')
ax.set_xlabel(r'Capital per worker $k$')
ax.set_ylabel(r'Output per worker $y$')
ax.set_title('Technological progress shifts the production function upward')
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('Figures/technology_production_shift.png', dpi=180)
plt.close(fig)

# 2) Output paths: catch-up plus technology vs catch-up without technology.
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(t, y, label=rf'$g_A={100*g_A:.0f}\%$')
ax.plot(t, y_zero, label=r'$g_A=0$')
ax.set_xlabel('Time')
ax.set_ylabel(r'Output per worker $y$')
ax.set_title('Technology prevents per-worker output from settling at a fixed level')
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('Figures/technology_output_paths.png', dpi=180)
plt.close(fig)

# 3) Growth-rate decomposition. With technology, early growth contains
# catch-up (x rising toward x*) plus g_A; asymptotically g_y -> g_A.
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(t, 100.0 * g_y, label=rf'$g_y$, $g_A={100*g_A:.0f}\%$')
ax.plot(t, 100.0 * g_y_zero, label=r'$g_y$, $g_A=0$')
ax.axhline(100.0 * g_A, linestyle='--', label=rf'long-run $g_A={100*g_A:.0f}\%$')
ax.axhline(0.0, linestyle=':', label='zero growth')
ax.set_xlabel('Time')
ax.set_ylabel('Per-worker output growth rate (%)')
ax.set_title('Catch-up growth fades; technology growth remains')
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('Figures/technology_growth_rates.png', dpi=180)
plt.close(fig)

print(f'x* with technology = {x_star:.6f}')
print(f'x*(0-tech counterfactual) = {x_zero_star:.6f}')
print(f'initial x = {x0:.6f}')
print(f'initial g_y with technology = {100*g_y[0]:.3f}%')
print(f'final g_y with technology = {100*g_y[-1]:.3f}%')
print(f'final g_y without technology = {100*g_y_zero[-1]:.3f}%')
