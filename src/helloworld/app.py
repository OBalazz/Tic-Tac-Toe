"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class tictactoe(toga.App):

    def startup(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.player = 'X'

        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        #Játéktér felépítése
        for i in range(3):
            row_box = toga.Box(style=Pack(direction=ROW))

            for j in range(3):
                button = toga.Button('', on_press=self.button_pressed, style=Pack(flex=1, height=100, font_size=30), id=f'{i}{j}')
                row_box.add(button)

            self.main_box.add(row_box)

        self.main_window = toga.MainWindow(title='Tic-Tac-Toe', size=(300, 300))
        self.main_window.content = self.main_box
        self.main_window.show()
        #Gombnyomásra ellenőrzi, hogy nyert e valaki, vagy döntetlen
    def button_pressed(self, widget):
        if widget.text == '':
            widget.text = self.player
            i, j = int(widget.id[0]), int(widget.id[1])
            self.board[i][j] = self.player
            
            if self.check_win(self.player):
                result_label = toga.Label(f'{self.player} wins!', style=Pack(padding=10))
                rematch_button = toga.Button('Rematch', on_press=self.rematch_button_pressed, style=Pack(flex=1,padding=10))

                end_game_box = toga.Box(style=Pack(direction=COLUMN, alignment="center"))
                end_game_box.add(result_label)
                end_game_box.add(rematch_button)

                self.main_window.content = end_game_box
            elif self.check_draw():
                result_label = toga.Label('Draw!', style=Pack(padding=10,alignment="center"))
                rematch_button = toga.Button('Rematch', on_press=self.rematch_button_pressed, style=Pack(flex=1,padding=10))

                end_game_box = toga.Box(style=Pack(direction=COLUMN, alignment="center"))
                end_game_box.add(result_label)
                end_game_box.add(rematch_button)

                self.main_window.content = end_game_box

            self.player = 'O' if self.player == 'X' else 'X'
    #nyert e bárki
    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False
    
    #döntetlen e
    def check_draw(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))

    #játék újraindítása
    def rematch_button_pressed(self, widget):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        for row_box in self.main_box.children:
            for button in row_box.children:
                button.text = ''
        self.main_window.content = self.main_box

def main():
    return tictactoe()
