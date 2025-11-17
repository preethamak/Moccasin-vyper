from src import fav
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_fav() -> VyperContract:
    print("Hi")
    fav_con: VyperContract =  fav.deploy()
    s_num : int= fav_con.retrieve()
    print(f'Starting number {s_num}')
    
    fav_con.store(5)
    n1 : int = fav_con.retrieve()
    print(f'After updating {n1}')
    
    active_network = get_active_network()
    #fav_con = fav.at("0xcd932d2a2EF5deCE3E636f76456333F093232e2f")  Only if contract is already deployed
    
    print(active_network)
    if active_network.has_explorer():
        res = active_network.moccasin_verify(fav_con)
        res.wait_for_verification()  #Waits until the verification of the contract is done
        
    return fav_con
    
def moccasin_main():     #Here both calling main function and moccasin main works.
    deploy_fav()