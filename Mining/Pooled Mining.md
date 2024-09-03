# The probabilities of pooled mining

The process of several miners working together to find a block and splitting the reward (coinbase + transaction fee) in proportion to the hash they contributed is called pooled mining. 
Let the pool's total hash rate be $H$. Then, 
```math
P(\text{finding a block}) = \frac{1}{2^{32}D} 
D - \text{difficulty}
```