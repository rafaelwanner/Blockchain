from block import Block

genesisBlock = Block("Initial Block")
genesisBlock.add_transaction("Satoshi pays Patoshi 10BTC")
genesisBlock.show_Block()

print("Genesis finished")

activeBlock = Block(genesisBlock.get_hash())

while True:

    i = input('Enter Transactions: ')

    if i == 'EXIT':
        print('Blockchain stopped')
        break
    elif i == 'NEXT': #next block
        activeBlock.show_Block()
        print('-----NEXT BLOCK-----')
        previousBlock = activeBlock.get_hash()
        activeBlock = Block(previousBlock)
    else:
        activeBlock.add_transaction(i)
        print('Transaction added')
