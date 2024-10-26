Transaction introspection can be defined as the ability of bitcoin script interpreter to examine and analyze the contents, structure and properties of the transaction that it is processing. This capability allows the interpreter to make decisions (or) perform actions based on the internal details of the transaction. 

#### Bitcoin's limited transaction introspection
In bitcoin, transaction introspection happens during signing and verification of transaction. It happens in the following contexts
1. Sighash type: 
	- During signing, the signer can choose 