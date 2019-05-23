# qianGuang /2019/5/15  /github:CACaptain   /1376420235@qq.com
class quene(object):

    def __init__(self):
        self.__list = []

    def enquence(self, item):
        self.__list.append(item)

    def denquence(self, item):
        self.__list.insert(0, item)

    def dequence(self):
        return self.__list.pop(0)

    def adequence(self):
        return self.__list.pop(-1)

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = quene()
    s.enquence(6)
    s.enquence(7)
    s.enquence(8)
    s.enquence(9)
    s.denquence(1)
    s.denquence(2)
    s.denquence(3)
    print(s.size())
    print(s.dequence())
    print(s.adequence())
    print(s.adequence())
    print(s.is_empty())
    print(s.size())

