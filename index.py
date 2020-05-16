class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash


one_block = Block('one_data', 'one_hash', 'one_last_hash')

print(one_block.data)
print(one_block.hash)
print(one_block.last_hash)
