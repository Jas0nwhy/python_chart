import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('data.csv')

# 设置颜色和标记
colors = ['#b0c4de', '#f08080', '#90ee90', '#ffa07a', '#afeeee']
markers = ['o', 's', 'D', 'x', '^']

# 绘制点线图
fig, ax = plt.subplots(figsize=(10, 5))

for key, grp in df.groupby(['Node']):
    ax = grp.plot(ax=ax, kind='line', x='Round', y='Trust', label=key, color=colors[key], marker=markers[key], markersize=8)

# 添加标题和标签
ax.set_title('Prediction Node Trustworthiness over Time', fontsize=18)
ax.set_xlabel('Round', fontsize=16)
ax.set_ylabel('Trustworthiness', fontsize=16)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# 显示和保存图像
plt.tight_layout()
plt.savefig('trustworthiness.png', dpi=300)
plt.show()
