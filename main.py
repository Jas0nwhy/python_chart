import matplotlib.pyplot as plt

# Experiment 1: Off-chain Consensus Efficiency

# Generate simulated data
num_nodes = [3, 4, 5, 6, 7, 8]
events_per_sec = [100, 200, 300, 400, 500, 600]
tx_throughput = [75, 150, 225, 300, 375, 450]

# Plot data
plt.plot(num_nodes, tx_throughput)
plt.xlabel('Number of Nodes')
plt.ylabel('Transaction Throughput (tx/s)')
plt.title('Off-chain Consensus Efficiency')
plt.savefig('experiment1.png')
plt.show()
