import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
x = np.array([0,0,0,100,100,100,200,200,200,300,300,300,400,400,400,500,500,500])
y = np.array([0,0,0,0.2,0.2,0.2,0.3333,0.3333,0.5,0.5,0.4,0.6,0.8,0.8,0.8,1,1,1])

plt.scatter(x, y, alpha=0.5)
plt.show()