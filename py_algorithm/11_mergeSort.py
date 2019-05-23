# qianGuang /2019/5/18  /github:CACaptain   /1376420235@qq.com
def merge_sort(alist):
    n= len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    li = [2, 4, 3, 8, 5, 1, 9, 0, 7, 6]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)

#最优n(logN) 最坏(n(lonn) 稳定