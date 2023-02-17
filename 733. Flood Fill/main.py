class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        else:
            m = len(image) # row in 0..m-1
            n = len(image[0])
            default_color = image[sr][sc]
            frontier = list()
            frontier.append([sr, sc])
            while len(frontier) != 0:
                coordinate = frontier.pop()
                row = coordinate[0]
                col = coordinate[1]
                image[row][col] = color
                if row < m-1:
                    if image[row+1][col] == default_color:
                        frontier.append([row+1, col])
                if row > 0:
                    if image[row-1][col] == default_color:
                        image[row-1][col] = color
                        frontier.append([row-1, col])
                if col < n-1:
                    if image[row][col+1] == default_color:
                        frontier.append([row][col+1])
                if col > 0:
                    if image[row][col-1] == default_color:
                        frontier.append([row, col-1])
        return image