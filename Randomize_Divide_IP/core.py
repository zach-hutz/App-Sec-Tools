import random

def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist

def split_list(mylist):
    listLength = len(mylist)
    split1 = mylist[:listLength//3]
    split2 = mylist[listLength//3:listLength//3*2]
    split3 = mylist[listLength//3*2:]
    return split1, split2, split3

if __name__ in '__main__':
    newList = []
    ipLIST = input("Enter ips: ")
    ipLIST = ipLIST.split(", ")

    if len(ipLIST) <= 1:
        print("No IPs entered!")
        raise SystemExit
    else:
        for _ in range(5):
            newList = shuffle_list(ipLIST)

split1, split2, split3 = split_list(newList)

print("Split 1: ", split1, end='\n')
print("Split 2: ", split2, end='\n')
print("Split 3: ", split3, end='\n')
