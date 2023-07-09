import matplotlib.pyplot as plt
import numpy as np

# 数据
nodes = [3, 5, 7, 9]
transactions = [50, 100, 150, 200, 250, 300]
data = np.array([
    [0.80, 0.68, 0.54, 0.40, 0.28, 0.20],
    [0.92, 0.88, 0.76, 0.62, 0.48, 0.32],
    [0.95, 0.92, 0.85, 0.76, 0.64, 0.50],
    [0.96, 0.94, 0.90, 0.84, 0.76, 0.68]
])

# 绘制热力图
fig, ax = plt.subplots()
im = ax.imshow(data, cmap='YlGn')

# 添加轴标签
ax.set_xticks(np.arange(len(transactions)))
ax.set_yticks(np.arange(len(nodes)))
ax.set_xticklabels(transactions)
ax.set_yticklabels(nodes)
ax.set_xlabel('Amount of cross-chain transaction data(MB)')
ax.set_ylabel('Number of oracle nodes')

# 添加每个单元格的文本注释
for i in range(len(nodes)):
    for j in range(len(transactions)):
        text = ax.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center', color='black')

# 添加颜色条
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Oracle validation success rate', rotation=-90, va="bottom")

# 添加图表标题
#plt.title("Impact of the number of workgroup nodes and cross-chain data capacity on the success rate of data authenticity verification")
plt.savefig('热力图.png')
# 展示图表
plt.show()
