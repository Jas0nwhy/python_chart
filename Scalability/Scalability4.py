# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 设置颜色
# # sns.set_palette('Paired')
#
# # 模拟数据
# data = {'Relationship': ['1-1', '1-2', '2-1', '2-2', '2-3', '3-2', '3-3']*2,
#         'Type': ['Publish-Subscribe']*7 + ['Request-Response']*7,
#         'Average Latency(s)': [23.4801017,25.9532535,46.5394298,58.6864903,84.6933612,96.2814068,131.118007,
#                                25.645, 63.375, 68.810, 87.763, 125.927, 186.945, 254.568]
#         }
#
# # 转换为DataFrame格式
# df = pd.DataFrame(data)
# #
# # 绘制统计图
# sns.barplot(x='Relationship', y='Average Latency(s)', hue='Type', data=df, palette={'Publish-Subscribe': '#2ecc71', 'Request-Response': '#0984e3'})
#
# # 设置标题和轴标签
# plt.title('Latency Comparison')
# plt.xlabel('Relationship')
# plt.ylabel('Average Latency (s)')
#
# # 修改刻度线朝向
# plt.tick_params(axis='both', direction='in')
#
# # save the chart as a high-quality PNG file
# plt.savefig('Latency_Comparison.png', dpi=300)
#
# # 显示图形
# plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 模拟数据
data = {'Regulatory Relationship': ['1-1', '1-2', '2-1', '2-2', '2-3', '3-2', '3-3'],
        'Average Latency(s)': [23.4801017,25.9532535,46.5394298,58.6864903,84.6933612,96.2814068,131.118007]
        }

# 转换为DataFrame格式
df = pd.DataFrame(data)

# 绘制统计图
sns.barplot(x='Regulatory Relationship', y='Average Latency(s)', data=df, palette='BuGn_d')

# 在每个柱子里添加斜线
for index, row in df.iterrows():
    plt.bar(index, row['Average Latency(s)'], color='white', edgecolor='black')
    plt.plot([index-0.2, index+0.2], [row['Average Latency(s)']*0.95, row['Average Latency(s)']*0.95], color='black', linewidth=1)

# 设置标题和轴标签
plt.title('Average Latency for Different Regulatory Relationships')
plt.xlabel('Regulatory Relationship')
plt.ylabel('Average Latency (s)')
# 修改刻度线朝向
plt.tick_params(axis='both', direction='in')

# save the chart as a high-quality PNG file
plt.savefig('Average_Latecy.png', dpi=300)
# 显示图形
plt.show()
