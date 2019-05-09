class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def print_queue(self):
        print(self.queue)
