# https://leetcode.com/problems/perfect-rectangle
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0

        for rec in rectangles:
            bottom_left = (rec[0], rec[1])
            top_right = (rec[2], rec[3])
            top_left = (rec[0], rec[3])
            bottom_right = (rec[2], rec[1])

            area += (rec[2] - rec[0]) * (rec[3] - rec[1])

            for i in [top_left, top_right, bottom_left, bottom_right]:
                if i not in corners:
                    corners.add(i)
                else:
                    corners.remove(i)

        if len(corners) != 4:
            return False

        corners = sorted(corners)
        first = corners.pop(0)
        last = corners.pop()

        wholeArea = (last[0] - first[0]) * (last[1] - first[1])

        return area == wholeArea