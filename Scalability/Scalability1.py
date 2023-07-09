import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 定义数据
data = {
    'Regulatory relationship': ['1-1', '1-2', '2-1', '2-2', '3-2', '2-3', '3-3'],
    'Average delay(ms)': [500, 800, 550, 900, 1100, 1300, 1500],
}

# 转化为dataframe
df = pd.DataFrame(data)

# 设置画布大小和背景风格
plt.figure(figsize=(8, 6))
sns.set_style('ticks')

# 绘制点线图
sns.pointplot(x='Regulatory relationship', y='Average delay(ms)', data=df, markers=['o'], linestyles=['-'])

# 设置坐标轴标签
plt.xlabel('Regulatory relationship', fontsize=12)
plt.ylabel('Average delay(ms)', fontsize=12)

# 设置坐标轴刻度线朝向坐标轴内部
plt.tick_params(axis='both', which='both', direction='in')

# 显示图像
plt.show()
