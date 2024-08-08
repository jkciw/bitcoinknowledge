Fork refers to an event of an independent implementation of a project spinning off from the main project
- Often occurs due to irreconcilable differences, as to which way the development has to proceed, between developers. 
	- Eg. Litecoin is a fork of bitcoin
- It can also occur if significant architectural changes have to be made in the software - ***Break of Compatibility***. 
- ***Hardfork and Softfork*** , in the context of Bitcoin, refer to the ***compatibility breaking changes*** in the bitcoin protocol. 
### Soft Fork[^1]
- Backward compatible changes to the [consensus rules](../Consensus/Consensus%20Rules.md) are called *soft fork*
- ***Backward compatibility*** means that full nodes implementing the changes ***must not*** accept any blocks that full nodes not implementing the changes ***would consider invalid*** 
  
  ![](images/Pasted%20image%2020240509165827.png) 

- If >51% of the hash power start to use the soft fork, chain split doesn't happen. 
- There is a possibility of a short term chain split happening, consisting of new vs old (consensus) blocks. However, since majority of the miners start implementing the new change, the chain tip consisting of blocks implementing new rules would emerge as the heavier chain and the split would resolve itself.  

### Hard Fork
- Backwards incompatible changes to the consensus rules are called Hard Fork
- Full nodes implementing the new changes ***will*** accept blocks that full nodes not implementing the changes  ***would consider invalid*** 
 
 ![](images/Pasted%20image%2020240509170606.png)
- To seamlessly implement a hard fork, all the participants of the network - miners, developers, nodes and users have to switch to the implementation of the new consensus rule. 
# References

[^1]: https://bitcoin.stackexchange.com/questions/30817/what-is-a-soft-fork-what-is-a-hard-fork-what-are-their-differences