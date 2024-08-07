Difficulty adjustment is the process of adjusting the difficulty of the network to ensure blocks are created every 10 minutes. The definition of ***target*** and ***difficulty*** and how they are calculated is shown below, using the genesis block and block #501509. 

![](images/difficulty_adjustment%201.jpg)

- Once every 2016 blocks, the protocol assesses the block production time with respect to the difficulty. 
- Difficulty is adjusted as follows[^1]
$$Difficulty_{new} = Difficulty_{old}*\frac{timestamp_{block_{2015}}-{timestamp_{block_{0}}}}{20160}$$

# References
[^1]: https://bitcoin.stackexchange.com/questions/67425/why-does-bitcoin-adjust-the-difficulty-every-2016-instead-of-2048-blocks?rq=1