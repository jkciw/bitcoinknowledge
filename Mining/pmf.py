import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# To calculate the probability mass function(PMF) for the event of finding/mining a block

BLOCK_REWARD = 3.125
DIFFICULTY = 86.87 * 10**12
HASH_RATE = 10*110 * 10**12
TIME = 24*3600

def calculate_lambda(diff, hash_rate, time):
    target = (2**224) / diff
    prob_success = target / (2**256)
    return hash_rate * prob_success * time

def calculate_miner_stats(lambda_param, block_reward):
    expected_reward = lambda_param * block_reward
    variance_reward = expected_reward*block_reward
    sd_reward = np.sqrt(variance_reward)
    sd_percent = (sd_reward/expected_reward)*100
    probability_reward = 1-np.exp(-lambda_param)
    return expected_reward, variance_reward, sd_reward, sd_percent, probability_reward

def get_pmf(lambda_param):
    x_min = int(stats.poisson.ppf(0.001, lambda_param))
    x_max = int(stats.poisson.ppf(0.999, lambda_param))+1
    x = np.arange(x_min, x_max)
    y = stats.poisson.pmf(x, lambda_param)*100
    return x, y
def calculate_range_probabilities(lambda_param, step=5):
    x_max = int(stats.poisson.ppf(0.9999, lambda_param)) + step
    ranges = list(range(0, x_max, step))
    probabilities = []
    
    for i in range(len(ranges) - 1):
        lower = ranges[i]
        upper = ranges[i+1]
        prob = (stats.poisson.cdf(upper, lambda_param) - stats.poisson.cdf(lower, lambda_param))*100
        probabilities.append(prob)
    return ranges[:-1], probabilities
def calculate_at_least_probabilities(lambda_param, max_blocks=70):
    blocks = np.arange(1, max_blocks + 1)
    probabilities = 1 - stats.poisson.cdf(blocks - 1, lambda_param)
    return blocks, probabilities
def plot_pmf(x, y, block_reward, time, lambda_param):
    plt.figure(figsize=(12, 6))
    #plt.bar(x, y, alpha=0.8) # use bar plots for well formed poission distribution
    plt.stem(x,y, basefmt=" ") # use stem plots if only few data points are available for plotting
    plt.xlabel('No. of blocks likely to be found')
    plt.ylabel('Probability of finding the no.of blocks(%)')
    plt.title(f'PMF of Blocks Found in {time/3600} hrs')
    plt.grid(alpha=0.3)
    # Add expected value line
    expected_blocks = lambda_param
    plt.axvline(x=expected_blocks, color='r', linestyle='--', label=f'{lambda_param:.0f} no of blocks are likely to be found in {time/(24*3600)} days \n' 
    f'The expected reward is: {lambda_param*block_reward:.4f} BTC')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.2f}%"))
    plt.legend()
    #adjust axis if necessary
    #plt.xlim(100, max(x) + 0.5)
    #plt.ylim(0, max(y) * 1.1)
    plt.show()

def plot_range_probabilities(ranges, probabilities, lambda_param):
    plt.figure(figsize=(12, 6))
    plt.bar(ranges, probabilities, width=4, align='edge')
    plt.xlabel('Number of blocks')
    plt.ylabel('Probability')
    plt.title(f'Probability Distribution for Ranges of 5 Blocks (λ = {lambda_param:.2f})')
    plt.grid(True, alpha=0.3)
    
    # Add text annotations for probabilities
    for i, prob in enumerate(probabilities):
        plt.annotate(f'{prob:.1f}', (ranges[i] + 2.5, prob), 
                     textcoords="offset points", xytext=(0,5), ha='center')

    # Customize x-axis ticks
    plt.xticks(ranges, [f'{r}-{r+5}' for r in ranges])
    
    plt.tight_layout()
    plt.show()
def plot_at_least_probabilities(blocks, probabilities, lambda_param):
    plt.figure(figsize=(15, 8))
    plt.plot(blocks, probabilities, marker='o', linestyle='-', markersize=4)
    plt.xlabel('Number of Blocks')
    plt.ylabel('Probability of Finding At Least X Blocks')
    plt.title(f'Probability of Finding At Least X Blocks in 24 hours (λ = {lambda_param:.2f})')
    plt.grid(True, alpha=0.3)
    
    # Add horizontal lines at key probability levels
    for prob in [0.9, 0.5, 0.1]:
        plt.axhline(y=prob, color='r', linestyle='--', alpha=0.5)
        plt.text(blocks[-1], prob, f'{prob*100:.0f}', va='center', ha='left', color='r')

    # Customize x-axis ticks
    plt.xticks(np.arange(0, max(blocks)+1, 5))
    
    # Customize y-axis to show percentages
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))

    plt.tight_layout()
    plt.show()
def print_statistics():
    lambda_param = calculate_lambda(DIFFICULTY, HASH_RATE, TIME)
    expected_reward, variance_reward, sd_reward, sd_percent, probability_reward = calculate_miner_stats(lambda_param, BLOCK_REWARD)
    print(f"Expected number of blocks: {lambda_param:.5f}")
    print(f"Expected reward: {expected_reward:.4f} BTC")
    print(f"Variance of reward: {variance_reward:.4f} BTC")
    print(f"Standard deviation of reward: {sd_reward:.4f} BTC")
    print(f"Standard deviation as a percent of expected reward: {sd_percent:.2f} %")
    print(f"The probability that the miner will receive a reward at all: {probability_reward:.4f}")

def pmf_example():
    lambda_param = calculate_lambda(DIFFICULTY, HASH_RATE, TIME)
    expected_reward, variance_reward, sd_reward, sd_percent, probability_reward = calculate_miner_stats(lambda_param, BLOCK_REWARD)
    x, y = get_pmf(lambda_param)
    plot_pmf(x, y, expected_reward, TIME, lambda_param)

def rangeprob_examples():
    lambda_param = calculate_lambda(DIFFICULTY, HASH_RATE, TIME)
    ranges, probabilities = calculate_range_probabilities(lambda_param)
    plot_range_probabilities(ranges, probabilities, lambda_param)

def atleastprob_examples():
    lambda_param = calculate_lambda(DIFFICULTY, HASH_RATE, TIME)
    blocks, probabilities = calculate_at_least_probabilities(lambda_param, 10)
    plot_at_least_probabilities(blocks, probabilities, lambda_param)

if __name__ == '__main__':
    print_statistics()
    rangeprob_examples()
    atleastprob_examples()
    pmf_example()

