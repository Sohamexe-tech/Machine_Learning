import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Scatter Plot ---
x = np.random.rand(100)
y = 2*x + np.random.randn(100)*0.2

plt.figure(figsize=(6, 5))
plt.scatter(x, y, alpha=0.6, color='coral')
plt.title('Scatter: x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()