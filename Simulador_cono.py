Simulador_cono.py
Simulador_cono.py python import numpy as np import matplotlib.pyplot as plt

KERNEL DE VISUALIZACIÓN PARAMÉTRICA - SISTEMA LEMNISCÁTICO CONTINUO (1997)
Licencia: GNU General Public License v3.0
fig = plt.figure(figsize=(12, 6))

Bloque 1: El Escenario de la Antesala (Cono Recostado)
ax1 = fig.add_subplot(121, projection='3d') u = np.linspace(0.01, 2.0, 40) v = np.linspace(0, 2*np.pi, 40) U, V = np.meshgrid(u, v)

X1 = U Y1 = U * np.cos(V) * (1.0 / (1.0 + np.exp(-5 * (U - 1)))) # Círculo excéntrico (Tiempo) Z1 = U * np.sin(V) # Elipse axial (Espacio)

ax1.plot_surface(X1, Y1, Z1, cmap='twilight', alpha=0.7, edgecolor='none') ax1.set_title("Escenario de la Antesala\nCono Recostado (Espacio/Tiempo)") ax1.axis('off')

Bloque 2: El Compás de Espera (Lucidez Plena - El Plato y el Palito)
ax2 = fig.add_subplot(122, projection='3d') z_stick = np.linspace(0, 2.5, 20) ax2.plot(np.zeros_like(z_stick), np.zeros_like(z_stick), z_stick, color='black', linewidth=4, label='Palito (Eje Espacial)')

v_plate = np.linspace(0, 2*np.pi, 50) ax2.plot(1.0 * np.cos(v_plate), 1.0 * np.sin(v_plate), np.ones_like(v_plate) * 2.5, color='red', linewidth=3, label='Plato (Tiempo Unificado)') ax2.set_title("El Compás de Espera\nLucidez Plena (Equilibrio Ortogonal)") ax2.set_xlim(-1.5, 1.5); ax2.set_ylim(-1.5, 1.5); ax2.set_zlim(0, 3) ax2.axis('off')

plt.tight_layout() plt.show()
