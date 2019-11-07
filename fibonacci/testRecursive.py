def addRecursive(num):
    if num==1:
        return 1
    else:
        return num+addRecursive(num-1)

print(addRecursive(10))
