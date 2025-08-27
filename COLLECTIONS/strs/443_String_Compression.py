class Solution(object):
    def compress(self, chars: list[str]):
        """
        :type chars: List[str]
        :rtype: int
        """

        if not chars:
            return [str]

        read = 0
        write = 0

        n = len(chars)

        while read < len(chars):
            count = 0
            cur_char = chars[read]

            while read < n and cur_char == chars[read]:
                count += 1
                read += 1

            chars[write] = cur_char
            write += 1

            if count > 1:
                for ch in str(count):
                    chars[write] = ch
                    write += 1

        return write


if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))
