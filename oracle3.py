import matplotlib.pyplot as plt
import numpy as np

# 设置风格
#('ieee')

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

# 绘制第一个子图
x = np.array([10, 20, 30, 60, 120])
y1 = np.array([0.976, 0.941, 0.898, 0.802, 0.685])
y2 = np.array([0.989, 0.962, 0.917, 0.819, 0.702])
y3 = np.array([0.993, 0.973, 0.933, 0.834, 0.718])
y4 = np.array([0.996, 0.981, 0.949, 0.85, 0.741])
ax1.plot(x, y1, marker='o', label='3 Nodes')
ax1.plot(x, y2, marker='s', label='5 Nodes')
ax1.plot(x, y3, marker='*', label='7 Nodes')
ax1.plot(x, y4, marker='^', label='9 Nodes')
ax1.set_xlabel('Data Size (MB)')
ax1.set_ylabel('Success Rate')
ax1.legend()

# 绘制第二个子图
x = np.array([3, 5, 7, 9])
y1 = np.array([303.6, 496.7, 690.6, 910.2])
y2 = np.array([195.4, 285.3, 407.1, 536.7])
y3 = np.array([135.2, 173.7, 245.3, 324.4])
y4 = np.array([74.3, 94.2, 132.6, 174.9])
y5 = np.array([34.6, 43.9, 64.9, 85.3])
ax2.plot(x, y1, marker='o', label='10MB')
ax2.plot(x, y2, marker='s', label='20MB')
ax2.plot(x, y3, marker='*', label='30MB')
ax2.plot(x, y4, marker='^', label='60MB')
ax2.plot(x, y5, marker='x', label='120MB')
ax2.set_xlabel('Nodes')
ax2.set_ylabel('Throughput (tx/s)')
ax2.legend()

# 调整布局
fig.tight_layout()

# 保存图像
plt.savefig('figure.png')
