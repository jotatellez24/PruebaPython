#################################
import pytest  
from clase import *
def test_is_prime():
    
    assert is_prime(0)==False
    assert is_prime(1)==False 
    assert is_prime(2)==True 
    assert is_prime(3)==True 
    assert is_prime(4)==False
 
#Falla
#  def test_is_prime():
#     assert is_prime(0)==True
#     assert is_prime(1)==False 
#     assert is_prime(2)==True 
#     assert is_prime(3)==True 
#     assert is_prime(4)==False
  
#Falla
# def test_fibonacci():
#     assert fibonacci(1) == 2
#     assert fibonacci(2) == 1
#     assert fibonacci(3) == 2
#     assert fibonacci(4) == 3
#     assert fibonacci(5) == 5
#     assert fibonacci(6) == 8
#     assert fibonacci(7) == 13
#     assert fibonacci(8) == 21

##################################
def test_fibonacci():

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
