from functions import add
import numpy as np

def test_add():
  assert add(3, 4) == 7 # assert is central format for unit tests. if after statement there is a value that is true, then nothing happens. if false an exception at line 4 happens

def test_show_printing():
    matrix = np.random.rand(5, 5)
    print(matrix)
    assert False 
