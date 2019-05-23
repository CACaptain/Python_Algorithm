# qianGuang /2019/5/17  /github:CACaptain   /1376420235@qq.com

def shellSort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
         #gap步长
        gap //= 2

if __name__ == "__main__":
    li = [2, 4, 3, 8, 5, 1, 9, 0, 7, 6]
    print(li)
    shellSort(li)
    print(li)

#T=O(n^2)  不稳定