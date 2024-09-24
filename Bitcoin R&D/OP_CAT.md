#### What is OP_CAT ?
An opcode to concatenate two stack elements in bitcoin script. 
- BIP 420 defines the proposed OP_CAT
- Given $[X_1, X_2]$, where $X_2$ is the top element of the stack, OP_CAT consumes the two elements and pushes $[X_1 \parallel X_2]$ 
- The operation fails 
	- if there are fewer than two stack elements on the stack
	- if the size of the concatenated element's size > 520 bytes (MAX_SCRIPT_ELEMENT_SIZE)
- Proposed to be activated by redefining OP_SUCCESS126 of tapscript 

#### Potential applications
1. Bitstream protocol - an atomic swap protocol that enables swapping of decryption keys for bitcoin - Robin Linus (2023)
2. Using a combination of OP_CAT and MAST, 1-of-N multisignatures, for very large `N`, theoretically upto 4 billion keys can be constructed without much added cost when compared to traditional multisigs. - Petier Wuille (2015)
3. Using a combination of OP_CAT and Schnorr signatures, we can create M-of-M multisig setups that look like single signature setups. - Petier Wuille (2015)
4. OP_CAT can be used to realize generalize threshold trees Eg. conditions like Either A and B sign (OR) 2 out of C,D and E Sign - Pieter Wuille (2015)
5. Quantum resistant ECDSA signatures using OP_CAT and Lamport Signatures - Jeremy Rubin (2021)
6. Decentralize Non-Equivocation contracts that penalize by charging bitcoins - Aniket Kate (2015)
7. Different types of  [covenants](Covenants.md) can be realized. - (2016)
8. With a combination of OP_CAT, OP_CHECKSIGFROMSTACK and miniscript interesting covenants can be realized - Andrew Poelstra (2021)

#### Apprehensions about OP_CAT
- Will pave way to realize general [covenants](Covenants.md), which itself can bring in unknown unknowns 
- Will pave way to [MEV](Miner%20Extracted%20Value.md)  and thus centralization of mining
- Will pave way to realize recursive covenants, which leads to reduced privacy and decentralization 
- Will pave way to implement drivechains that can lead to complex and long contracts putting undue pressure on nodes. 