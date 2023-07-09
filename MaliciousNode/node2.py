# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 设置颜色
# sns.set_palette('Paired')
# sns.set_style("ticks")
#
# data = {'Malicious Oracle Node Proportion(%)': ['10', '20', '30', '40']*2,
#         'Type': ['BLS Scheme']*4 + ['RSA Weighted Scheme']*4,
#         'Success Rate(%)': [100, 97, 93, 86,
#                             100, 100, 97, 96]
#         }
#
# # 转换为DataFrame格式
# df = pd.DataFrame(data)
#
# # 设置字体大小
# plt.rc('font', size=16)
# # 绘制统计图
# sns.barplot(x='Malicious Oracle Node Proportion(%)', y='Success Rate(%)', hue='Type', data=df, dodge=0.7, linewidth=0.4, palette = "Greens")
#
# # 设置标题和轴标签
# # plt.title('Success Rate of Cross-Chain Data Authenticity Verification\nwith Different Malicious Oracle Node Proportions')
# plt.xlabel('Malicious Oracle Node Proportion(%)')
# plt.ylabel('Success Rate(%)')
# plt.ylim(85, 101)
# # 修改刻度线朝向
# plt.tick_params(axis='both', direction='in')
#
# # 修改标签框中的字体大小
# # plt.legend(title="Type", bbox_to_anchor=(0.5, 0.99), loc=2, borderaxespad=0., prop={'size': 12})
# plt.legend(bbox_to_anchor=(0.5, 0.99), loc=2, borderaxespad=0., prop={'size': 12})
#
# # save the chart as a high-quality PNG file
# plt.savefig('node_notitle.png', dpi=300)
#
# # 显示图形
# plt.show()
#
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置颜色
sns.set_palette('Paired')
sns.set_style("ticks")

data = {'Malicious Oracle Node Proportion(%)': ['10', '20', '30', '40']*2,
        'Type': ['BLS Scheme']*4 + ['RSA Weighted Scheme']*4,
        'Success Rate(%)': [100, 97, 93, 86,
                            100, 100, 97, 96]
        }

# 转换为DataFrame格式
df = pd.DataFrame(data)

# 设置字体大小
plt.rc('font', size=16)

# 设置不同类型的柱形图纹路
hatches = ['//', '//', '//', '//', '\\\\', '\\\\', '\\\\', '\\\\']

# 绘制统计图，设置dodge参数来区分不同type的柱形图
bar = sns.barplot(x='Malicious Oracle Node Proportion(%)', y='Success Rate(%)', hue='Type', data=df, dodge=0.7, linewidth=0.4, palette = "Greens", edgecolor='black')

# Loop over the bars
for i,thisbar in enumerate(bar.patches):
    # Set a different hatch for each bar
    thisbar.set_hatch(hatches[i])

# 设置标题和轴标签
plt.xlabel('Malicious Oracle Node Proportion(%)')
plt.ylabel('Success Rate(%)')
plt.ylim(85, 101)

# 修改刻度线朝向
plt.tick_params(axis='both', direction='in')

# 修改标签框中的字体大小
plt.legend(bbox_to_anchor=(0.5, 0.99), loc=2, borderaxespad=0., prop={'size': 12})

# save the chart as a high-quality PNG file
plt.savefig('node_notitle.png', dpi=300)

# 显示图形
plt.show()

