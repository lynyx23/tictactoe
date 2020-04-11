from graphics import *
import numpy as np
import math

board=np.zeros((3,3),dtype=np.int32)

# Default sizes (in px)
full_size=348
size=300
padding_size=15
div_width=9
button_width=200
button_height=67
button_center=full_size/2 #174
between_cells=size/3+div_width
first_cell=padding_size+size/6

rounds=0

# Visual elements of the menu
# Defines the window object
window = GraphWin("TicTacToe", full_size, full_size)

# Adds a black rectangle used as padding
def add_padding():
    global window

    padding=Rectangle(Point(0,0),Point(full_size,full_size))
    padding.setWidth(padding_size)
    padding.draw(window)

add_padding()

# Logo section
logo=Image(Point(button_center,75),"./assets/image.png")
logo.draw(window)

# Play and exit buttons
play_button=Image(Point(button_center,button_center),"./assets/play.png")
play_button.draw(window)
exit_button=Image(Point(button_center,250),"./assets/exit.png")
exit_button.draw(window)

# Logic of the menu
def menu():
    global window

    # Gets mouse coordinates after click
    mouse=window.getMouse()
    x=mouse.getX()
    y=mouse.getY()

    # Gets the y coordinate of the exit button's center
    exit_point=exit_button.getAnchor()
    exit_center_y=exit_point.getY()

    # Test if mouse isn't on any button
    if x<(full_size-button_width)/2 or x>(full_size+button_width)/2:
        menu()
    # Test if the mouse is on the play button
    elif y>=button_center-button_height/2 and y<=button_center+button_height/2:
        start_game()
    # Test if the mouse is on the exit button
    elif y>=exit_center_y-button_height/2 and y<=exit_center_y+button_height/2:
        window.close()
    # If x is right but y isn't (for missclicks)
    else:
        menu()

# It basically draws the green x's and o's
# If any of the parameters is -1 it will be ignored
# The one that isn't -1 will determine the line/column/diagonal that will be drawn
def win_draw(line,coll,diag):
    global window

    if line!=-1:
        # Tests if the cell is occupied by a x
        if board[line][0]==1:
            for j in range(0,3):
                # Draws the new x image
                x=Image(Point(first_cell+line*between_cells,first_cell+j*between_cells),'./assets/win_x.png')
                x.draw(window)
        # Tests if the cell is occupied by an o
        elif board[line][0]==2:
            for j in range(0,3):
                # Draws the new o image
                o=Image(Point(first_cell+line*between_cells,first_cell+j*between_cells),'./assets/win_o.png')
                o.draw(window)
    elif coll!=-1:
        # Tests if the cell is occupied by a x
        if board[0][coll]==1:
            for j in range(0,3):
                # Draws the new x image
                x=Image(Point(first_cell+j*between_cells,first_cell+coll*between_cells),'./assets/win_x.png')
                x.draw(window)
        # Tests if the cell is occupied by an o
        elif board[0][coll]==2:
            for j in range(0,3):
                # Draws the new o image
                o=Image(Point(first_cell+j*between_cells,first_cell+coll*between_cells),'./assets/win_o.png')
                o.draw(window)
    elif diag!=-1:
        # Tests if diag refers to the primary diagonal
        if diag==1:
            # Tests if the cell is occupied by a x
            if board[0][0]==1:
                for j in range(0,3):
                    # Draws the new x image
                    x=Image(Point(first_cell+j*between_cells,first_cell+j*between_cells),'./assets/win_x.png')
                    x.draw(window)
            # Tests if the cell is occupied by an o
            elif board[0][0]==2:
                for j in range(0,3):
                    # Draws the new o image
                    o=Image(Point(first_cell+j*between_cells,first_cell+j*between_cells),'./assets/win_o.png')
                    o.draw(window)
        # Tests if diag refers to the secondary diagonal
        elif diag==2:
            # Tests if the cell is occupied by a x
            if board[0][2]==1:
                for j in range(0,3):
                    # Draws the new x image
                    x=Image(Point(first_cell+(2-j)*between_cells,first_cell+j*between_cells),'./assets/win_x.png')
                    x.draw(window)
            # Tests if the cell is occupied by an o
            elif board[0][2]==2:
                for j in range(0,3):
                    # Draws the new o image
                    o=Image(Point(first_cell+(2-j)*between_cells,first_cell+j*between_cells),'./assets/win_o.png')
                    o.draw(window)

def win_test():
    global window
    global rounds

    # If statements that test if the game has already been won and calls for win_draw to draw the new images
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=0:
            win_draw(i,-1,-1)
            return 1
        elif board[0][i]==board[1][i]==board[2][i] and board[0][i]!=0:
            win_draw(-1,i,-1)
            return 1

    # Tests if the primary diagonal have the same elements
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=0:
        win_draw(-1,-1,1)
        return 1

    # Tests if the secondary diagonal have the same elements
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2]!=0:
        win_draw(-1,-1,2)
        return 1

    # Tests if the game ends in a tie
    if rounds>=9:
        # For structure going through the elements in board (the matrix)
        for i in range(0,3):
            for j in range(0,3):
                # Tests if the cell is occupied by a x
                if board[i][j]==1:
                    # Draws the new x image
                    x=Image(Point(first_cell+i*between_cells,first_cell+j*between_cells),'./assets/tie_x.png')
                    x.draw(window)
            # Tests if the cell is occupied by an o
                elif board[i][j]==2:
                    # Draws the new o image
                    o=Image(Point(first_cell+i*between_cells,first_cell+j*between_cells),'./assets/tie_o.png')
                    o.draw(window)
        return 1

# Clears the whole window
def clear():
    global window

    for item in window.items[:]:
        item.undraw()

# Preps the game board so that it can be used again
def play_again():
    global window
    global rounds
    global board

    # Clears the window and redraws the padding
    clear()
    add_padding()

    # Resets the board matrix
    board=np.zeros((3,3),dtype=np.int32)

    # Resets the round counter
    rounds=0

    start_game()

# The logic of the final menu
def end_menu_logic():
    global window

    # Gets mouse coordinates after click
    mouse=window.getMouse()
    x=mouse.getX()
    y=mouse.getY()

    # Gets the y coordinate of the exit button's center
    exit_point=exit_button.getAnchor()
    exit_center_y=exit_point.getY()

    # Test if mouse isn't on any button
    if x<(full_size-button_width)/2 or x>(full_size+button_width)/2:
        end_menu_logic()
    # Test if the mouse is on the play button
    elif y>=button_center-button_height/2 and y<=button_center+button_height/2:
        play_again()
    # Test if the mouse is on the exit button
    elif y>=exit_center_y-button_height/2 and y<=exit_center_y+button_height/2:
        return
    # If x is right but y isn't (for missclicks)
    else:
        end_menu_logic()

# Visual elements of the final menu
def end_menu():
    global window

    # The dimmed background
    bk=Image(Point(button_center,button_center),"./assets/end.png")
    bk.draw(window)

    # Logo section
    logo=Image(Point(button_center,75),"./assets/hm.png")
    logo.draw(window)

    # Play and exit buttons
    play_button=Image(Point(button_center,button_center),"./assets/play_again.png")
    play_button.draw(window)
    exit_button=Image(Point(button_center,250),"./assets/exit.png")
    exit_button.draw(window)

    end_menu_logic()

# The game logic
def game():
    global window
    global rounds

    # Testing if the game has already been won
    # If yes, then it calls for the end_menu function
    if win_test()==1:
        window.getMouse()
        end_menu()
        return
    else:
        # Getting the x and y coordinates of the mouse click
        mouse=window.getMouse()
        x=mouse.getX()
        y=mouse.getY()

        # Calculating the cell location in the game board (a matrix)
        cell_x=int(math.floor(x/116))
        cell_y=int(math.floor(y/116))

        # If the cell hasn't already been occupied
        if board[cell_x][cell_y]==0:
            rounds+=1
            # If rounds is an odd number it means it's x's turn
            if rounds%2==1:
                # Occupies the cell
                board[cell_x][cell_y]=1
                # Displays the x
                x=Image(Point(first_cell+cell_x*between_cells,first_cell+cell_y*between_cells),"./assets/drawn_x.png")
                x.draw(window)
            # If rounds is an even number it means it's o's turn
            else:
                # Occupies the cell
                board[cell_x][cell_y]=2
                # Displays the o
                o=Image(Point(first_cell+cell_x*between_cells,first_cell+cell_y*between_cells),"./assets/drawn_o.png")
                o.draw(window)
    game()

# Visual elements of the game screen
def start_game():
    global window

    clear()
    add_padding()

    # Sizes for the dividers
    div1_size=padding_size+size/3
    div2_size=padding_size+2*size/3+div_width*(3/2)

    # Creating and drawing the vertical dividers
    div1=Line(Point(div1_size,0),Point(div1_size,full_size))
    div1.setWidth(div_width)
    div1.draw(window)
    div2=Line(Point(div2_size,0),Point(div2_size,full_size))
    div2.setWidth(div_width)
    div2.draw(window)

    # Creating and drawing the horizontal dividers
    div3=Line(Point(0,div1_size),Point(full_size,div1_size))
    div3.setWidth(div_width)
    div3.draw(window)
    div4=Line(Point(0,div2_size),Point(full_size,div2_size))
    div4.setWidth(div_width)
    div4.draw(window)

    game()

menu()
