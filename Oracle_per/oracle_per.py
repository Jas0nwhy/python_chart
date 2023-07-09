import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 设置数据
data = pd.DataFrame({
    'Node Number': [3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9],
    'Cross-chain Data Size (MB)': [10, 20, 30, 60, 120] * 4,
    'Success Rate':
                    # [0.976, 0.941, 0.898, 0.802, 0.685,
                    #  0.989, 0.962, 0.917, 0.819, 0.702,
                    #  0.993, 0.973, 0.933, 0.834, 0.718,
                    #  0.996, 0.981, 0.949, 0.85, 0.741],
                    [0.976, 0.941, 0.898, 0.822, 0.705,
                     0.989, 0.962, 0.917, 0.869, 0.752,
                     0.993, 0.983, 0.933, 0.914, 0.848,
                     0.996, 0.981, 0.949, 0.935, 0.915],
    'Throughput (tx/s)':
                     # [283,134,89,44,22,
                     # 365,183,122,61,31,
                     # 445,222,148,74,37,
                     # 509,255,170,85,42,]
                    [146, 128, 63, 32, 25,
                     183, 145, 113, 110, 100,
                     222, 212, 176, 145, 142,
                     254, 235, 216, 163, 144, ]
})

# 绘制图表
# 修改点线的宽度和颜色
sns.set_palette("Paired")
sns.set_context("paper", font_scale=1.2)
sns.set_style("ticks")
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 4))
sns.pointplot(data=data, x='Cross-chain Data Size (MB)', y='Success Rate', hue='Node Number', ax=ax1,
              capsize=0.2, errwidth=1.2, linewidth=0.6)
sns.pointplot(data=data, x='Cross-chain Data Size (MB)', y='Throughput (tx/s)', hue='Node Number', ax=ax2,
              capsize=0.2, errwidth=1.2, linewidth=0.6)
ax1.set_ylim(0.6, 1.0)
ax2.set_ylim(0, 300)
ax1.set_title("Impact of oracle nodes and cross-chain data volume \n on success rate")
ax2.set_title("Impact of oracle nodes and cross-chain data volume \n on cross-chain throughput")
ax1.tick_params(direction='in', width=0.6)
ax2.tick_params(direction='in', width=0.6)
plt.tight_layout()
# 设置图像质量
plt.savefig("plot.png", dpi=300, bbox_inches='tight')
plt.show()


