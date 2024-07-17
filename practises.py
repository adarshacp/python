hash_table=[[] for _ in range(10)]

def hash_func(key):
    return key % len(hash_table)
def insert(hash_table,key,value):
    hash_key=hash_func(key)
    bucket=hash_table[hash_key]
    bucket.append((key,value))

insert(hash_table,10,'nepal')
insert(hash_table,25,'usa')
insert(hash_table,20,'india')
insert(hash_table,36,'bihar')
print(hash_table)
