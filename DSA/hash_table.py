# Creating an hash table data type

class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__table = [None] * self.__size

    def __hash(self, key):
        hashed_value = abs(hash(key))
        index = hashed_value % self.__size
        return index
    
    def set(self, key, value):
        index = self.__hash(key)
        if self.__table[index] == None:
            self.__table[index] = []
        else:
            for item in self.__table[index]:
                if item[0] == key:
                    item[1] = value
                    return None
        self.__table[index].append([key, value])
        
            


    def get(self, key):
        index = self.__hash(key)
        if self.__table[index] == None:
            return None
        for item in self.__table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    def all(self):
        obj = {}
        for item in self.__table:
            if item is not None:
                for inner_item in item:
                    obj[inner_item[0]] = inner_item[1]
        return obj
    
    def keys(self):
        obj_keys = []
        for item in self.__table:
            if item is not None:
                for inner_item in item:
                    obj_keys.append(inner_item[0])
        return obj_keys
car = HashTable(100);
car.set("volvo", 42)
car.set("Volvo",24)
car.set("Ford", 68)
print(car.all())
print(car.keys())


# Creating an Ordered Hash Table

class HashTableOrdered: # I could inherit from the HashTable class above but i decided not to, so each class can stand on it's own for easier and faster understanding.
    def __init__(self, size):
        self.__size = size
        self.__table = [None] * self.__size
        self.__first_index = None
        self.__last_index = None

    def __hash(self, key):
        hashed_value = abs(hash(key))
        index = hashed_value % self.__size
        return index
    
    def get_last_index_data(self):
        if self.__last_index is None:
            return None
        return self.__table[self.__last_index][0]

    def update_last_index_data(self, data, current_index):
        if self.__last_index != current_index and data is not None:
            data.append(current_index)
        
    def set(self, key, value):
        index = self.__hash(key)
        if self.__table[index] == None:
            self.__table[index] = []
            if self.__first_index is None:
                self.__first_index = index
        else:
            for item in self.__table[index]:
                if item[0] == key:
                    item[1] = value
                    return None
        self.__table[index].append([key, value])
        self.update_last_index_data(self.get_last_index_data(), index)
        self.__last_index = index


    def get(self, key):
        index = self.__hash(key)
        if self.__table[index] == None:
            return None
        for item in self.__table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    def all(self):    
        obj = {}
        if self.__first_index is None:
            return None
        index = self.__first_index
                
        while index is not None:
            for item in self.__table[index]:
                obj[item[0]] = item[1]
            index_data = self.__table[index][0]
            if (len(index_data) == 3):
                index = index_data[2]
            else:
                index = None
        return obj
    
    def keys(self):
        obj_keys = []

        if self.__first_index is None:
            return None
        index = self.__first_index
                
        while index is not None:
            for item in self.__table[index]:
                obj_keys.append(item[0])
            index_data = self.__table[index][0]
            if (len(index_data) == 3):
                index = index_data[2]
            else:
                index = None
        return obj_keys


car = HashTableOrdered(100);
car.set("volvo", 42)
car.set("Volvo",24)
car.set("Ford", 68)
print(car.get("Ford"))
print(car.all())
print(car.keys())