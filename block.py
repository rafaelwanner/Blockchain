class Block:

    def __init__(self, previousBlock):
        self.previousBlock = previousBlock #hash of previous block
        self.transactions = ['Coinbase Transaction'] #list of transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_hash(self):
        block = self.transactions
        block.append(self.previousBlock)
        print(tuple(block)) #append previous block hash to list of transactions
        return hash(tuple(block))

    def show_Block(self):
        print('Hash Previous Block: {}'.format(self.previousBlock))
        print('Transsactions: {}'.format(self.transactions))
