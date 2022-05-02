import collections

# # Deprecated
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         def list2dict(word_list):
#             word_dict = {}
#             for word in word_list:
#                 word_dict[word] = [i for i in word_list if (len([1 for x, y in zip(word, i) if x != y]) == 1)]
#             return word_dict
#
#         visited = set()
#         queue = collections.deque([[i] for i in wordList if (len([1 for x, y in zip(beginWord, i) if x != y]) == 1)])
#         word_dict = list2dict(wordList)
#
#         while queue:
#             current_path = queue.popleft()
#             current_word = current_path[-1]
#
#             if current_word == endWord: return len(current_path) + 1
#
#             if current_word in visited: continue
#             visited.add(current_word)
#
#             for value in word_dict[current_word]:
#                 new_path = current_path + [value]
#                 queue.append(new_path)
#         return 0

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord: return length

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        beginWord, endWord, wordList = f.read().split('\n')

    solution = Solution()
    output = solution.ladderLength(beginWord, endWord, wordList)
    print(output)
