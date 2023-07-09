import matplotlib.pyplot as plt
import numpy as np

# 数据
nodes = [3, 5, 7, 9]
data_size = [10, 20, 30, 60, 120]
success_rate = np.array([
    [0.976, 0.941, 0.898, 0.802, 0.685],
    [0.989, 0.962, 0.917, 0.819, 0.702],
    [0.993, 0.973, 0.933, 0.834, 0.718],
    [0.996, 0.981, 0.949, 0.85, 0.741]
])
throughput = np.array([
    [303.6, 195.4, 135.2, 74.3, 34.6],
    [496.7, 285.3, 173.7, 94.2, 43.9],
    [690.6, 407.1, 245.3, 132.6, 64.9],
    [910.2, 536.7, 324.4, 174.9, 85.3]
])

# 绘图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

# 第一个子图：Success Rate
for i, node in enumerate(nodes):
    ax1.plot(data_size, success_rate[i], label=f"{node} Nodes", marker='o')
ax1.set_xlabel("Data Size (MB)")
ax1.set_ylabel("Success Rate")
ax1.set_xticks(data_size)
ax1.set_ylim(0.6, 1.0)
ax1.legend()

# 第二个子图：Throughput
for i, node in enumerate(nodes):
    ax2.plot(data_size, throughput[i], label=f"{node} Nodes", marker='o')
ax2.set_xlabel("Data Size (MB)")
ax2.set_ylabel("Throughput (tx/s)")
ax2.set_xticks(data_size)
ax2.legend()

# 设置全局参数
plt.tight_layout()
plt.savefig("figure.png", dpi=300, bbox_inches='tight')
plt.show()

# 绘制大图
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

