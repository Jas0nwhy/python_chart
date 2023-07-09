import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data from the table
rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
high_trust_1 = [0.2, 0.4, 0.6, 0.7, 0.8, 0.9, 0.85, 0.88, 0.86, 0.85, 0.83, 0.75]
high_trust_2 = [0.2, 0.6, 0.8, 0.9, 0.85, 0.88, 0.87, 0.9, 0.87, 0.85, 0.82, 0.88]
mid_trust_1 = [0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.58, 0.6, 0.63, 0.64, 0.62, 0.6]
low_trust_1 = [0.2, 0.15, 0.12, 0.1, 0.08, 0.06, 0.13, 0.12, 0.1, 0.18, 0.17, 0.15]
low_trust_2 = [0.2, 0.25, 0.22, 0.2, 0.18, 0.16, 0.12, 0.16, 0.14, 0.19, 0.13, 0.13]

# 设置字体大小
plt.rc('font', size=16)

# create a pandas dataframe with the data
data = {"Rounds": rounds,
        "High Trust 1": high_trust_1,
        "High Trust 2": high_trust_2,
        "Mid Trust 1": mid_trust_1,
        "Low Trust 1": low_trust_1,
        "Low Trust 2": low_trust_2}
df = pd.DataFrame(data)

# set style and plot the data
sns.set_palette("Paired")
#sns.set_context("paper", font_scale=1.2)
sns.set_style("ticks")
sns.lineplot(data=df, x="Rounds", y="High Trust 1", marker='o', markersize=10, linestyle='-',label='High Trust 1', )
sns.lineplot(data=df, x="Rounds", y="High Trust 2", marker='s', markersize=10, linestyle='--',label='High Trust 2')
sns.lineplot(data=df, x="Rounds", y="Mid Trust 1", marker='v', markersize=10, linestyle=':',label='Mid Trust 1')
sns.lineplot(data=df, x="Rounds", y="Low Trust 1", marker='^', markersize=10, linestyle='-.',label='Low Trust 1')
sns.lineplot(data=df, x="Rounds", y="Low Trust 2", marker='p', markersize=10, linestyle='--',label='Low Trust 2')

# add legend, title and axis labels
plt.legend(bbox_to_anchor=(0.65, 0.55), loc=2, borderaxespad=0., prop={'size': 12})

plt.xlabel("Rounds")
plt.ylabel("Global Trust Score")
# get the current axis objectlabel

ax = plt.gca()
ax.set_xlim(0,13)

ax.tick_params(direction="in")
# plt.title("Global Trust Scores of Oracle Nodes")

# save the chart as a high-quality PNG file
plt.savefig('oracle_trust_scores_notitle.png', dpi=300)
plt.show()