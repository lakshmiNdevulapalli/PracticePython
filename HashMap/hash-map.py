# Lookup key O(1) - avg case
# Insertion/Deletion O(1) - avg case

class HashMap:

    # Initialize HashMap
    def __init__(self, size):
        self.size = size
        self.map = [None] * size

    # Generate hash value using the Key
    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # Insert value into Hash table
    def add(self, key, value):
        # Get hash key value
        hash_key = self.get_hash(key)
        hash_value = [key, value]

        # Check if Hash key exits else add hash_value (new record)
        if self.map[hash_key] is None:
            self.map[hash_key] = list([hash_value])
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
            # append the value to existing record
            self.map[hash_key].append(hash_value)
            return True

    # Fetch the existing record from Hash table using the Key
    def get(self, key):
        # Get hash key value
        hash_key = self.get_hash(key)

        for pair in self.map[hash_key]:
            if pair[0] == key:
                return pair[1]

    # delete the existing with the key
    def delete(self, key):
        # Get hash key value
        hash_key = self.get_hash(key)

        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
        return False

    # print the hash map table records
    def print_hash_map(self):
        for item in self.map:
            if item is not None:
                print(str(item))


"""
Driver code
"""
hash = HashMap(size=6)
hash.add('Adam', '123-1423')
hash.add('Adam', '123-3445')
hash.add('Bob', '234-1423')
hash.add('Caleb', '345-2344')
hash.add('Dave', '456-1244')
hash.print_hash_map()
hash.delete('Bob')
hash.print_hash_map()
print('Adam: ' + hash.get('Adam'))
