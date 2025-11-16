##from src import fav
#But if we did this, it will chech cases in fav.vy file. but what if we store
#and interact from scripts file, so we need to deploy scripts file.

from script.deploy import deploy_fav  #import the function
import pytest

'''
function --> it is default arguement, deploys contract or every function written.
session --> it deploys contract only once for entire test file.
'''
@pytest.fixture(scope="function")#Deploy contract at once and pass as argument to all other function
def fav():
    return deploy_fav()

def test_start_val(fav):
    
    assert fav.retrieve() == 5
    
def test_can_change_values(fav):
    #arrange
    
    #act
    fav.store(15)
    #assert
    assert fav.retrieve() == 15
    
def test_can_add_people(fav):
    #arrange
    new_person = "Starc"
    fav_num = 56
    #act
    fav.add_person(new_person, fav_num)
    #assert
    assert fav.list_of_people(0) == (fav_num, new_person)  #Arguments to be passed correctly