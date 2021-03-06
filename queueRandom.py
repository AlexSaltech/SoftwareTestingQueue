# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion. for instance, if 
# you wanted to randomly decide between 
# calling enqueue and dequeue, you would 
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

import array
import random


class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self, x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail - self.head) == self.size
        if self.tail < self.head:
            assert (self.head - self.tail) == (self.max - self.size)
        if self.head == self.tail:
            assert (self.size == 0) or (self.size == self.max)


# Write a random tester for the Queue class.
def test():
    size = 500
    q = Queue(size)
    checkQ = []
    for _ in range(100000):
        if random.random() < 0.5:
            num = random.randrange(0, 100)
            if len(checkQ) >= size:
                assert not q.enqueue(num)
                q.checkRep()
            else:
                assert q.enqueue(num)
                q.checkRep()
                checkQ.append(num)
        else:
            if len(checkQ) <= 0:
                assert q.dequeue() is None
                q.checkRep()
            else:
                assert q.dequeue() == checkQ.pop(0)
                q.checkRep()
    print "Success!"


test()
