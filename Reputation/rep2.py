import matplotlib.pyplot as plt

# data from the table
rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
high_trust_1 = [0.2, 0.4, 0.6, 0.7, 0.8, 0.9, 0.85, 0.88, 0.86, 0.85, 0.83, 0.75]
high_trust_2 = [0.2, 0.6, 0.8, 0.9, 0.85, 0.88, 0.87, 0.9, 0.87, 0.85, 0.82, 0.88]
mid_trust_1 = [0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.58, 0.6, 0.63, 0.64, 0.62, 0.6]
low_trust_1 = [0.2, 0.15, 0.12, 0.1, 0.08, 0.06, 0.13, 0.12, 0.1, 0.18, 0.17, 0.15]
low_trust_2 = [0.2, 0.25, 0.22, 0.2, 0.18, 0.16, 0.23, 0.22, 0.2, 0.28, 0.27, 0.3]

# plot the data
fig, ax = plt.subplots(figsize=(10, 5))
# colors = ['#b0c4de', '#f08080', '#90ee90', '#ffa07a', '#afeeee']
ax.plot(rounds, high_trust_1, marker='o', linestyle='-', label='High Trust 1')
ax.plot(rounds, high_trust_2, marker='s', linestyle='--', label='High Trust 2')
ax.plot(rounds, mid_trust_1, marker='v', linestyle=':', label='Mid Trust 1')
ax.plot(rounds, low_trust_1, marker='^', linestyle='-.', label='Low Trust 1')
ax.plot(rounds, low_trust_2, marker='p', linestyle='--', label='Low Trust 2')

# add legend, title and axis labels
ax.legend()
ax.set_xlabel('Rounds')
ax.set_ylabel('Global Trust Score')
# ax.set_title('Global Trust Scores of Oracle Nodes')
plt.show()
# save the chart as a high-quality PNG file
plt.savefig('oracle_trust_scores.png', dpi=300)
