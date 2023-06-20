#!/usr/bin/env python3


class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

    def insert(self, word: str) -> None:
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = Trie()
            current = current.children[c]
        current.word = True

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.word

    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True
