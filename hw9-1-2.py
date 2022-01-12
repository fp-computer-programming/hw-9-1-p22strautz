# Author: SCT (AMDG) 1/12/22

def odd_number(list):
    for i, v in enumerate(list):
        try:
            if i % 2 != 0:
                print(int(v))
        except:
            if v == str or bool:
                print("Only input integers")

odd_number([1, "two", 3, 4, 5, 6])