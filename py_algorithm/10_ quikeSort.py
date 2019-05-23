# qianGuang /2019/5/17  /github:CACaptain   /1376420235@qq.com


def quickSort(alist, first, last):

    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    #退出循环时low = high
        alist[low] = mid_value
    #左边对子序列操作
        quickSort(alist, first, low-1)
        quickSort(alist, low+1, last)

if __name__ == "__main__":
    li = [2, 4, 3, 8, 5, 1, 9, 0, 7, 6]
    print(li)
    quickSort(li, 0, len(li)-1)
    print(li)

#最优T=O(n(log2^n)) 最坏n^2 不稳定