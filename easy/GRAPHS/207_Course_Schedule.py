"""207. Course Schedule"""


class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graphs: dict[int, list[int]] = {}
        count: list[int] = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graphs[b] = graphs.get(b, [])
            graphs[b].append(a)
            count[a] += 1

        queue = [i for i in range(numCourses) if count[i] != 0]
        visited = 0

        while queue:
            course = queue.pop(0)
            visited += 1

            for next_course in graphs.get(course, []):
                count[next_course] -= 1
                if count[next_course] == 0:
                    queue.append(next_course)

        return visited == numCourses
