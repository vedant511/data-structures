class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def get_size(self):
        return self.size

    def add(self, item, pos=None):
        new_node = Node(item)
        if pos is not None:
            if pos <= 0 or pos > self.size+1:
                return False
            elif pos == 1:
                temp = self.head
                self.head = new_node
                new_node.next = temp
            elif pos == self.size+1:
                temp = self.tail
                self.tail = new_node
                temp.next = new_node
            else:
                prev = None
                curr = self.head
                count = 1
                while count != pos:
                    prev = curr
                    curr = curr.next
                    count += 1
                prev.next = new_node
                new_node.next = curr
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp
        self.size += 1
        return True

    def remove(self, item):
        if self.size == 0:
            return False
        prev = self.head
        curr = self.head
        while curr is not None:
            if curr.data == item:
                prev.next = curr.next
                curr.next = None
                self.size -= 1
                return True
            else:
                prev = curr
                curr = curr.next
        return False

    def pop(self, pos=None):
        if pos is None:
            temp = self.head.next
            self.head = temp
            self.head.next = None
        else:
            item = None
            if pos <= 0 or pos > self.size:
                return False
            elif pos == 1:
                temp = self.head.next
                self.head = temp
                self.head.next = None
            else:
                count = 0
                curr = self.head
                prev = None
                while count != pos:
                    prev = curr
                    curr = curr.next
                    count += 1
                item = curr.data
                prev.next = curr.next
                curr.next = None
            if item:
                return True, item
            else:
                return False

    def search(self, item):
        found = False
        curr = self.head
        count = 1
        while curr is not None:
            if curr.data == item:
                found = True
                break
            else:
                count += 1
                curr = curr.next
        if found:
            return found, count
        else:
            return found

    def index(self, item):
        idx = -1
        if self.head is None:
            return idx
        curr = self.head
        count = 1
        while curr is not None:
            if curr.data == item:
                idx = count
                break
            else:
                curr = curr.next
                count += 1
        return idx

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
