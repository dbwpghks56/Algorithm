def solution(numbers: list):
    defaultList = [0,1,2,3,4,5,6,7,8,9]

    for i in numbers:
        defaultList.remove(i)
    print(defaultList)

    return sum(defaultList)