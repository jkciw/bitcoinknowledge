A set of rules that bitcoin nodes agree upon and enforce when considering the validity of a block and its transactions [^1].  
- Policy rules are a super set of consensus rules [^2]. Policy rules exist to 
	- close DOS vectors
	- make future consensus changes safer to deploy
- Rules regarding the functioning of the network are not consensus rules [^1].
- New consensus can be implemented using a soft fork, while removing consensus can only be accomplished by hard-forking the chain. 
- The rules can be understood by reading the `code` implemented by the `bitcoin core` implementation. 
- The consensus rules can be found inside `bitcoin/src/consensus/`
- The policy rules can be found inside `bitcoin/src/policy/`
- However, there are many policy and consensus checks that happen outside these two directories. 
- `CheckTransaction()` found in `bitcoin/src/consensus/tx_check.cpp` contains the following consensus rules. 
	1. Inputs and Outputs of a transaction shouldn't be empty
	2. The total size of all the transactions in the block, excluding witness data, should be less than 4 MB
		`bitcoin/src/consensus/consensus.h`
		1. The maximum allowed size of a serialized block is 4 MB - 
	4. The value of each output used in all the transaction, to be included in a block/included in a block, should be $0 < value_{output} < 21$ $million$ $BTC$
		`bitcoin/src/consensus/amount.h`
		1. The amount of satoshi's in one BTC is $10^{8}$ (i.e) 100 Million
		2. The maximum amount of satoshi's that can be created is $21 \cdot 10^{14}$ 
	4. The sum of outputs in a transaction should be $0\leqq \sum{value_{output}} \leqq 21$ $million$ $BTC$ 
	5. The inputs of a transaction should not contain any duplicates
	6. The inputs of a non-coinbase transaction should not be Null
	7. If the transaction is a coinbase transaction, the ScriptSig size should be between $2< size_{ScriptSig}<100$  
- `CheckTxInputs()` found in `bitcoin/src/consensus/tx_verify.cpp` contains the following consensus rules
	1. All the inputs in a transaction should be available for spending
	2.  The sum of inputs in a transaction should be $0\leqq \sum{value_{input}} \leqq 21$ $million$ $BTC$ 
	3. The sum of inputs in a transaction should be greater than or equal to the sum of outputs in a transaction $\sum{value_{input}} \geqq \sum{value_{output}}$ 
	4. The transaction fee $tx_{fee}=\sum{value_{input}} -\sum{value_{output}}$  should be $0\leqq tx_{fee} \leqq 21$ $million$ $BTC$ 
- `ConnectBlock()` found in `bitcoin/src/validation.cpp` contains the following consensus rules
	1. The accumulated fees in a block should be $0\leqq block_{fee} \leqq 21$ $million$ $BTC$ 
	2. The block should not contain a non-BIP-168 (RelativeTimeLock) final transaction
	3. The maximum no.of signature check operations (legacy, p2sh, segwit) in a block should not exceed 8000
	4. The scripts of all the transactions in the block should be valid. 
	5. The block subsidy should be less than or equal to the block reward(fees + subsidy) $block_{subsidy} \leqq (tx_{fees} + block_{subsidy} )$ 
		`GetBlockSubsidy()` in `bitcoin/src/validation.cpp`
		1. $block_{subsidy} = 0$ when no.of Halvings $\geqq$ 64
		2. The initial $block_{subsidy} = 50$ $BTC$ 
		3. The $block_{subsidy}$ is cut in half for every halving
		4. halving = $\frac {block_{height}}{210000 blocks}$
- `CheckBlock()` found in `bitcoin/src/validation.cpp` contains the following consensus rules
	1. Block should not be empty
	2. The block's weight, excluding witness data, should not exceed 4 MB
	3. The block's first transaction must be a coinbase transaction
	4. A block should not contain more than one coinbase transaction 
- `ContextualCheckBlock()`found in `bitcoin/src/validation.cpp` contains the following consensus rules
	1. All the transactions in the block must be ***final***
		`IsFinalTx()` in `bitcoin/src/consensus/tx_verify.cpp`
			A $tx$ is final if 
			1. $nLockTime = 0$ (or)
			2.  $nLockTime \lt blockheight_{threshold} || blocktime_{threshold}$ (or)
			3. $nSequence = ffffffff$ , irrespective of the above two conditions
	2. The first item of the ScriptSig of a coinbase transaction in a block must be the block's height. 
![](images/Pasted%20image%2020240705125857.png)
			The `CheckTransaction()` function of bitcoin core
# References

[^1]: https://en.bitcoin.it/wiki/Consensus
[^2]: https://bitcoin.stackexchange.com/questions/100317/what-is-the-difference-between-policy-and-consensus-when-it-comes-to-a-bitcoin-c
