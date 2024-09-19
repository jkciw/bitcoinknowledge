#### Definition 
- If contracts, in bitcoin scripts are complex enough, miners can analyze which contract executions are profitable for the miner and can order transactions such that the contract that gets executed first is the most profitable for the miner. 
- MEV is front running some transactions based on mempool activity for profits. Profit could be achieved by order or include/exclude some transactions in block. 
- Normally such opportunities are  found in complex smart contracts that allow trades being settled on-chain. 
#### In what form MEVs can be realized in Bitcoin ?
- By mining pools assembling a very competent team to analyze voluminous `spending conditions` published in the merkele trees of transactions and figuring out which one would be the most profitable to mine.
- Automated Market Maker (AMMs), if realized using covenants, will create deposit and withdrawal transactions. Miners can front run such transactions. 
#### Why MEV is difficult to realize in Bitcoin ?
- Key value store in Ethereum doesn't exist in Bitcoin. Data can't be stored on chain and retrieved by the script during execution, in Bitcoin. 
- Ethereum operates based on an ***account model*** . 
	- In an account model, every address has a balance associated with it. Transactions deduct units from the account(or) address. 
- Bitcoin operates based on an ***UTXO model*** . 
	- UTXOs are indivisible entities. A UTXO is consumed on the whole when a transaction uses that UTXO.
- Example: Consider an address with 10 units in it. Assume that it is a 2 of 10 multisig. There are 45 possible valid spending conditions.
	- Consider 11 transactions that try to spend 1 unit from that address.
		- Because of the account based model, each 1 ETH transaction only ***deducts*** from the address. The address remains static. If 11 such deductions arrive at the mempool, the miner can:
			- order the 11 such that he can extract the maximum fees. 
			- because the miner can order transactions, he also has the power to decide which 1 transaction out of the 11 transaction becomes invalid as there are only 10 ETHs in the address. 
		- Because of the UTXO based model, each 1 BTC transaction consumes the whole UTXO. If 11 transactions arrive at the mempool with the UTXO holding 10 BTC as input, the miner can only choose one of the 11 transactions that offers him the most fee. All other transactions becomes invalid once the first transaction is mined as the parent UTXO is consumed. The remaining 9 BTC will become a new UTXO, using the same address or different address
	 