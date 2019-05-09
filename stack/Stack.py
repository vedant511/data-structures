class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.get_size() > 0:
            data = self.items[-1]
            del self.items[-1]
            return data
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)

    def peek(self):
        if self.get_size() > 0:
            return self.items[-1]
        else:
            return None

    def print_stack(self):
        print(self.items)
