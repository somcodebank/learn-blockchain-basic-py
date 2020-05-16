def pseudo_hash(data):
    return '<hash>' + data + '</hash>'


def hash(data):
    return pseudo_hash(data)


class Block:
    def __init__(self, data, hash_data, last_hash_data):
        self.data = data
        self.hash = hash_data
        self.last_hash = last_hash_data


one_block = Block('one_data', hash('one_hash'), 'one_last_hash')

print(one_block.data)
print(one_block.hash)
print(one_block.last_hash)
