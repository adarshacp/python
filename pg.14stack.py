class Stack:
    def __init__(self, size):
        self.maximize = size
        self.top = -1
        self.list = []

    def isempty(self):
        return self.top == -1

    def isfull(self):
        return self.top == self.maximize - 1

    def push(self, value):
        if self.isfull():
            print("Can't add! Stack is full")
            return
        else:
            self.top += 1
            self.list.append(value)
            print(value, "has been added successfully!")

    def pop(self):
        if self.isempty():
            print("The stack is empty")
            return
        else:
            print("Popped item:", self.list.pop())
            self.top -= 1

    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.list)


stk = Stack(3)
print("\n Enter 1 to push 2 to pop 3 to display 4 to stop:")
choice = int(input("Input choice: "))
while choice in [1, 2, 3]:
    if choice == 1:
        item = int(input("Enter item to push: "))
        stk.push(item)
    elif choice == 2:
        stk.pop()
    elif choice == 3:
        stk.display()
    print("\n Enter 1 to push 2 to pop 3 to display 4 to stop:")
    choice = int(input("\nInput choice: "))
print("End")
