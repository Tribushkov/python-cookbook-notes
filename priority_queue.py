import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push (self, item, priority):
        heapq.heappush(self._queue, (-priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]


q = PriorityQueue()
q.push('item', 1)
q.push('foo', 3)
q.push('bar', 5)
q.push('hello', 1)

print q.pop()  # bar
print q.pop()  # foo
print q.pop()  # hello
