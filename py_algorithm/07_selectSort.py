# qianGuang /2019/5/17  /github:CACaptain   /1376420235@qq.com
def select_sort(alist):
    n = len(alist)
    for j in range(n-1): #j:0~n-2
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] =alist[min_index], alist[j]


if __name__ == "__main__":
    li = [2, 4, 3, 8, 5, 1, 9, 0, 7, 6]
    print(li)
    select_sort(li)
    print(li)

    #时间复杂度；O(n^2)  不稳定