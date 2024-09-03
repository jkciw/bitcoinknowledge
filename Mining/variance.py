import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Constants
TIME = 24 * 3600  # 24 hours in seconds
DIFFICULTY = 86.87 * 10**12
POOL_HASHRATE = 228 * 10**18  # hashes per second
SOLO_HASHRATE = 1100 * 10**12  # hashes per second
BLOCK_REWARD = 3.125  # BTC

def calculate_lambda(hashrate, difficulty, time):
    return (hashrate * time) / (2**32 * difficulty)

def calculate_variance(lambda_param, block_reward):
    return lambda_param * (block_reward**2)

# Calculate lambda for pool and solo miner
lambda_pool = calculate_lambda(POOL_HASHRATE, DIFFICULTY, TIME)
lambda_solo = calculate_lambda(SOLO_HASHRATE, DIFFICULTY, TIME)

# Calculate variances
variance_pool_total = calculate_variance(lambda_pool, BLOCK_REWARD)
variance_solo = calculate_variance(lambda_solo, BLOCK_REWARD)

# Calculate individual miner's share in the pool
individual_share = SOLO_HASHRATE / POOL_HASHRATE
variance_pool_individual = (individual_share**2) * variance_pool_total

print(f"Pool's Total Variance: {variance_pool_total:.8f} BTC²")
print(f"Pool Miner (Individual) Variance: {variance_pool_individual:.8f} BTC²")
print(f"Solo Miner Variance: {variance_solo:.8f} BTC²")
print(f"Variance Reduction Factor: {variance_solo / variance_pool_individual:.2f}")


# Plotting
labels = ['Pool (Total)', 'Individual in Pool', 'Solo Miner']
variances = [variance_pool_total, variance_pool_individual, variance_solo]
colors = ['#1f77b4', '#2ca02c', '#d62728']  # Blue, Green, Red

# Set the style
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(12, 6))

# Create horizontal bar plot
bars = ax.barh(labels, variances, color=colors, alpha=0.8)

# Customize the plot
ax.set_xlabel('Variance (BTC²)', fontsize=12)
ax.set_title('Comparison of Mining Variances (24-hour period)', fontsize=16)
ax.set_xscale('log')

# Add value labels to the end of each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2, f'{width:.2e}', 
            ha='left', va='center', fontweight='bold', fontsize=10)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a text box with additional information
textstr = f'Variance Reduction Factor:\nSolo vs Pool (Individual) = {variance_solo / variance_pool_individual:.2f}'
props = dict(boxstyle='round', facecolor='white', edgecolor='gray', alpha=0.8)
ax.text(0.05, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)

plt.tight_layout()
plt.show()