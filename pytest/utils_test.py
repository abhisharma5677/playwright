# Simple use case for using pytest

import utils

def test_root():
    print("Testing for 25....")
    root_25 = utils.root(25) 
    print(f"....Got the {root_25}")
    assert root_25 == 5


# TO run the pytest...
# 1. pytest utils_test.py      ---> simply running the pytest
# 2. pytest -v utils_test.py    ---> to get some more info about the test going on
# 3. pytest -s utils_test.py    ----> to get the print statements used in testing