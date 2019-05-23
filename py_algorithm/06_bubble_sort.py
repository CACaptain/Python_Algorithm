# qianGuang /2019/5/17  /github:CACaptain   /1376420235@qq.com

def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1, 0, -1):
        count = 0
        for i in range(j):
    # for j in range(n-1):
    #     for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
            if count == 0:
                break
                # return


if __name__ == "__main__":
    li = [2, 4, 3, 8, 5, 1, 9, 0, 7, 6]
    print(li)
    bubble_sort(li)
    print(li)

    #稳定 Q(n^2)