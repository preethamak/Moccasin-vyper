#



# pragma version 0.4.0
# @license MIT

import fav

initializes: fav

exports: (
    #fav.retrieve
    fav.__interface__ #This import everything from other contract, all functions and public variables
)

@deploy
def __init__():
    fav.__init__()
    print('Number from contract is', fav.my_favorite_number)

@external
def store(new_num: uint256):
    fav.my_favorite_number = new_num + 5
