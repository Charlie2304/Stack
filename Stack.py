# [Stack]
# [Charlie Smith]
# [16/12/25]
# AS Computer Science

# Constants

MAX_NUMBER = 5

# Global Variables

stack = []
top = -1

# Subprograms

# [Push command]
def push(stack, item):
    stack.append(item)
    if (len(stack) > MAX_NUMBER):
        print("Stack is full, stack overflow")
    else:
        return stack

    

# [Pop command]
def pop(stack):
    stack.pop()
    if len(stack) == 0:
        print("Stack is empty, stack underflow")
    else:
        return stack

# [Peek command]
def peek(stack):
    print(stack[-1])

# [Check empty]

def ifEmpty(stack):
    if(len(stack) == 0):
        print("List is empty")
    
    


# Main Program

push(stack, 100)
push(stack, 200)
print(stack)
peek(stack)
pop(stack)
pop(stack)
print(stack)
