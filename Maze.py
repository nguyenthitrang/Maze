# class maze
class Maze:
    def __init__(self):
        self.maze = [
            [[0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 0, 1, 1]],
            [[1, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0]],
            [[1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1]],
            [[0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 0, 1, 1], [0, 0, 1, 0]],
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1]],
            [[0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0], [1, 0, 1, 0]],
            [[1, 0, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1], [1, 0, 0, 1]],
            [[1, 1, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1]],
            [[0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 0]],
            [[1, 1, 0, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1], [1, 0, 0, 1], [1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 1]]
        ]

        self.outPos = [9,5]
        self.inPos = [0,4]
        self.mappingDes = {
            0: "Close",
            1: "Open"
        }
        self.mappingDir = {
            0: ["Top", "t"],
            1: ["Right", "r"],
            2: ["Bottom", "b"],
            3: ["Left", "l"]
        }

    def getOutp(self):
        return self.outPos

    def getInp(self):
        return self.inPos

    def getPosVal(self, curPos):
        value = self.maze[curPos[0]][curPos[1]]
        return value

    def getDes(self, curPosVal):
        posibleMove = []
        for i, v in enumerate(curPosVal):
            if v == 1:
                posibleMove.append(self.mappingDir[i][-1])
            print "%s: %s" % (self.mappingDir[i][0], self.mappingDes[v])
        return posibleMove

    def checkPos(self, curPos):
        if curPos == self.outPos:
            return True
        else:
            return False


# class player
class Player:
    def __init__(self, curPos, prePos):
        self.curPos = curPos
        self.prePos = prePos

    def moveTop(self):
        self.prePos = self.curPos
        self.curPos[0] -= 1

    def moveRight(self):
        self.prePos = self.curPos
        self.curPos[1] += 1

    def moveBot(self):
        self.prePos = self.curPos
        self.curPos[0] += 1

    def moveLeft(self):
        self.prePos = self.curPos
        self.curPos[1] -= 1

def getNextPos(maze, curPos):
    val = maze.getPosVal(curPos)  # 0110
    nextPos = []
    for i in range(4):
        if val[i] == 1:
            if i == 0: nextPos.append([curPos[0] - 1, curPos[1]])
            if i == 1: nextPos.append([curPos[0], curPos[1] + 1])
            if i == 2: nextPos.append([curPos[0] + 1, curPos[1]])
            if i == 3: nextPos.append([curPos[0], curPos[1] - 1])
    return nextPos


def correctPath(maze, curPos, visitPos):
    # bien flag: False loi sai, True loi dung hoac chua di qua
    flag = []
    for i in range(100):
        flag.append(True)

    corPath = [curPos]
    while corPath[-1] != visitPos:
    # tim o tiep theo: findPath
        nextPos = findPath(maze, corPath[-1], corPath, flag)
    # them o tiep theo
        corPath.append(nextPos)
    # xoa duong cut: checkPath
        corPath = delPath(maze, corPath, visitPos, flag)
    return corPath

def findPath(maze, curPos, corPath, flag):
    nextPos = getNextPos(maze, curPos)
    for i in range(len(nextPos)):
        index = nextPos[i][0]*10 + nextPos[i][1]
        if flag[index] == True and nextPos[i] not in corPath:
            return nextPos[i]

def delPath(maze, corPath, visitPos, flag):
    # khi corPath[-1] khong la duong cut nua thi dung
    while not checkPath(maze, corPath, visitPos, flag):
        index = corPath[-1][0] * 10 + corPath[-1][1]
        flag[index] = False
        del corPath[-1]
    return corPath

def checkPath(maze, corPath, visitPos, flag):
    # True: di tiep duoc
    nextPos = getNextPos(maze, corPath[-1])
    for i in range(len(nextPos)):
        index = nextPos[i][0] * 10 + nextPos[i][1]
        if flag[index] == True and nextPos[i] not in corPath or corPath[-1] == visitPos:
            return True
    return False

def play(player, maze):
    playerInputMapping = {
        "t": player.moveTop,
        "r": player.moveRight,
        "b": player.moveBot,
        "l": player.moveLeft
    }
    printMaze(maze, player)
    if maze.checkPos(player.curPos):
        print "Congratulation: You passed the Maze."
        return
    print "Possible Direction:"
    possibleMove = maze.getDes(maze.getPosVal(player.curPos))
    print "Choose Direction: (t: top, r: right, b: )"

    input = raw_input("t/r/b/l to move top/right/bottom/left: ")
    while input not in possibleMove:
        input = raw_input("t/r/b/l to move top/right/bottom/left: ")
    playerInputMapping[input]()
    play(player, maze)

def printMaze(maze, path):
    s = " ___ ___ ___ ___ _o_ ___ ___ ___ ___ ___\n"
    for i in range(0,10):
        for j in range(0,10):
            if maze.getPosVal([i,j])[3] == 1:
                s += ' '
            else:
                s += '|'
            if maze.getPosVal([i,j])[2] == 1:
                if [i,j] in path:
                    s += ' + '
                else:
                    s += '   '
            elif [i,j] == [9,5]:
                s += '_x_'
            elif [i,j] in path:
                s += '_+_'
            else:
                s += '___'

        s += '|\n'
    print s

if __name__ == "__main__":
    print "Hello Player!"
    maze = Maze()
    player = Player(maze.getInp(), [])
    for i in range(100):
        print i
        print correctPath(maze, player.curPos, [i/10,i%10])
        printMaze(maze, correctPath(maze, player.curPos, [i/10,i%10]))

