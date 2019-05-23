# qianGuang /2019/5/16  /github:CACaptain   /1376420235@qq.com
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):   #单向循环链表
    def __init__(self, node=None):
        self._head = None
        if node:    #如果链表只有一个元素
            node.next = node

    def is_empty(self):
        return self._head is None

    def length(self):
        if self.is_empty():
            return 0
        cur =self._head  #cur:游标
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):   #遍历
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def append(self, item):  #尾插法
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self.head:
                cur = cur.next
            # node.next = cur.next
            node.next = self._head
            cur.next = node

    def add(self, item):    #头插法
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self.head:
                cur = cur.next
            node.next = self._head
            self._head = node
            # cur.next = node
            cur.next = self._head

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
        if self.is_empty():
            return
        pre = None
        cur = self._head
        while cur.next != self._head:  #循环条件，cur为None
            if cur.elem == item:   #查找所要删除的元素
                #先判断此点是否为头节点
                if cur ==self._head:    #判断是否为头节点
                    rear =self._head
                    while rear.next != self._head:
                        rear = rear.next
                        rear.next = self._head
                else:   #中间结点
                    pre.next = cur.next #删除的方法
                return
            else:   #移动浮标
                pre = cur
                cur = cur.next
            if cur.elem == item: #退出循环 cur指向尾节点
                if cur ==self._head:
                    # 链表只有一个节点
                    self._head = None
                else:
                    # pre.next = cur.next
                    pre.next = self._head

    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
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
