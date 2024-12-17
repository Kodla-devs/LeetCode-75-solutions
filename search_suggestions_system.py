from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestion = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.suggestion) < 3:
                node.suggestion.append(word)
    
    def search(self, prefix):
        node = self.root
        result = []
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestion)
            else:
                result.extend([[] for _ in range(len(prefix) - len(result))])
                return result
        return result

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()

        for product in products:
            trie.insert(product)

        return trie.search(searchWord)