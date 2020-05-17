def pseudo_hash(data):
    return '<hash>' + data + '</hash>'


def hash(data):
    return pseudo_hash(data)


class Block:
    def __init__(self, data, hash_data, last_hash_data):
        self.data = data
        self.hash = hash_data
        self.last_hash = last_hash_data


# one_block = Block('one_data', hash('one_hash'), 'one_last_hash')

# print(one_block.data)
# print(one_block.hash)
# print(one_block.last_hash)

class Blockchain:
    def __init__(self):
        genesis = Block('root', 'hash_root', 'last_hash_root')
        self.chain = [genesis]

    def add_block(self, data):
        last_hash = self.chain[-1].hash
        hash_data = hash(data + last_hash)
        block = Block(data, hash_data, last_hash)
        self.chain.append(block)


blockchain = Blockchain()
blockchain.add_block('1')
blockchain.add_block('2')
blockchain.add_block('3')

for block in blockchain.chain:
    print(block.__dict__)
