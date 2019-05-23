# qianGuang /2019/5/16  /github:CACaptain   /1376420235@qq.com
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    def __init__(self, node = None):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur =self._head  #cur:游标
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):   #遍历
        cur = self._head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print(" ")

    def append(self,item):  #尾插法
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def add(self, item):    #头插法
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node

    def insert(self, pos, item):    #添加元素
        # pos:位置 从0开始
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self. _head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self._head
        while cur is not None:  #循环条件，cur为None
            if cur.elem == item:   #查找所要删除的元素
                #先判断此点是否为头节点
                if cur ==self._head:
                    self._head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next    #删除的方法
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:   #移动浮标
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur.next is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = DoubleLinkList()
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
    print(ll.search(5))
    print(ll.search(100))