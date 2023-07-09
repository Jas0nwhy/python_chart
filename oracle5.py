import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
data = pd.read_csv('Oracle_per/experiment_result2.csv')

# 绘制Success Rate图
sns.set(style='ticks')
fig, ax = plt.subplots(figsize=(6, 4))
sns.lineplot(x='Data Size(MB)', y='Success Rate', hue='Node number', data=data, ax=ax)
sns.scatterplot(x='Data Size(MB)', y='Success Rate', hue='Node number', data=data, ax=ax)
plt.xlabel('Cross-Chain size(MB)')
plt.ylabel('Success rate')
plt.xlim(left=0)
plt.ylim(bottom=0, top=100)
plt.xticks(data['Data Size(MB)'])
plt.yticks(range(0, 101, 10))
plt.tick_params(direction='in', top=True, right=True)
plt.legend(title='Node number', loc='lower left', bbox_to_anchor=(0, 1))
plt.tight_layout()
plt.savefig('success_rate.png', dpi=300)

# 绘制吞吐量图
fig, ax = plt.subplots(figsize=(6, 4))
sns.lineplot(x='Data Size(MB)', y='Throughput(tx/s)', hue='Node number', data=data, ax=ax)
sns.scatterplot(x='Data Size(MB)', y='Throughput(tx/s)', hue='Node number', data=data, ax=ax)
plt.xlabel('Cross-Chain size(MB)')
plt.ylabel('Throughput(tx/s)')
plt.xlim(left=0)
plt.xticks(data['Data Size(MB)'])
plt.yticks(range(0, 550, 50))
plt.tick_params(direction='in', top=True, right=True)
plt.legend(title='Node number', loc='lower left', bbox_to_anchor=(0, 1))
plt.tight_layout()
plt.savefig('throughput.png', dpi=300)


