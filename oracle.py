import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
df = pd.read_csv('experiment_results.csv')

# 绘制预言机工作组数据真实性验证的成功率折线图
sns.lineplot(data=df, x='Data Size (MB)', y='Success Rate', hue='Nodes', style='Nodes')
plt.title('Success Rate of Cross-Chain Data Validation by Oracle Workgroup')
plt.xlabel('Data Size (MB)')
plt.ylabel('Success Rate')
plt.ylim(0.6, 1)
plt.show()

# 绘制每秒验证成功的交易吞吐量折线图
sns.lineplot(data=df, x='Data Size (MB)', y='Throughput (tx/s)', hue='Nodes', style='Nodes')
plt.title('Throughput of Cross-Chain Data Validation by Oracle Workgroup')
plt.xlabel('Data Size (MB)')
plt.ylabel('Throughput (tx/s)')
plt.show()
