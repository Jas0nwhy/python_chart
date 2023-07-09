# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 模拟数据
# data = {'Regulatory Relationship': ['1-1', '1-2', '2-1', '2-2', '2-3', '3-2', '3-3'],
#         'Average Latency(s)':
#                 # [2.221, 2.455, 3.074, 3.279, 4.216, 4.366, 5.031]
# # [11.74005085, 12.97662675, 23.2697149, 29.34324515, 42.3466806, 48.1407034, 65.55900335]
# [23.4801017,25.9532535,46.5394298,58.6864903,84.6933612,96.2814068,131.118007]
#
#         }
#
# # 设置字体大小
# plt.rc('font', size=16)
#
# # 转换为DataFrame格式
# df = pd.DataFrame(data)
#
# # 绘制统计图
# sns.barplot(x='Regulatory Relationship', y='Average Latency(s)', data=df, palette='Greens', hatch='//', edgecolor='black')
#
# # 设置标题和轴标签
# # plt.title('Average Latency for Different Regulatory Relationships')
# plt.xlabel('Regulatory Relationship')
# plt.ylabel('Average Latency (s)')
# # 修改刻度线朝向
# plt.tick_params(axis='both', direction='in')
# # save the chart as a high-quality PNG file
# plt.savefig('Average_Latecy_notitle.png', dpi=300)
# # 显示图形60
# plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 模拟数据
data = {'Regulatory Relationship': ['1-1', '1-2', '2-1', '2-2', '2-3', '3-2', '3-3'],
        'Average Latency(s)':
                # [2.221, 2.455, 3.074, 3.279, 4.216, 4.366, 5.031]
# [11.74005085, 12.97662675, 23.2697149, 29.34324515, 42.3466806, 48.1407034, 65.55900335]
[23.4801017,25.9532535,46.5394298,58.6864903,84.6933612,96.2814068,131.118007]
        }

# 设置字体大小
plt.rc('font', size=16)

# 转换为DataFrame格式
df = pd.DataFrame(data)

# 创建figure并设置大小
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制统计图
sns.barplot(x='Regulatory Relationship', y='Average Latency(s)', data=df, palette='Greens', hatch='//', edgecolor='black', ax=ax)

# 设置标题和轴标签
# plt.title('Average Latency for Different Regulatory Relationships')
ax.set_xlabel('Regulatory Relationship')
ax.set_ylabel('Average Latency (s)')

# 调整轴的范围
ax.set_ylim(0, 140)
ax.set_xlim(-0.5, 6.5)

# 修改刻度线朝向
ax.tick_params(axis='both', direction='in')

# save the chart as a high-quality PNG file
plt.savefig('Average_Latecy_notitle.png', dpi=300)

# 显示图形
plt.show()
