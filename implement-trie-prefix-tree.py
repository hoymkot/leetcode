# Leetcode 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = {};
        self.isInserted = False;

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if len(word) == 0:
            self.isInserted = True;
            return
        if self.next.get(word[0]) is None:
            self.next[word[0]] = Trie()
        self.next.get(word[0]).insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return self.isInserted
        if self.next.get(word[0]) is None:
            return False
        return self.next.get(word[0]).search(word[1:])

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return (self.isInserted == True or len(self.next) > 0)
        if self.next.get(prefix[0]) is None:
            return False
        return self.next.get(prefix[0]).startsWith(prefix[1:])

t = Trie()
t.insert("hello");
