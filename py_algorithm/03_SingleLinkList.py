# qianGuang /2019/5/16  /github:CACaptain   /1376420235@qq.com
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur =self._head  #cur:游标
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):   #遍历
        cur = self._head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print(" ")

    def append(self,item):  #尾插法
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):    #头插法
        node = Node(item)
        node.next = self._head
        self._head = node

    def insert(self, pos, item):    #添加元素
        # pos:位置 从0开始
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self. _head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        pre = None
        cur = self._head
        while cur != None:  #循环条件，cur为None
            if cur.elem == item:   #查找所要删除的元素
                #先判断此点是否为头节点
                if cur ==self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next #删除的方法
                break
            else:   #移动浮标
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.insert(-1, 9)
    ll.travel()
    print(ll.length())
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
