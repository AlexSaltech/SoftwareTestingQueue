# Regression Testing
# ------------------
# The goal of this problem is for you to write a regression tester
# for the Queue class.
#
# Begin by finding and fixing all of the bugs in the Queue class. Next,
# define the function regression_test to take in a list of enqueue inputs
# and dequeue indicators (the returned list of the previous problem) and
# repeat those method calls using the fixed Queue.
#
# That is, after fixing the Queue class, create a new Queue instance,
# and call the method corresponding to the indicator in the list
# for each item in the list:
#
# Call the enqueue function whenever you come across an integer, using that
#     integer as the argument.
# Call the dequeue function whenever you come across the 'dq' indicator.

import array
import errorQueueRandom


# Fix this Queue class
class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max - 1
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self, x):
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size <= 0:
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
            assert (self
                    .size == 0) or (self.size == self.max)


# An example list of enqueue integers and dequeue indicators
'''
inputs = [(574, 0), ('dq', 0), (991, 0), ('dq', 0), ('dq', 1),
         (731, 0), (97, 0), ('dq', 0), (116, 0), ('dq', 0),
         (464, 0), (723, 0), (51, 0), ('dq', 0), (553, 0),
         (390, 0), ('dq', 0), (165, 0), (952, 0), ('dq', 0),
         ('dq', 0), (586, 0), (894, 0), ('dq', 0), ('dq', 0),
         (125, 0), (802, 0), (963, 0), (370, 0), ('dq', 0),
         ('dq', 0), (467, 0), (274, 0), ('dq', 0), (737, 0),
         (665, 0), (996, 0), (604, 0), (354, 0), ('dq', 0),
         (415, 0), ('dq', 0), ('dq', 0), ('dq', 0), ('dq', 0),
         ('dq', 0), (588, 0), (702, 0), ('dq', 0), ('dq', 0),
         (887, 0), ('dq', 0), (286, 0), (493, 0), (105, 0),
         ('dq', 0), (942, 0), ('dq', 0), (167, 0), (88, 0),
         ('dq', 0), (145, 0), ('dq', 0), (776, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), ('dq', 0), (67, 0), ('dq', 0),
         ('dq', 0), (367, 0), ('dq', 0), (429, 0), (996, 0),
         (508, 0), ('dq', 0), ('dq', 0), (295, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), (997, 0), ('dq', 0), (29, 0),
         (669, 0), ('dq', 0), (911, 0), ('dq', 0), ('dq', 0),
         (690, 0), (169, 0), (730, 0), (172, 0), (161, 0),
         (966, 0), ('dq', 0), (865, 0), ('dq', 0), (348, 0)]
'''


# Write a regression tester for the Queue class
def regression_test(inputs):
    size = 15
    q = Queue(size)
    out = []
    checkQ = []
    for inp in inputs:
        num = inp[0]
        if isinstance(num, int):
            # If it is an enqueue
            if len(checkQ) >= size:
                try:
                    assert not q.enqueue(num)
                    q.checkRep()
                    out.append((num, 0))
                except AssertionError:
                    out.append((num, 1))
            else:
                try:
                    assert q.enqueue(num)
                    q.checkRep()
                    checkQ.append(num)
                    out.append((num, 0))
                except AssertionError:
                    out.append((num, 1))
        else:
            # If it is a dequeue
            if len(checkQ) <= 0:
                try:
                    assert q.dequeue() is None
                    q.checkRep()
                    out.append(('dq', 0))
                except AssertionError:
                    out.append(('dq', 1))
            else:
                try:
                    assert q.dequeue() == checkQ.pop(0)
                    q.checkRep()
                    out.append(('dq', 0))
                except AssertionError:
                    out.append(('dq', 1))
    return out

inputs = errorQueueRandom.random_test()
outputs = regression_test(inputs)
print "\nInputs:\n"
for x in inputs:
    print x
print "\n\nOutputs:\n"
for x in outputs:
    print x
print inputs == outputs
