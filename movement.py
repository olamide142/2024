from stack import *
import numpy as np

class Movement:
    
    def __init__(self, data):
        self.data = data
        self.stack = []

    def up(self):
        for datum in self.data:
            self.stack.append(stack_it_up(datum))
        return np.array(self.stack).transpose().tolist()

    def down(self):
        for datum in self.data:
            self.stack.append(stack_it_right(datum))
        return np.array(self.stack).transpose().tolist()
    
    def left(self):
        for datum in self.data:
            self.stack.append(stack_it_left(datum))
        return np.array(self.stack).transpose().tolist()

    
    def right(self):
        for datum in self.data:
            self.stack.append(stack_it_right(datum))
        print(np.array(self.stack).tolist())
        return np.array(self.stack).tolist()