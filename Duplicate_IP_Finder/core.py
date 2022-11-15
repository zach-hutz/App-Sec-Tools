if __name__ in '__main__':
    addresses = input("Enter ips: ")
    addresses = addresses.split(", ")
    if len(addresses) != len(set(addresses)):
        print("Duplicates found: ", {x for x in addresses if addresses.count(x) > 1})
    else:
        print("No duplicates found!")
