import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

A = 1.0
alpha = 0.5
delta = 0.1
K = np.linspace(0, 40, 500)
F = A * K**alpha
D = delta * K
K_gr = (alpha * A / delta) ** (1/(1-alpha))
F_gr = A * K_gr**alpha
D_gr = delta * K_gr
C_gr = F_gr - D_gr
s_gr = delta * K_gr / F_gr

Path('Figures').mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(9, 6), facecolor='white')
ax.set_facecolor('white')
ax.plot(K, F, label=r'$F(K)=A K^{\alpha}$')
ax.plot(K, D, label=r'$\delta K$')
ax.vlines(K_gr, 0, F_gr, linestyles='--', label=r'$K_{GR}$')
ax.annotate('', xy=(K_gr, F_gr), xytext=(K_gr, D_gr), arrowprops=dict(arrowstyle='<->', lw=2))
ax.text(K_gr + 0.8, (F_gr + D_gr)/2, r'$C^*=F(K)-\delta K$', va='center')
ax.scatter([K_gr], [F_gr], zorder=5)
ax.scatter([K_gr], [D_gr], zorder=5)
ax.text(K_gr + 0.8, F_gr + 0.18, rf'$F(K_{{GR}})={F_gr:.1f}$')
ax.text(K_gr + 0.8, D_gr - 0.35, rf'$\delta K_{{GR}}={D_gr:.1f}$')
ax.text(K_gr - 3.5, -0.45, rf'$K_{{GR}}={K_gr:.0f}$')
ax.text(1.0, 5.2, rf'Max steady-state consumption at $K_{{GR}}$\n$F^\prime(K_{{GR}})=\delta$\n$s_{{GR}}={s_gr:.2f}$')
ax.set_xlim(0, 40)
ax.set_ylim(0, max(F)*1.12)
ax.set_xlabel('Capital stock $K$')
ax.set_ylabel('Output / depreciation')
ax.set_title('Solow Golden Rule: maximize steady-state consumption')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Figures/solow_golden_rule.png', dpi=200, facecolor='white', transparent=False)
plt.close(fig)
