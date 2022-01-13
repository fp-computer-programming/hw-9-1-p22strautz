# Author: SCT (AMDG) 1/12/22

def find_thing(list_or_string, to_be_found):
    for i, v in enumerate(list_or_string):
        try:
            if to_be_found in v:
                print(i)
                break
            elif to_be_found not in list_or_string:
                print(-1)
                break
                
        except: print("Invalid Input")
                
find_thing("apple", "p")
