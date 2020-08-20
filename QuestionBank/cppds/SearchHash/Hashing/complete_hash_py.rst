.. activecode:: complete_hash_py
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: SearchHash
   :subchapter: Hashing
   :topics: SearchHash/Hashing
   :from_source: T
   :caption: Complete Hash Table Example
   :optional:

   class HashTable:
       def __init__(self):
           self.size = 11 # initial size of hash table is prime to help with collision resolution
           self.slots = [None] * self.size # list to hold key items
           self.data = [None] * self.size # list to hold data values

       def put(self,key,data):
         hashvalue = self.hashfunction(key,len(self.slots))

         if self.slots[hashvalue] == None:
           self.slots[hashvalue] = key
           self.data[hashvalue] = data
         else:
           if self.slots[hashvalue] == key:
             self.data[hashvalue] = data  #replace
           else:
             nextslot = self.rehash(hashvalue,len(self.slots))
             while self.slots[nextslot] != None and \
                             self.slots[nextslot] != key:
               nextslot = self.rehash(nextslot,len(self.slots))

             if self.slots[nextslot] == None:
               self.slots[nextslot]=key
               self.data[nextslot]=data
             else:
               self.data[nextslot] = data #replace

        # Function that assumes there will eventually be
        # an empty slot unless the key is alread present in the slot
       def hashfunction(self,key,size): # implements remainder method
            return key%size

        # Fomputes original hashvalue, and if slot is
        # not empty iterates until empty slot is found
       def rehash(self,oldhash,size):
           return (oldhash+1)%size

        # computes the initial hash value
        # if value is not in the initial slot, uses
        # rehash to locate the next position
       def get(self,key):
         startslot = self.hashfunction(key,len(self.slots))

         data = None
         stop = False
         found = False
         position = startslot
         while self.slots[position] != None and  \
                              not found and not stop:
            if self.slots[position] == key:
              found = True
              data = self.data[position]
            else:
              position=self.rehash(position,len(self.slots))
              if position == startslot:
                  stop = True
         return data

       def __getitem__(self,key):
           return self.get(key)

       def __setitem__(self,key,data):
           self.put(key,data)

   H=HashTable()
   H[54]="cat"
   H[26]="dog"
   H[93]="lion"
   H[17]="tiger"
   H[77]="bird"
   H[31]="cow"
   H[44]="goat"
   H[55]="pig"
   H[20]="chicken"
   print(H.slots)
   print(H.data)

   print(H[20])

   print(H[17])
   H[20]='duck'
   print(H[20])
   print(H[99])