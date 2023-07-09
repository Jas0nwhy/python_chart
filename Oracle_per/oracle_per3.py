import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 设置数据
data = pd.DataFrame({
    'Node Number': [3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9],
    'Cross-chain Data Size (MB)': [10, 20, 30, 60, 120] * 4,
    'Success Rate':
                    [0.976, 0.961, 0.898, 0.852, 0.842,
                     0.989, 0.958, 0.917, 0.899, 0.852,
                     0.993, 0.983, 0.933, 0.914, 0.908,
                     0.996, 0.981, 0.949, 0.935, 0.915],
    'Throughput (KB/s)':
        [1868.8, 1638.4, 806.4, 409.6, 320.0,
         2242.4, 1856.0, 1446.4, 1408.0, 1280.0,
         2941.6, 2713.6, 2252.8, 1856.0, 1820.8,
         3251.2, 3008.0, 2764.8, 2090.4, 1843.2]
})

# 绘制图表
# 修改点线的宽度和颜色
sns.set_palette("Paired")
sns.set_context("paper", font_scale=1.2)
sns.set_style("ticks")
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 4))
# sns.pointplot(data=data, x='Cross-chain Data Size (MB)', y='Success Rate', hue='Node Number', ax=ax1,
#               capsize=0.2, errwidth=1.2, linewidth=0.6)
# sns.pointplot(data=data, x='Cross-chain Data Size (MB)', y='Throughput (KB/s)', hue='Node Number', ax=ax2,
#               capsize=0.2, errwidth=1.2, linewidth=0.6)
sns.pointplot(data=data, x='Cross-chain Data Size (MB)', y='Success Rate', hue='Node Number', ax=ax1,
              capsize=0.2, errwidth=1.2)
sns.pointplot(data=data, x='Cross-chain Data Size (MB)', y='Throughput (KB/s)', hue='Node Number', ax=ax2,
              capsize=0.2, errwidth=1.2)
ax1.set_ylim(0.82, 1.00)
ax2.set_ylim(0, 3500)
ax1.set_title("Impact of oracle nodes and cross-chain data volume \n on success rate")
ax2.set_title("Impact of oracle nodes and cross-chain data volume \n on cross-chain throughput")
ax1.tick_params(direction='in', width=0.6)
ax2.tick_params(direction='in', width=0.6)
plt.tight_layout()
# 设置图像质量
plt.savefig("plot3.png", dpi=300, bbox_inches='tight')
plt.show()


