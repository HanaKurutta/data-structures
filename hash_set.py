class HashSet():
    def __init__(self, *keys):
        self.add(*keys)
        self.__table = [[] for _ in range(5)]

    def add(self, *keys):
        for key in keys:
            if self.has(key):
                continue

            code = self.__hash(key)
            buck_ind = code % len(self.__table)

            if len(self.__table[buck_ind]) >= 2:
                self.__rebuild(len(self.__table) * 2)
                buck_ind = code % len(self.__table)

            self.__table[buck_ind].append(key)

    def has(self, key):
        code = self.__hash(key)
        buck_ind = code % len(self.__table)

        for item in self.__table[buck_ind]:
            if item == key:
                return True
        return False

    def __hash(self, key):
        cont = 0

        for letter in key:
            cont += ord(letter)

        return cont

    def __rebuild(self, bucket_count):
        new_table = [[] for _ in range(bucket_count)]

        for bucket in self.__table:
            for key in bucket:
                code = self.__hash(key)
                buck_ind = code % bucket_count
                new_table[buck_ind].append(key)
                
        self.__table = new_table
