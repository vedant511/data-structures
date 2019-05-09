from queue_ds.Queue import Queue

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
