import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Histogram (distribution of data) ---
data = np.random.randn(1000)
plt.figure(figsize=(7, 4))
plt.hist(data, bins=30, color='steelblue', edgecolor='white')
plt.title('Normal Distribution')
plt.show()