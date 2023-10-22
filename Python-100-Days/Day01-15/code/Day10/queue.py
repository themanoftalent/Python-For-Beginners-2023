class QueueTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def enqueue(self, item):
        self.in_stack.append(item)
    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empy queue")
        return self.out_stack.pop()
class MaxStack(QueueTwoStacks):
    def get_max(self):
        return max(self.out_stack)
stacks = MaxStack()
stacks.in_stack = [1,2,3]
stacks.enqueue(3)
print stacks.in_stack
print stacks.dequeue()
print stacks.out_stack
print stacks.in_stack
print stacks.get_max()
