import time
import random

class Stack:
	"""
	Represents a stack data structure
	"""
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		last = len(self.items)-1
		return self.items[last]

	def size(self):
		return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
    	pq = Queue()
    	tix_sold = []
    	for i in range(10):
    		pq.enqueue("person"+ str(i))
    	t_end = time.time() + till_show
    	now = time.time()
    	while now < t_end and not pq.is_empty():
    		now = time.time()
    		r = random.randint(0, max_time)
    		time.sleep(r)
    		person = pq.dequeue()
    		print(person)
    		tix_sold.append(person)
    	return tix_sold


queue = Queue()
x = queue.simulate_line(30, 3)
print(x)
