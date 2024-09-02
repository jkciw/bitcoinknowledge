### Understanding the probability of mining a block[^1]
Bitcoin mining is the process of repeatedly computing hashes (double SHA256) of the block header, slightly modified each time, until a hash less than the [target](../Network/Target%20and%20Difficulty.md) is found. Weather a computed hash leads to a block being mined is a ***random event***, independent of the validity of any other calculated hashes.

![](images/miningprob_eq1.png)


From the above equations, it can be derived that  miner with hash rate $h$ and mining for a time period $t$ will find $\frac{ht}{2^{32}\times D}$ blocks. 

### Poisson Process
Poisson process is a stochastic process that models the occurrence of random events over time. These events occur continuously and independent of each other. By definition, a poisson process has the properties listed below. An authoritative resource to understand the poisson process in detail would be the text book written by Papoulis[^2]. A table illustrating how and why the process of *mining a block* can be understood and analyzed as poisson process is shown below[^3]:

Event - Finding a $\text{hash}<\text{target}$


| <center>S.No</center> | <center>Poisson property</center>                        | <center>Mining</center>                                                                                                                                                      |
| --------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.                    | Event occurs independently of each other                 | The event of finding a $\text{hash} < \text{target}$ (a.k.a) finding a block happens independently, (i.e) the previous hash (or) future hash doesn't impact the current hash |
| 2.                    | The average rate of the event remains constant over time | As shown in (5) above, on an average $\frac{ht}{2^{32}\times D}$ blocks are found in a given time intreval                                                                   |
| 3.                    | Two events cannot occur at exactly the same instant      | A miner cannot find two hashes < target at the same time.                                                                                                                    |

The probability mass function (PMF) is given by

![](images/miningprob_eq2.png)

For a poisson process, $\text{mean} = \lambda t$  , also $\text{mean}=\text{variance}$. Hence the variance of blocks found by a miner in time $t$ can be expressed as

![](images/miningprob_eq3.png)

If the mining reward is assumed to be $B$ BTC per block, the expected reward can be expressed as

![](images/miningprob_eq4.png)

the variance in the mining reward, a measure of how dispersed the possible mining reward could be around the expected reward (9), can be expressed as 


![](images/miningprob_eq5.png)

The standard deviation, a measure of the amount of variation a *random variable* $X$ has about its mean, of the mining reward can be expressed, from (10) as


  ![](images/miningprob_eq6.png)
 
 The probability that a miner, mining with a constant hash rate of $h$, will ever receive a payment during the time period $t$ can be expressed as
 

 ![](images/miningprob_eq7.png)
 
 Understanding the above equations using examples would be helpful. 
#### Example 1 
Consider a miner with a constant hash rate of 333 PHs, difficulty of 40.64G, block reward of 25 BTC, for 24 hrs. The Probability mass function (PMF) plot is shown below
 
![](images/pmf_24hrs.png)

As can be seen from the plot, the miner has ~ 3% chance of finding 165 no of blocks in 24 hrs. As another example, if we consider the same miner mining for only 10 minutes, he has  ~35% chance of finding 1 block in 10 minutes. The PMF plot for this case is shown below. 

![](images/pmf_10_min.png)

The variance in the expected BTC reward calculated using (10) for 24 hr period is 2575517.12 $BTC^2$. The standard deviation of the expected reward is 1604.84 BTC. As can be seen, the miner suffers from quite a large block reward deviation. 

It is to be noted that the hash values used in the above calculations are quite high for a solo miner and are used for illustrative purposes only. 

#### Example 2
A realistic hash rate and difficulty would be 180 GH/s & 1.18G respectively. These values are typical of a Antminer S1 ASIC and difficulty during early 2014. On repeating the above calculation for these values, only 0.00306862 blocks are likely to be found in 24hrs (i.e) there is close to a 100% chance of not finding a block in 24 hrs. In fact, it would likely take ~326 days $(\frac{24}{0.00306862})$  to find a block with the hash rate, provided the difficulty remains the same. The expected reward, given the probability of finding a block in the 24hr window is 0.0767 BTC. The variance in the reward would be 47.95 $BTC^2$. The standard deviation of the reward that the miner can expect, calculated using (11) for this case is 6.92 BTC. This standard deviation when expressed as a percentage of the expected reward $\frac{\sqrt(\lambda \times B^2)}{\lambda}\times 100 \%$ equals to $9026.05\%$ . A solo miner faces large variance and deviations in the expected rewards. Such are the odds of solo mining. 

The PMF plot for the above mentioned hash rate, difficulty and time period is shown below. As explained, the probability of finding a block with this hash rate, in 24 hrs, is close to zero. 


![](images/pmf_24hrs_lowhash.png)


#### Example 3
Let us consider another example of a solo miner, owning 100 Antminer S19 Pro, capable of 110 Th/s individually. The difficulty, as on August 2024, is 86.87T and the block subsidy is 3.125 BTC. If the miner, with 100 S19 Pros, mine for 24 hrs, the probability of him finding a block is close to 0. Numerically, since finding a fraction of a block doesn't make sense for a solo miner, he is likely to only find 0.00255 block. For this effort, he can expect a reward of 0.0249 BTC. The standard deviation as a percentage of the expected reward is 1981.35%. The probability that the miner will ever receive a reward in the 24 hrs time period is 0.0025. 

The code to plot the PMF can be found [here](../Mining/pmf.py)
# Credits
I would like to thank [Faizal](https://twitter.com/faisal_qrs) for helping with the calculations. 
# References

[^1]: Rosenfeld, Meni. “Analysis of Bitcoin Pooled Mining Reward Systems.” _ArXiv (Cornell University)_, 1 Jan. 2011, https://doi.org/10.48550/arxiv.1112.4980.\
[^2]: Papoulis, A. and Pillai, S.U. (2014) _Probability, random variables, and stochastic processes Athanasios Papoulis ; S. Unnikrishna Pillai_. Boston, Mass: McGraw-Hill.
[^3]: https://bitcoin.stackexchange.com/questions/43440/why-is-poisson-instead-of-negative-binomial-used-for-computing-attackers-potent


