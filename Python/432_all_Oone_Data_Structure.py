class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table={}
        self.max=""
        self.min=""

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if not key:
            return
        if key in self.table:
            self.table[key]+=1
        else:
            self.table[key]=1

        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.table:
            if self.table[key] > 1:
                self.table[key] -= 1
            else:
                self.table.pop(key)
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.table:
            max=0
            for key in self.table:
                if self.table[key]>max:
                    max=self.table[key]
                    self.max=key
        else:
            self.max=""
        return self.max
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.table:
            min='a'
            for key in self.table:
                if self.table[key]<min:
                    min=self.table[key]
                    self.min=key
        else:
            self.min=""
        return self.min

    def display(self):
        print self.table
        self.getMaxKey()
        self.getMinKey()
        print "max=%s"%self.max
        print "min=%s"%self.min
        
if __name__ == '__main__':
    obj = AllOne()

    obj.inc('a')
    obj.display()
    obj.inc('b')
    obj.display()
    obj.inc('b')
    obj.display()
    obj.inc('b')
    obj.display()
    obj.inc('b')
    obj.display()
    obj.dec('b')
    obj.display()
    param_3 = obj.getMaxKey()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()