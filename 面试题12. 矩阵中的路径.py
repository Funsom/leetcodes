class Solution:
    def exist(self, board, word: str) -> bool:
        def search(x,y,index,visited):
            if board[x][y] == word[index]:
                visited.add((x,y))
                index += 1
                print(x,y,word[:index],visited)
                flag = False
                if index == lens:
                    return True
                if  x < row-1 and (x+1,y) not in visited:
                    flag = search(x+1,y,index,visited)
                    if flag: return True
                    
                if  x > 0 and (x-1,y) not in visited:
                    flag = search(x-1,y,index,visited)
                    if flag: return True
                    
                if  y < col-1 and (x,y+1) not in visited:
                    flag = search(x,y+1,index,visited)
                    if flag: return True
                    
                if  y > 0 and (x,y-1) not in visited:
                    flag = search(x,y-1,index,visited)
                    if flag: return True
                visited.remove((x,y))
            else:
                return False

        row = len(board)
        col = len(board[0])
        lens = len(word)
        for i in range(row):
            for j in range(col):
                
                if search(i,j,0,set()):
                    return True
        return False

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]

    word = "ABCESEEEFS"
    s = Solution()
    print(s.exist(board,word))