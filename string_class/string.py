class String(list):

    def __init__(self, string):
        if all(len(letter) == 1 for letter in string):
            super().__init__(string)
        else:
            raise TypeError('The list must contain single-character strings only')

    def __str__(self):
        return ''.join(self)

    def append(self, __object):
        self.extend([__object])

    def insert(self, __index, __object):
        self[__index:__index] = [__object]

    def remove(self, __value):
        for index in range(len(self)):
            if self[index] == __value:
                del self[index]
                break

    def replace(self, __old_char, __new_char):
        for index in range(len(self)):
            if self[index] == __old_char:
                self[index] = __new_char

    def reverse(self):
        self[:] = self[::-1]

    def upper(self):
        for index in range(len(self)):
            self[index] = self[index].upper()

    def lower(self):
        for index in range(len(self)):
            self[index] = self[index].lower()

    def __add__(self, other):
        result = super().__add__(other)
        return String(result)

    def __mul__(self, other):
        result = super().__mul__(other)
        return String(result)

    @classmethod
    def read_file(cls, filename: str):
        with open(filename, 'r') as file:
            data = file.read().split()
        return cls(data)
