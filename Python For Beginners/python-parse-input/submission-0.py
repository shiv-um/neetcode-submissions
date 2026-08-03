from typing import List

def read_integers() -> List[int]:
    pass
    user_input = input().split(",")
    int_list = []
    for i in user_input:
        int_list.append(int(i))
    
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
