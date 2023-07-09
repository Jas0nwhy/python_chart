import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 设置数据
data = pd.DataFrame({
    'Malicious Oracle Node Ratio': [10, 20, 30, 40],
    'RSA Weighted Threshold Signature': [1.0, 0.97, 0.93, 0.86],
    'BLS Threshold Signature': [1.0, 1.0, 0.96, 0.92]
})

# 绘制图表
# 修改点线的宽度和颜色
sns.set_palette("Paired")
sns.set_context("paper", font_scale=1.2)
sns.set_style("ticks")
plt.figure(figsize=(8, 6))
sns.pointplot(data=data, x='Malicious Oracle Node Ratio', y='RSA Weighted Threshold Signature',
              capsize=0.2, errwidth=1.2, linewidth=0.6, label="RSA Weighted Threshold Signature")
sns.pointplot(data=data, x='Malicious Oracle Node Ratio', y='BLS Threshold Signature',
              capsize=0.2, errwidth=1.2, linewidth=0.6, label="BLS Threshold Signature")
plt.title("Success Rate of Cross-Chain Data Authenticity Verification\nwith Different Malicious Oracle Node Ratio")
plt.xlabel("Malicious Oracle Node Ratio (%)")
plt.ylabel("Success Rate")
plt.legend(title="Signature Method")
plt.ylim(0.8, 1.005)
plt.tight_layout()
# 设置图像质量
plt.savefig("plot4.png", dpi=300, bbox_inches='tight')
plt.show()

