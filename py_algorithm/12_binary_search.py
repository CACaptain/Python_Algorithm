# qianGuang /2019/5/18  /github:CACaptain   /1376420235@qq.com
def binary_search(alist, item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search1(alist, item):

    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":

    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(li, 0))
    print(binary_search(li, 5))
    print(binary_search(li, 9))
    print(binary_search(li, 18))
    print("------")
    print(binary_search1(li, 0))
    print(binary_search1(li, 5))
    print(binary_search1(li, 9))
    print(binary_search1(li, 12))

    # logN