import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Judul aplikasi
st.title("🧈 Visualisasi 3D: Fungsi Biaya Produksi Tahu")

st.write(r"""
Fungsi biaya produksi:
\[
C(x, y) = 2x^2 + 3xy + y^2 + 50
\]
di mana:
- \(x\) = jumlah kedelai (kg)  
- \(y\) = jumlah tenaga kerja (jam)
""")

# Rentang input
x_min, x_max = st.slider("Rentang x (kedelai)", 0, 50, (0, 20))
y_min, y_max = st.slider("Rentang y (tenaga kerja)", 0, 50, (0, 20))

# Grid untuk x dan y
x_vals = np.linspace(x_min, x_max, 50)
y_vals = np.linspace(y_min, y_max, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Fungsi biaya
Z = 2*X**2 + 3*X*Y + Y**2 + 50

# Plot 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
ax.set_xlabel('Kedelai (kg)')
ax.set_ylabel('Tenaga Kerja (jam)')
ax.set_zlabel('Biaya (ribu rupiah)')
ax.set_title('Permukaan Fungsi Biaya Produksi Tahu')

# Tampilkan di Streamlit
st.pyplot(fig)
