# pragma version 0.4.0
# @license MIT

#from interfaces import i_fav
interface i_fav:
    def store(new_num: uint256): nonpayable
    def retrieve() -> uint256: view

original_fav_con: address
list_of_fav_con: public(DynArray[address, 100])

@deploy
def __init__(original_fav_con: address):
    self.original_fav_con = original_fav_con
    
@external
def create_fav_con():
    new_fav_con: address = create_copy_of(self.original_fav_con)
    self.list_of_fav_con.append(new_fav_con)

@external
def save_from_fac(fav_index: uint256, new_num: uint256):
    fav_add: address = self.list_of_fav_con[fav_index]
    fav_con: i_fav = i_fav(fav_add)
    extcall fav_con.store(new_num)
#import all the function defination from i_fav.vyi file. Its messy to write everything in one file
