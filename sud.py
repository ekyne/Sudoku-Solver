## Author: 	Kyle Gilmore
## Date: 	March 18, 2022
## Project:	Sudoku Solver
## File: 	sud.py
## Function: 	Main Driver of the Sudoku Solver Project.

try:
    import pygame
    import time
except:
    import install_requirements
    import pygame
    import time

## class which represents each cell in the grid matrix
class Square:
    def __init__(self,i,j,n):
        self.i = i
        self.j = j
        self.select = False
        self.keyed = False
        self.val = n
        self.keyedVal = 0
        self.automated = True
   
    ## if a number is entered in the selected cell, it will color the number in grey, else the cell will remain blank
    def enterNumber(self, grid, i, j):
        self.keyed = True
        if grid[i][j].keyedVal != 0:
            screen.fill((white),(85 + (70 * j) + 3,85 + (70 * i) + 3,64,64))
            screen.blit(pygame.font.Font.render(font, str(grid[i][j].keyedVal) ,True,(123,123,123)),(86 + (70 * j) + 25, 85 + (70 * i) + 25))
        elif grid[i][j].keyedVal == 0 and grid[i][j].val == 0:
            screen.fill((white),(85 + (70 * j) + 3,85 + (70 * i) + 3,64,64))
        pygame.display.update()

    ## if a number entered in the selected cell and is not zero, the number will be colored in black, else the cell will remain blank
    def printNumber(self, grid, i, j):
        if grid[i][j].val != 0:
            grid[i][j].keyedVal = 0
            ##screen.fill((white),(85 + (70 * j) + 3,85 + (70 * i) + 3,64,64))
            screen.blit(pygame.font.Font.render(font, str(grid[i][j].val) ,True,(0,0,0)),(85 + (70 * j) + 25,85 + (70 * i) + 25))
        else:
            screen.fill((white),(85 + (70 * j) + 3,85 + (70 * i) + 3,64,64))
        pygame.display.update()

    ## lights up the cell that is selected in green
    def lightUp(self,grid,i,j):
        if grid[i][j].select == False:
            pygame.draw.rect(screen,(0,255,0),(85 + (j*70)+3,85 +(i*70)+3,64,64),1)
            grid[i][j].select = True
            pygame.display.update()

    ## reverts the lighting of the previously selected cell
    def lightDown(self,grid,i,j):
        if grid[i][j].select == True:
            pygame.draw.rect(screen,(white),(85 + (j*70)+3,85 +(i*70)+3,64,64),1)
            grid[i][j].select = False
            pygame.display.update()

## creates the layout of the sudoku puzzle
def draw():
    screen.fill(white)

    pygame.draw.line(screen,(0,0,0),[295,85],[295,715],3)
    pygame.draw.line(screen,(0,0,0),[505,85],[505,715],3)
    pygame.draw.line(screen,(0,0,0),[85,295],[715,295],3)
    pygame.draw.line(screen,(0,0,0),[85,505],[715,505],3)

    pygame.draw.line(screen,(0,0,0),[25,800],[775,800],3)

    pygame.draw.line(screen,(0,0,0),[85,85],[85,715],2)
    pygame.draw.line(screen,(0,0,0),[155,85],[155,715])
    pygame.draw.line(screen,(0,0,0),[225,85],[225,715])
    pygame.draw.line(screen,(0,0,0),[365,85],[365,715])
    pygame.draw.line(screen,(0,0,0),[435,85],[435,715])
    pygame.draw.line(screen,(0,0,0),[575,85],[575,715])
    pygame.draw.line(screen,(0,0,0),[645,85],[645,715])
    pygame.draw.line(screen,(0,0,0),[715,85],[715,715])

    pygame.draw.line(screen,(0,0,0),[85,85],[715,85])
    pygame.draw.line(screen,(0,0,0),[85,155],[715,155])
    pygame.draw.line(screen,(0,0,0),[85,225],[715,225])
    pygame.draw.line(screen,(0,0,0),[85,365],[715,365])
    pygame.draw.line(screen,(0,0,0),[85,435],[715,435])
    pygame.draw.line(screen,(0,0,0),[85,575],[715,575])
    pygame.draw.line(screen,(0,0,0),[85,645],[715,645])
    pygame.draw.line(screen,(0,0,0),[85,715],[715,715])
    screen.blit(pygame.font.Font.render(font, "Strikes:" ,True,(0,0,0)),(100,825))
    screen.blit(pygame.font.Font.render(font,"Time: ",True,(0,0,0)),(550,825))
    pygame.display.update()

## returns true if a puzzle is solved, else false
def isFilled(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].val == 0:
                return False
    return True

## if the selected position is not valid, increment a strike
def enteredPosition(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].keyed == True:
                n = grid[i][j].keyedVal
                if selectPosition(grid,i,j,n):
                    grid[i][j].printNumber(grid,i,j)
                else:
                    count = count + 1
                grid[i][j].keyed = False
    return count

## if the selected position is valid, return true, else return false
def validPosition(grid,y,x,n):
    cellX = x // 3
    cellY = y // 3
    for i in range(9):
        if grid[y][i].val == n: 
            return False
        if grid[i][x].val == n: 
            return False
    for i in range(cellY*3,(cellY*3)+3):
        for j in range(cellX*3,(cellX*3)+3):
            if grid[i][j].val == n:
                return False
    return True

## if the selected position is valid, the number is printed to the cell
def selectPosition(grid, i, j, n):
    if(validPosition(grid,i,j,n)):
        grid[i][j].val = n
        screen.fill((white),(85 + (70 * j) + 3,85 + (70 * i) + 3,64,64))
        screen.blit(pygame.font.Font.render(font, str(grid[i][j].val) ,True,(0,0,0)),(85 + (70 * j) + 25,85 + (70 * i) + 25))
        return True
    else:
        screen.fill((white),(85 + (70 * j) + 3,85 + (70 * i) + 3,64,64))
        if grid[i][j].val != 0:
            screen.blit(pygame.font.Font.render(font, str(grid[i][j].val) ,True,(0,0,0)),(85 + (70 * j) + 25,85 + (70 * i) + 25))
        return False

## the sudoku puzzle is initialized
def initializeGrid(font,screen):
    grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7]]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = Square(i,j,grid[i][j])
            grid[i][j].printNumber(grid,i,j)
            if grid[i][j].val != 0:
                grid[i][j].automated = False
 
    return grid

## performs the automation to find the solution for the puzzle using backtracking
def automate(grid,i,j):
    if i == 8 and j == 8:
        return True
    if grid[i][j].val != 0:
        if j == 8:
            if automate(grid,i+1,0):
                return True
        else:
            if automate(grid,i,j+1):
                return True
        return False
    else:
        for num in range(9):
            if j == 8:
                if(validPosition(grid,i,j,num+1)):
                    grid[i][j].val = num+1
                    grid[i][j].printNumber(grid,i,j)
                    if automate(grid,i+1,0):
                        return True
                    else:
                        grid[i][j].val = 0
                        grid[i][j].printNumber(grid,i,j)
            else:
                if(validPosition(grid,i,j,num+1)):
                    grid[i][j].val = num+1
                    grid[i][j].printNumber(grid,i,j)
                    if automate(grid,i,j+1):
                        return True
                    else:
                        grid[i][j].val = 0
                        grid[i][j].printNumber(grid,i,j)
        return False

## main function of the program
def main():
    otherX = -1
    otherY = -1
    passed = 0
    minutes = 0
    strikes = ""
    
    draw()
    count = 0
    autoCount = 3;
    pressed = False
    validPress = False
    grid = initializeGrid(font,screen)
    print("")
    print("Welcome to the Sudoku Solver!")
    print("")
    print("Select a cell and use the number keys to select a number")
    print("Press ENTER when you have made your selection.")
    print("Press DELETE if you want to delete a number from the puzzle.")
    print("Press Y if you want the puzzle solution to be automated.")
    print("Press Q if you want to quit the program.")
    print("")
    startTime = pygame.time.get_ticks()
    while True:

        ##if the puzzle is filled, the game is won
        if isFilled(grid):
            print("")
            print("Success! The Puzzle is solved!")
            time.sleep(5)
            exit()
        screen.blit(pygame.font.Font.render(font, strikes ,True,(255,0,0)),(250,825))
        passed = pygame.time.get_ticks() - startTime
        screen.fill((white),(650,825,100,50))

        ## the timer is set here
        text = pygame.font.Font.render(font, str(minutes) + ":{:02d}".format(passed//1000), True,(0,0,0))
        screen.blit(text,(650,825))
        pygame.display.update()
        clock.tick()
        if passed//1000 > 59:
            startTime = pygame.time.get_ticks()
            minutes = minutes + 1
        if minutes > 10:
            print("Time is up!")
            exit()

        ## if the strikes increment to at least 3, the game is lost
        if len(strikes) > 2:
            print("Game over.")
            exit()

        ## mouse and key events are acted upon here
        ev = pygame.event.get()
        for event in ev:
            validPress = True
            ## if a mousebutton is pressed over a cell, the coordinates of the cell are retrieved and the cell lights up
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                if coords[0] > 85 and coords[0] < 715 and coords[1] > 85 and coords[1] < 715:
                    x = (coords[0] - 85) // 70
                    y = (coords[1] - 85) // 70
                    if grid[y][x] != grid[otherY][otherX]:
                        grid[otherY][otherX].lightDown(grid,otherY,otherX)
                    grid[y][x].lightUp(grid,y,x)
                    otherY = y
                    otherX = x
                    pressed = True

            ## if a number key is pressed, the number is entered into the cell before validation
            if event.type == pygame.KEYDOWN and (pressed == True or validPress == True):

                ## if automation attempts are remaining, it is computed
                if event.key == pygame.K_y and validPress == True:
                    if autoCount > 0:
                        if not automate(grid,0,0):
                            autoCount = autoCount - 1
                            if(autoCount == 0):
                                print("No automation attempts are remaining.")
                                print("")
                            else:
                                print("Only " + str(autoCount) + " automation attempts are left.")
                                print("")
                if event.key == pygame.K_1:
                    grid[y][x].keyedVal = 1
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_2:
                    grid[y][x].keyedVal = 2
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_3:
                    grid[y][x].keyedVal = 3
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_4:
                    grid[y][x].keyedVal = 4
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_5:
                    grid[y][x].keyedVal = 5
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_6:
                    grid[y][x].keyedVal = 6
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_7:
                    grid[y][x].keyedVal = 7
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_8:
                    grid[y][x].keyedVal = 8
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_9:
                    grid[y][x].keyedVal = 9
                    grid[y][x].enterNumber(grid,y,x)
                if event.key == pygame.K_q and validPress == True:
                    exit()
                if event.key == pygame.K_DELETE:
                    grid[y][x].val = 0
                    grid[y][x].keyedVal = 0
                    grid[y][x].enterNumber(grid,y,x)

                ## if the enter button is pressed and the entered numbers are not valid, strikes will be incremented here
                if event.key == pygame.K_RETURN:
                    anX = enteredPosition(grid)
                    while anX != 0:
                        strikes = strikes + "X"
                        anX = anX - 1

pygame.init()

## screen display is set here
screen = pygame.display.set_mode((800,900))

##white color is set here
white = (255, 255, 255)

##clock is set here
clock = pygame.time.Clock()

##font of the text is set here
font = pygame.font.Font(pygame.font.get_default_font(), 36)

main()
