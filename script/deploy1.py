from src import fav, fav_fac
from moccasin.boa_tools import VyperContract

def deploy_fav() -> VyperContract:
    fav_con: VyperContract = fav.deploy()
    return fav_con

def deploy_fact(fav_con : VyperContract):
    fac_con = fav_fac.deploy(fav_con)
    # create a new copy via the factory
    fac_con.create_fav_con()
    
    # read the new address from the factory (NOT from fav_con)
    new_fav_add: str = fac_con.list_of_fav_con(0)
    new_fav_con: VyperContract = fav.at(new_fav_add)
    
    # interact with the new copy
    new_fav_con.store(5)
    
    fac_con.save_from_fac(0, 15)
    print(f'Stored value in new contract is {new_fav_con.retrieve()}')
    print(f'stored value in original contract is {fav_con.retrieve()}')
    
def moccasin_main():
    fav_con = deploy_fav()
    deploy_fact(fav_con)
