def buildArray(target,n):
    target2 = []
    check = 0
    for i in range(1, n + 1):
        if target[check] == i:
            target2.append("Push")
            check += 1
        else:
            target2.append("Push")
            target2.append("Pop")
        if check == len(target):
            break
    return target2


print(buildArray([1,4],4))