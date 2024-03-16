# ---------Environmental SetUp----------
# 1. create a virtual environment    ---> sudo apt-get install python3-venv    ----> python3 -m venv venv
# 2. enter into virtual environment  ----> source venv/bin/activate
# 3. install pytest   ---> pip install pytest


#  Simple use case for using pytest

def root(num : int) -> float:
    return pow(num,0.5)

