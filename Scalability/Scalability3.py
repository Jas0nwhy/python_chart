import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置颜色
#sns.set_palette("Paired")

# 模拟数据
data = {'Regulatory Relationship': ['1-1', '1-2', '2-1', '2-2', '2-3', '3-2', '3-3'],
        'Average Latency(s)':
[23.4801017,25.9532535,46.5394298,58.6864903,84.6933612,96.2814068,131.118007]

        }

# 转换为DataFrame格式
df = pd.DataFrame(data)

# 绘制统计图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 设置标题和轴标签
fig.suptitle('Latency Comparison', fontsize=14)
axes[0].set_title('Regulatory Relationship')
axes[1].set_title('Request-Response Relationship')
axes[0].set_xlabel('Regulatory Relationship')
axes[1].set_xlabel('Request-Response Relationship')
axes[0].set_ylabel('Average Latency (s)')
axes[1].set_ylabel('Average Latency (s)')

# 修改刻度线朝向
axes[0].tick_params(axis='both', direction='in')
axes[1].tick_params(axis='both', direction='in')

# 绘制对照组1：Regulatory Relationship
sns.barplot(ax=axes[0], x='Regulatory Relationship', y='Average Latency(s)', data=df, palette='BuGn_d')

# 绘制对照组2：Request-Response Relationship
data2 = {'Request-Response Relationship': ['1-1', '1-2', '2-1', '2-2', '2-3', '3-2', '3-3'],
         'Average Latency(s)': [22.645, 25.375, 44.810, 56.763, 81.927, 93.945, 127.568]}
df2 = pd.DataFrame(data2)
sns.barplot(ax=axes[1], x='Request-Response Relationship', y='Average Latency(s)', data=df2, palette='YlOrRd')

# save the chart as a high-quality PNG file
plt.savefig('Latency_Comparison.png', dpi=300)

# 显示图形
plt.show()
