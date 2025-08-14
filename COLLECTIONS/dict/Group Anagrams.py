"""https://leetcode.com/problems/group-anagrams/description/"""


class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups_words: dict[tuple[int, ...], list[str]] = {}

        for word in strs:
            counter = [0] * 26

            for letter in word:
                counter[ord(letter) - ord("a")] += 1  # ORD важная команда

            key = tuple(counter)

            groups_words.setdefault(key, []).append(word)

        return list(groups_words.values())
