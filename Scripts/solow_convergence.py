import numpy as np
import matplotlib.pyplot as plt

# Simplified Solow model: dK/dt = s A K^alpha - delta K
A = 1.0
alpha = 0.5
s = 0.20
delta = 0.10
K0 = 0.25
T = 100.0
dt = 0.02

K_star = (s * A / delta) ** (1.0 / (1.0 - alpha))

t = np.arange(0.0, T + dt, dt)
K = np.empty_like(t)
K[0] = K0

for i in range(len(t) - 1):
    dK = s * A * K[i] ** alpha - delta * K[i]
    K[i + 1] = K[i] + dt * dK

gK = s * A * K ** (alpha - 1.0) - delta

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(t, K, label=r'$K(t)$')
ax.axhline(K_star, linestyle='--', label=rf'$K^*={K_star:.1f}$')
ax.set_xlabel('Time')
ax.set_ylabel('Capital stock $K$')
ax.set_title('Solow convergence to the steady state')
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('Figures/solow_convergence_levels.png', dpi=180)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(t, gK, label=r'$g_K=\dot K/K$')
ax.axhline(0.0, linestyle='--', label='steady-state growth = 0')
ax.set_xlabel('Time')
ax.set_ylabel('Capital growth rate')
ax.set_title('Capital growth rate decays toward zero')
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('Figures/solow_convergence_growth.png', dpi=180)
plt.close(fig)

print(f'K* = {K_star:.6g}')
print(f'final K = {K[-1]:.6g}')
print(f'final gK = {gK[-1]:.6g}')
