# qianGuang /2019/5/17  /github:CACaptain   /1376420235@qq.com
def insertSort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    li = [2, 4, 3, 8, 5, 1, 9, 0, 7, 6]
    print(li)
    insertSort(li)
    print(li)

    # 时间复杂度；O(n^2)  稳定
