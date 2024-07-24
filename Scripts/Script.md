The straight forward cryptographic way of `locking` and `unlocking` funds or information is to lock it to a public key and unlock it using a private key. However such a simple scheme is poor w.r.t[^1] 
- privacy
- efficiency in the context of a proof of work system 
- capability to use complex spending conditions
Thus the need for an advanced authorization and authentication system. 

### Nature of Bitcoin's Script Language
Bitcoin's script is modeled after the stack-based language called Forth[^2]. The distinguishing feature of bitcoin's script language are:
1. It is Turing Incomplete
2. The processing of instructions is simple and fast[^3]
3. Analysis of scripts are fairly easy[^3]
4. The language is stateless. It doesn't maintain a memory of past executions[^4]. 
### Turing Incompleteness
Universal Turing Machines are machines (or) programming languages that can execute ***any*** program. A programming language that can take any program and execute them, irrespective of time and memory constraints, is called ***Turing Complete***. Bitcoin Script is designed to be ***Turing Incomplete*** because[^4] the program that the language executes ***must always end*** in a deterministic state. This requires the language to not use loops. 

### Constraints within which Bitcoin Script has to operate
The design choice of the script language is dictated by the decentralized and peer to peer nature of bitcoin. Constraints within which the script language operates include[^5]:
1. The outcome of the evaluation of a script must depend only on the data committed to by the transaction. 
2. The language must strike a balance between complexity(or)features that it can offer and the resources required to validate (processing power) and transmit (bandwidth) transactions
3. The computational cost of any script that can be created using the language has to be deterministic (i.e) it should be possible to calculate ahead of time, how long will it take for the script to be evaluated. 

# References

[^1]: https://bitcoin.stackexchange.com/questions/553/how-do-scripts-work
[^2]: https://bitcoin.stackexchange.com/questions/114034/is-bitcoin-script-necessary?noredirect=1&lq=1
[^3]: https://bitcoin.stackexchange.com/questions/29754/history-behind-the-scripting-language-in-bitcoin
[^4]: M. Antonopoulos, A., & A. Harding, D. (n.d.). Authorization and Authentication: Stateless verification. In _Mastering Bitcoin_ (3rd ed., p. 262). O’REILLy.
[^5]: https://bitcoin.stackexchange.com/questions/114034/is-bitcoin-script-necessary?noredirect=1&lq=1