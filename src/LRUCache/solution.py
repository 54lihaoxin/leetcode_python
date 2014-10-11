# LRU Cache
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
# 
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


class LRUCache:
    
    # hxl: obviously this is not a thread safe implementation

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.usedCapacity = 0
        self.keyNodeDict = {}    # hxl: K: a key; V: the list node that stores the value tuple (key, value)
        
        # hxl: the value of the list node is a tuple of (key, value)
        self.head = DoublyLinkedListNode((0, 0)) # hxl: next to head is the most recently used node
        self.tail = DoublyLinkedListNode((0, 0)) # hxl: next to head is the least recently used node
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # @return the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    def get(self, key):
        node = self.keyNodeDict.get(key)
        if node != None:
            (k, v) = node.val
            self.markRecentlyUsed(key)
            return v
        else:
            return -1     

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):        
        node = self.keyNodeDict.get(key)
        if node != None:
            self.markRecentlyUsed(key)
            node.val = (key, value)   
        else:   # hxl: the key is new
            if self.usedCapacity < self.capacity:   # hxl: add new node to linked list
                self.usedCapacity += 1
                newNode = DoublyLinkedListNode((key, value))
                newNode.prev = self.head
                newNode.next = self.head.next
                self.head.next.prev = newNode
                self.head.next = newNode
                self.keyNodeDict[key] = newNode                
            else:   # hxl: else replace the value of LRU node
                (LRUKey, LRUVal) = self.tail.prev.val
                self.keyNodeDict.pop(LRUKey)
                self.keyNodeDict[key] = self.tail.prev
                self.keyNodeDict[key].val = (key, value)
                self.markRecentlyUsed(key)
        
    def markRecentlyUsed(self, key):
        node = self.keyNodeDict[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def __repr__(self):
        r = '<< '
        cur = self.head.next
        while cur != self.tail:
            (k, v) = cur.val
            r += '{0}:{1} '.format(k, v)
            cur = cur.next
        return r + '>>'
    