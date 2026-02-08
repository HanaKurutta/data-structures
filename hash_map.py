class HashMap():
    def __init__(self, *items:list[tuple[str, any]]):
        self.__map = [[] for _ in range(5)]
        for key, value in items:
            self.set(key, value)


    def set(self, key : str, value):
        code = self.__hash(key)
        bucket_ind = code % len(self.__map)
        if self.has(key):
            for i in range(len(self.__map[bucket_ind])):
                if self.__map[bucket_ind][i][0] == key:
                    self.__map[bucket_ind][i] = (key, value)
            return
        if len(self.__map[bucket_ind]) > 2:
            self.__rebuild(len(self.__map) * 2)
            bucket_ind = code % len(self.__map)
        self.__map[bucket_ind].append((key, value))


    def has(self, key : str):
        code = self.__hash(key)
        bucket_ind = code % len(self.__map)
        for item in self.__map[bucket_ind]:
            if item[0] == key:
                return True
        return False   

    def __hash(self, key : str):
        counter = 0
        for letter in key:
            counter += ord(letter)
        return counter
    
    def __rebuild(self, count : int):
        new_map = [[] for _ in range(count)]
        for bucket in self.__map:
            for key, value in bucket:
                bucket_ind = self.__hash(key) % len(new_map)
                new_map[bucket_ind].append((key, value))
        self.__map = new_map
        