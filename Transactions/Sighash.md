# SigHash
Signature hash (SigHash) in bitcoin protocol is a construct that determines which parts of the transaction are signed and hence protected from being modified. 
There are four types of SigHash in bitcoin that can be used, individual or in combination, to sign a transaction. The flags are :
1. SigHash_ALL
2. SigHash_NONE
3. SigHash_SINGLE
4. SigHash_ANYONECANPAY

#### SigHash_ALL
- It is bitcoin's default SigHash type
- It commits all components of a transaction to the signature
- Thus no parts of the transaction can be changed once it is signed. 