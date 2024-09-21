class Stack:
    def __init__(self):
        self.stack_list = []
    
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
    
    def push(self, value):

        self.stack_list.append(value)
    
    def pop(self):
        if not len(self.stack_list) ==0:
            return self.stack_list.pop()
        else:
            return None



my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

print("Stack before pop(): ")
my_stack.print_stack()
print("\nPopped node: ")
print(my_stack.pop())

print("\nStack after pop(): ")
my_stack.print_stack()

###Extected output:
#5
#4
#3
#2
#1


