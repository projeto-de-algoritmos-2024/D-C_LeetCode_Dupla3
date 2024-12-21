class Solution:
    def getSkyline(self, buildings):
        return self.divideAndConquer(buildings)
    
    def divideAndConquer(self, buildings):
        if not buildings:
            return []
        if len(buildings) == 1:
            start, end, height = buildings[0]
            return [[start, height], [end, 0]]
        
        mid = len(buildings) // 2
        left_skyline = self.divideAndConquer(buildings[:mid])
        right_skyline = self.divideAndConquer(buildings[mid:])

        return self.mergeSkylines(left_skyline, right_skyline)
    
    
    def mergeSkylines(self, left, right):
        h1 = h2 = 0
        i = j = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                x, h2 = right[j]
                j += 1
            else:
                x = left[i][0]
                h1 = left[i][1]
                h2 = right[j][1]
                i += 1
                j += 1
            
            max_height = max(h1, h2)

            if not merged or merged[-1][1] != max_height:
                merged.append([x, max_height])

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


