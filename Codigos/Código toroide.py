import numpy as np
import matplotlib.pyplot as plt

# Establecemos las constantes fundamentales
carga_electron = 1.602e-19  # Carga elemental del electrón (C)
masa_electron = 9.109e-31   # Masa del electrón (kg)
vel_luz = 3.0e8             # Velocidad de la luz (m/s)

# Definimos los parámetros de los campos
campo_mag = 1e-3            # Intensidad del campo magnético (Tesla)
campo_elec = 1e-3           # Intensidad del campo eléctrico (V/m)

# Calculamos la frecuencia de ciclotrón
freq_ciclo = carga_electron * campo_mag / (masa_electron * vel_luz)

# Función que calcula la trayectoria trocoidal
def trayectoria_trocoide(t, coef_amplitud, vel_luz, campo_elec, campo_mag, freq_ciclo):
    x = (coef_amplitud / freq_ciclo) * np.sin(freq_ciclo * t) + (vel_luz * campo_elec / campo_mag) * t
    y = (coef_amplitud / freq_ciclo) * (np.cos(freq_ciclo * t) - 1)
    return x, y

# Creamos un arreglo temporal para la simulación
tiempo = np.linspace(0, 10, 1000)

# Caso 1: coef_amplitud > |vel_luz * campo_elec / campo_mag|
amp1 = 2 * (vel_luz * campo_elec / campo_mag)
x1, y1 = trayectoria_trocoide(tiempo, amp1, vel_luz, campo_elec, campo_mag, freq_ciclo)

# Caso 2: coef_amplitud < |vel_luz * campo_elec / campo_mag|
amp2 = 0.5 * (vel_luz * campo_elec / campo_mag)
x2, y2 = trayectoria_trocoide(tiempo, amp2, vel_luz, campo_elec, campo_mag, freq_ciclo)

# Caso 3: coef_amplitud = |vel_luz * campo_elec / campo_mag| (Trayectoria ciclóide)
amp3 = abs(vel_luz * campo_elec / campo_mag)
x3, y3 = trayectoria_trocoide(tiempo, amp3, vel_luz, campo_elec, campo_mag, freq_ciclo)

# Configuramos la figura y los subgráficos
plt.figure(figsize=(12, 8))

# Primer subgráfico: coef_amplitud mayor
plt.subplot(3, 1, 1)
plt.plot(x1, y1, label=r"$coef > \left|\frac{vel\_luz \times campo\_elec}{campo\_mag}\right|$", color="blue", linewidth=2)
plt.title("Trayectoria Trocoidal: coef_amplitud mayor", fontsize=14)
plt.xlabel("x(t)", fontsize=12)
plt.ylabel("y(t)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Segundo subgráfico: coef_amplitud menor
plt.subplot(3, 1, 2)
plt.plot(x2, y2, label=r"$coef < \left|\frac{vel\_luz \times campo\_elec}{campo\_mag}\right|$", color="red", linewidth=2)
plt.title("Trayectoria Trocoidal: coef_amplitud menor", fontsize=14)
plt.xlabel("x(t)", fontsize=12)
plt.ylabel("y(t)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Tercer subgráfico: coef_amplitud igual (cicloide)
plt.subplot(3, 1, 3)
plt.plot(x3, y3, label=r"$coef = \left|\frac{vel\_luz \times campo\_elec}{campo\_mag}\right|$ (Cicloide)", color="green", linewidth=2)
plt.title("Trayectoria Trocoidal: coef_amplitud igual (Cicloide)", fontsize=14)
plt.xlabel("x(t)", fontsize=12)
plt.ylabel("y(t)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Ajustamos la distribución y mostramos la gráfica
plt.tight_layout()
plt.show()