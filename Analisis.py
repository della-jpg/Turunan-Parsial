import streamlit as st
import numpy as np
import matplotlib.py as plt
from toolkits.mplot3d import Axes3D

st.title("Visualisasi Permukaan Fungsi Produksi Tahu (Cobb-Douglas)")

st.markdown("""
Model fungsi produksi:  
**Q(x, y) = A · x^α · y^β**  
Dimana:  
- x = jumlah kedelai (kg per hari)  
- y = jumlah tenaga kerja (orang per hari)  
""")

# Sidebar input parameter
st.sidebar.header("Parameter Fungsi Produksi")
A = st.sidebar.slider("A (Total Faktor Produktivitas)", 0.1, 2.0, 1.0, 0.1)
alpha = st.sidebar.slider("Alpha (elastisitas kedelai)", 0.0, 1.0, 0.5, 0.05)
beta = st.sidebar.slider("Beta (elastisitas tenaga kerja)", 0.0, 1.0, 0.5, 0.05)

# Rentang input
x_vals = np.linspace(1, 100, 50)
y_vals = np.linspace(1, 100, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Fungsi produksi Cobb-Douglas
Z = A * (X ** alpha) * (Y ** beta)

# Plot permukaan
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Kedelai (kg/hari)')
ax.set_ylabel('Tenaga Kerja (org/hari)')
ax.set_zlabel('Output (unit tahu)')
ax.set_title('Permukaan Fungsi Produksi Tahu')

st.pyplot(fig)
