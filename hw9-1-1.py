# Author: SCT (AMDG) 1/12/22

def even_number(list):
    for i, v in enumerate(list):
        if i % 2 == 0:
            print(v)
            

even_number([1, 2, 3, 4, 5])

