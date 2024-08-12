### Understanding the probability of mining a block[^1]
Bitcoin mining is the process of repeatedly computing hashes (double SHA256) of the block header, slightly modified each time, until a hash less than the [[Block - Time Stamps#Difficulty Adjustment Algorithm|target ]] is found. Weather a computed hash leads to a block being mined is a ***random event***, independent of the validity of any other calculated hashes.  <br>
$$
\begin{align}
&P(\text{finding a block})= \frac{\text{target}_{\text{current}}}{2^{256}} \tag{1}\\
\\
&\text{target}_{current} = \frac{\text{target}_{maximum}}{D} \tag{2}\\
&\text{where D - difficulty}\\
\\
&\text{substitutitng (2) in (1)}\\
\\
&P(\text{finding a block}) = \frac{\text{target}_{maximum}}{2^{256}\times D} \tag{3}\\
&\text{where target}_{maximum} = 2^{224}\\
\\
&\therefore P(\text{finding a block}) = \frac{1}{2^{32}\times D} \tag{4}\\
\\
&\text{for a time} \hspace{2mm} t \hspace{2mm} \& \hspace{2mm} \text{hash rate} \hspace{2mm} h\\
&\text{No. of Blocks Found} = \frac{ht}{2^{32}\times D} \tag{5}\\
\end{align}
$$

From the above equations, it can be derived that  miner with hash rate $h$ and mining for a time period $t$ will find $\frac{ht}{2^{32}\times D}$ blocks. 

### Poisson Process
Poisson process is a stochastic process that models the occurrence of random events over time. These events occur continuously and independent of each other. By definition, a poisson process has the following properties. A table illustrating how and why the process of *mining a block* can be understood and analyzed as poisson process is shown below:<br>
Event - Finding a $\text{hash}<\text{target}$ <br>

| <center>S.No</center> | <center>Poisson property</center>                        | <center>Mining</center>                                                                                                                                                      |
| --------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.                    | Event occurs independently of each other                 | The event of finding a $\text{hash} < \text{target}$ (a.k.a) finding a block happens independently, (i.e) the previous hash (or) future hash doesn't impact the current hash |
| 2.                    | The average rate of the event remains constant over time | As shown in (5) above, on an average $\frac{ht}{2^{32}\times D}$ blocks are found in a given time intreval                                                                   |
| 3.                    | Two events cannot occur at exactly the same instant      | A miner cannot find two hashes < target at the same time.                                                                                                                    |
<br>
The probability mass function (PMF) is given by 
$$
\begin{align}
&P(X=K) =\frac{e^{-\lambda t}\times(\lambda t)^K}{K!}\tag{6}\\
\\
&P(K) -\text{Probability of K blocks being found in the time intreval} \;t\\
&K - \text{No.of blocks found}\\
&\text{rate parameter}(\lambda) - \frac{h}{2^{32}\times D}\tag{7}
\end{align}
$$
<br>
For a poisson process, $\text{mean} = \lambda t$  , also $\text{mean}=\text{variance}$. Hence the variance of blocks found by a miner in time $t$ can be expressed as 
$$ \lambda = \frac{ht}{2^{32}\times D} \tag{8}$$ <br>
If the mining reward is assumed to be $B$ BTC per block, the expected reward can be expressed as <br>$$ \lambda \times B = \frac{htB}{2^{32}\times D} \tag{9}$$<br> the variance in the mining reward received by the miner can be expressed as <br>$$ \lambda \times B^2 = \frac{htB^2}{2^{32}\times D} \tag{10}$$<br>The standard deviation, a measure of the amount of variation a *random variable* $X$ has about its mean, of the mining reward can be expressed, from (10) as <br>$$\sigma = \sqrt{\lambda B^2} \tag{11}$$
<br> The probability that a miner, mining with a constant hash rate of $h$, will ever receive a payment during the time period $t$ can be expressed as <br>$$P(\text{receiving reward})=1-e^{-\lambda} \tag{12}$$<br>
Understanding the above equations using an example would be helpful. Consider a miner with a constant hash rate of 333 PHs, difficulty of 40.64G, block reward of 25 BTC, for 24 hrs. The Probability mass function (PMF) plot is shown below<br>
![](images/pmf_24hrs.png)<br>
As can be seen from the plot, the miner has ~ 3% chance of finding 165 no of blocks in 24 hrs. The same miner has  ~35% chance of finding 1 block in 10 minutes. The PMF plot is shown below. <br>
![](images/pmf_10_min.png)
<br>
The variance in the expected BTC reward calculated using (10) for 24 hr period is 103020 BTC. The standard deviation of the expected reward is 320.97 BTC. As can be seen, the miner suffers from quite a large block reward deviation. 
# References

[^1]: Rosenfeld, Meni. “Analysis of Bitcoin Pooled Mining Reward Systems.” _ArXiv (Cornell University)_, 1 Jan. 2011, https://doi.org/10.48550/arxiv.1112.4980.