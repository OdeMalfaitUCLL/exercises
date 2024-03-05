class CircularBuffer:
    def __init__(self,n):
        self.__max_size = n
        self.__items = []
    def add(self,item):
        self.__items.append(item)
        if len(self.__items) > self.__max_size:
            self.__items.remove(self.__items[0])
            
    def __getitem__(self,index):
        return self.__items[index]
    def __len__(self):
        return len(self.__items)

buffer = CircularBuffer(3)
print(len(buffer))