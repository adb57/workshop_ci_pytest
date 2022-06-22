from functions import add
import pytest

@pytest.mark.parametrize(
  "x, y, result", [(1,2,3), (3,4,7), (4,5,9)]
  )

def test_add(x, y, result):
  assert add(x, y) == result # assert is central format for unit tests. if after statement there is a value that is true, then nothing happens. if false an exception at line 4 happens
  
