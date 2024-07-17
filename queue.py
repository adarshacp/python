class Queue:
    def __init__(self, size):
        self.size = size
        self.q = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def dequeue(self):
        if self.is_empty():
            print("Empty list")
        else:
            print("Removing element", self.q[self.front])
            if self.rear == self.front:
                self.rear = -1
                self.front = -1
                self.q.clear()
            else:
                self.front += 1

    def insert_queue(self):
        if self.rear == self.size - 1:
            print("Overflow")
        else:
            value = int(input("Enter item to insert: "))
            print("Inserting element", value)
            self.rear += 1
            self.q.append(value)
            if self.front == -1:
                self.front = 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print('The queue is:', end=' ')
        i = self.front
        while i <= self.rear:
            print(self.q[i], end=' ')
            i += 1
        print()

qu = Queue(2)

while True:
    print("Enter 1 to insert, 2 to delete, 3 to display, 4 to stop")
    choice = int(input("Input choice: "))

    if choice == 1:
        qu.insert_queue()
    elif choice == 2:
        qu.dequeue()
    elif choice == 3:
        qu.display()
    elif choice == 4:
        print("---End---")
        break
    else:
        print("Invalid choice")
