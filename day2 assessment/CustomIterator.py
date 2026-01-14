class NumberIterator:
    def __init__(self,number):
        self.number=number
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<= self.number:
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration

obj = NumberIterator(5)
for num in obj:
    print(num)