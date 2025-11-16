from src import fav

def deploy_fav():
    print("Hi")
    fav_con = fav.deploy()
    s_num = fav_con.retrieve()
    print(f'Starting number {s_num}')
    
    fav_con.store(5)
    n1 = fav_con.retrieve()
    print(f'After updating {n1}')
    return fav_con
    
def moccasin_main():     #Here both calling main function and moccasin main works.
    deploy_fav()