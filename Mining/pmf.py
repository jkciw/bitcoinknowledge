import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# To calculate the probability mass function(PMF) for the event of finding/mining a block

# Constants
BLOCK_REWARD = 3.125  # BTC
HASH_RATE = 100*110 * 10**12  # hashes per second
DIFFICULTY = 86.87 * 10**12 
TIME_PERIOD = 24*3600  # 24 hours in seconds

# Calculate lambda (average number of blocks in the time period)
target = (2**224) / DIFFICULTY
prob_success = target / (2**256)
lambda_param = HASH_RATE * prob_success * TIME_PERIOD

# Generate x-axis values (number of blocks)
x = np.arange(0, 1) # increase (or) decrease as needed


# Calculate PMF for each x, expressed as a %
y = stats.poisson.pmf(x, lambda_param)*100

# Plotting
plt.figure(figsize=(12, 6))
#plt.bar(x, y, alpha=0.8) # use bar plots for well formed poission distribution
plt.stem(x,y, basefmt=" ") # use stem plots if only few data points are available for plotting
plt.xlabel('No. of blocks likely to be found')
plt.ylabel('Probability of fining the no.of blocks')
plt.title(f'PMF of Blocks Found in {TIME_PERIOD/3600} hrs\n'
          f'(The expected Reward = {lambda_param * BLOCK_REWARD:.2f} BTC)')
plt.grid(alpha=0.3)

# Add expected value line
expected_blocks = lambda_param
plt.axvline(x=expected_blocks, color='r', linestyle='--', label=f'{lambda_param:.0f} no of blocks are likely to be found in {TIME_PERIOD/3600} hrs')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.2f}%"))

plt.legend()
#adjust axis if necessary
#plt.xlim(100, max(x) + 0.5)
#plt.ylim(0, max(y) * 1.1)

# Metrics
no_blocks = lambda_param
reward = no_blocks * BLOCK_REWARD
variance_reward = reward * BLOCK_REWARD
sd_reward = np.sqrt(variance_reward)
sd_percent = (sd_reward/reward)*100
probability_reward = 1-np.exp(-lambda_param)
plt.show()
print(f"Expected number of blocks: {no_blocks:.5f}")
print(f"Expected reward: {reward:.4f} BTC")
print(f"Variance of reward: {variance_reward:.4f} BTC")
print(f"Standard deviation of reward: {sd_reward:.4f} BTC")
print(f"Standard deviation as a percent of expected reward: {sd_percent:.2f} %")
print(f"The probability that the miner will receive a reward at all: {probability_reward:.4f}")