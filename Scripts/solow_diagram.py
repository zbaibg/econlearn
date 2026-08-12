import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

A = 1.0
alpha = 0.5
delta = 0.10
s1 = 0.20
s2 = 0.35

K = np.linspace(0, 25, 600)
F = A * K**alpha
investment1 = s1 * F
investment2 = s2 * F
depreciation = delta * K

K1_star = (s1 * A / delta) ** (1 / (1 - alpha))
K2_star = (s2 * A / delta) ** (1 / (1 - alpha))

Path('Figures').mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 5.2), dpi=180, facecolor='white')
ax.set_facecolor('white')
ax.plot(K, investment1, label=rf'$s_1F(K)$, $s_1={s1:.2f}$', linewidth=2)
ax.plot(K, investment2, label=rf'$s_2F(K)$, $s_2={s2:.2f}$', linewidth=2, linestyle='--')
ax.plot(K, depreciation, label=rf'$\delta K$, $\delta={delta:.2f}$', linewidth=2)

for kstar, yoff in [(K1_star, 0.03), (K2_star, 0.06)]:
    ystar = delta * kstar
    ax.scatter([kstar], [ystar], zorder=5)
    ax.axvline(kstar, linestyle=':', linewidth=1)
    ax.annotate(rf'$K^*={kstar:.2f}$', xy=(kstar, ystar),
                xytext=(kstar + 0.5, ystar + yoff), fontsize=10)

# Direction of motion of K around the first stable fixed point.
for x in [0.8, 1.8, 3.0]:
    ax.annotate('', xy=(x + 0.7, 0.07), xytext=(x, 0.07),
                arrowprops=dict(arrowstyle='->', lw=1.2))
for x in [5.2, 7.0, 9.0]:
    ax.annotate('', xy=(x - 0.7, 0.07), xytext=(x, 0.07),
                arrowprops=dict(arrowstyle='->', lw=1.2))

ax.text(K1_star, 0.015, r'stable $K_1^*$', ha='center', va='bottom', fontsize=9)
ax.set_xlabel('Capital stock $K$')
ax.set_ylabel('Flow per unit time')
ax.set_title('Solow model: investment and depreciation')
ax.set_xlim(0, 14)
ax.set_ylim(0, 1.5)
ax.grid(True, alpha=0.25)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig('Figures/solow_steady_state.png', dpi=180, facecolor='white', transparent=False)
plt.close(fig)
