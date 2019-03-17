# Time:  O(n)
# Space: O(1)

# Ideas:
# interval intersect in both dimension


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # x, y axis
        rect1 = [sorted([A, C]), sorted([B, D])]
        rect2 = [sorted([E, G]), sorted([F, H])]

        itersect_area, area1, area2 = 1, 1, 1
        for p1, p2 in zip(rect1, rect2):
            area1 *= p1[1] - p1[0]
            area2 *= p2[1] - p2[0]
            left = max(p1[0], p2[0])
            right = min(p1[1], p2[1])
            itersect_area *= max(0, right - left)

        return area1 + area2 - itersect_area
