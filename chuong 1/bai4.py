
class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size  
    def isFull(self):
        return len(self.stack) == self.max_size

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy!")
        else:
            self.stack.append(value)
            print(f"Đã thêm {value} vào ngăn xếp.")
            
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
            return None
        else:
            return self.stack.pop()

   