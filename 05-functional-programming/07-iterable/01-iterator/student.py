class InclusiveRangeIterator:
    def __init__(self,start,end):
        self.__current_index =start
        self.__end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.__current_index <= self.__end:
            result = self.__current_index
            self.__current_index +=1
            return result
        else: raise StopIteration

class InclusiveRange:
    def __init__(self,start,end):
        self.__start = start
        self.__end = end
    def __iter__(self):
        return InclusiveRangeIterator(self.__start,self.__end)