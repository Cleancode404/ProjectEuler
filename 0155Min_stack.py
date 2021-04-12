class MinStack(object):
    '''
    initialize data structure here
    '''  
    def __init__(self):
        self.stack = []
        self.min_stack = []
    

    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
            return 
        if x <= self.min_stack[-1]:
            self.min_stack.append(x):
            
        

