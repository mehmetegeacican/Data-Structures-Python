

class HashTable:

    def __init__(self):
        self.MAX = 97
        self.arr = [[] for i in range(self.MAX)] #LIST IS BEING USED FOR CHAINING

    #**HASHING FUNCTION********
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 97

    def addValue(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def getValue(self,key):
        h = self.get_hash(key) 
        return self.arr[h]

    def setValue(self,key,value):
        hash_index = self.get_hash(key)
        for idx,ele in enumerate(self.arr[hash_index]):
            if ele[0]==key and len(ele)==2:
                self.arr[hash_index][idx] = (key,value)
                break
        else:
            self.arr[hash_index].append((key,value))
    
    def deleteValue(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    #DICTIONARY IMPLEMENTATION -2 DUNDERS
    def __setitem__(self,key,value):
        hash_index = self.get_hash(key)
        for idx,ele in enumerate(self.arr[hash_index]):
            if ele[0]==key and len(ele)==2:
                self.arr[hash_index][idx] = (key,value)
                break
        else:
            self.arr[hash_index].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __delitem__(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


    #DICTIONARY IMPLEMENTATION
"""t = HashTable()
print(t.get_hash("asdasda awaeasd"))
t['march 2'] = 7
t['march 1'] = 8
t.setValue('march 1',19)

del t['march 1']
print(t.getValue("march 2"))
print(t['march 1'])
print(t.arr)"""