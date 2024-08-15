### Target and Difficulty
***Difficulty adjustment*** is the process of adjusting the difficulty of the network to ensure blocks are created every 10 minutes. The definition of ***target*** and ***difficulty*** and how they are calculated is shown below, using the genesis block and block #501509. 

![](images/difficulty_adjustment%201.jpg)

- The maximum target is a large 256 bit number. 
 
$$
\begin{align*}
&\text{target}_{max} = 0X00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\\
\end{align*}
$$

- Once every 2016 blocks, the protocol assesses the block production time with respect to the target/difficulty. 
- New Target is calculated as follows 

$$Target_{new} = Target_{old}*\frac{20160}{timestamp_{block_{2015}}-{timestamp_{block_{0}}}}$$
- Difficulty is adjusted as follows[^1] 

$$Difficulty_{new} = Difficulty_{old}*\frac{timestamp_{block_{2015}}-{timestamp_{block_{0}}}}{20160}$$


It is to be noted that only `Target` is re-calculated every 2016 blocks and shared between nodes via the `nBits` field in the block header. `Difficulty` exists to facilitate easier understanding of the `Target` value [^2]. 
# References
[^1]: https://bitcoin.stackexchange.com/questions/67425/why-does-bitcoin-adjust-the-difficulty-every-2016-instead-of-2048-blocks?rq=1
[^2]: https://bitcoin.stackexchange.com/questions/50872/is-the-target-the-source-of-the-difficulty