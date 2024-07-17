
#implement Hash Function & Hash Table

hash_table = [[] for _ in range(10)]

def hashing_func(key):
	return key % len(hash_table)

def insert(hash_table, key, value):
	hash_key = hashing_func(key)
	bucket = hash_table[hash_key]
	bucket.append((key, value))



#Driver code
insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
insert(hash_table, 36, 'Bihar')
print (hash_table)

