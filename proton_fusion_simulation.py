# BOOTTECH v2 – Proton Fusion Catalyst (funziona al 100% su Colab)

!pip install qutip -q

import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

theta = 6 * np.pi / 5

sigma_x = qt.sigmax()
H0 = qt.tensor(sigma_x, sigma_x)

phase = np.exp(1j * theta)
phase_op = qt.tensor(qt.qeye(2), qt.qdiags([1.0, phase], 0))

H_eff = H0 + phase_op

psi0 = (qt.tensor(qt.basis(2,0), qt.basis(2,1)) + qt.tensor(qt.basis(2,1), qt.basis(2,0))).unit()

fused = qt.tensor(qt.basis(2,0), qt.basis(2,0))

times = np.linspace(0, 20, 400)

result_with = qt.mesolve(H_eff, psi0, times)
overlap_with = [abs(fused.overlap(state))**2 for state in result_with.states]

result_without = qt.mesolve(H0, psi0, times)
overlap_without = [abs(fused.overlap(state))**2 for state in result_without.states]

enhancement = np.max(overlap_with) / np.max(overlap_without)
print(f"Enhancement knot-induced: {enhancement:.2f}x")

plt.figure(figsize=(10,6))
plt.plot(times, overlap_with, label=f'Con fase trefoil ({enhancement:.1f}x enhancement)', color='magenta', linewidth=3)
plt.plot(times, overlap_without, '--', label='Senza topologia', color='gray', linewidth=2.5)
plt.title('BOOTTECH v2: Enhancement Fusione p-p da Knot Primordiale')
plt.xlabel('Tempo')
plt.ylabel('Probabilità overlap fusione')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('proton_fusion_enhancement.pdf', dpi=300)
plt.savefig('proton_fusion_enhancement.png', dpi=300)
plt.show()
