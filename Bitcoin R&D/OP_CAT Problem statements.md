#### Probable problem statements for research with respect to OP_CAT
1. Is the 520 bytes the right limit ? The memory weight of the entire stack should be computed before and after every operation and should be reasonably bounded[^1]
2. Can covenants leverage linearity of Schnorr Signatures to avoid or discourage MEV ?, Use the idea of Adaptor signature that the miner isn't privy to [^2] 
3. How to restrict revealing the contract details by the parties involved ? The lesser the details are revealed, the lesser the chances of miner taking advantage of them ?[^3] 
4. How to enable recursive covenants efficiently ? Just using OP_CAT to realize recursive covenants will occupy more data. 
5. How to make all transactions in a block simultaneous ? If this is possible, then ordering transactions inside a block doesn't make sense and hence MEV[^4]
6. Using coinpools/joinpools to solve miner payouts by p2p pools[^5] [^6] [^7]
# References

[^1]: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-January/013434.html
[^2]: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2022-May/020502.html
[^3]: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2022-May/020504.html
[^4]: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2022-May/020505.html
[^5]: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2023-May/021719.html
[^6]: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-August/014893.html
[^7]: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2020-June/017975.html