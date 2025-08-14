"""
49. Group Anagrams
"""


class Solution(object):
    def groupAnagrams(self, strs: list[str]):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups_words: dict[tuple[int, ...], list[str]] = {}

        for word in strs:
            counter: list[int] = [0] * 26

            for letter in word:
                counter[ord(letter) - ord("a")] += 1

            key = tuple(counter)

            groups_words.setdefault(key, []).append(word)

        return groups_words.values()


if __name__ == "__main__":
    solution = Solution()
    strs = list(map(str, input().split()))
    print(solution.groupAnagrams(strs))

"""
eat tea tan ate nat bat
bdddddddddd bbbbbbbbbbc
abbbbbbbbbbb aaaaaaaaaaab
"""
