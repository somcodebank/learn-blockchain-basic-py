Learn to create basic Blockchain with Python

There is a single file, index.py, in this tiny project.
Index.py consists of

- Block class to server as a storage for
  - data
  - hash data (hash of this data and the hash data of the last block in the chain)
  - last hash (hash of the last block in the chain)
- Blockchain class to server as chain og blocks, consists of
  - add_block method
    - takes data as input
    - form a Block for this data
      with hash and last hash data
    - append this newly created Block to the chain
- hash function that is currently using pseudohas function
- pseudohas function that serves as a fake hashing funciton
  by simply encapsulate the data in <hash</hash>
