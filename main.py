import kivy
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('tictactoe.kv')

    turn = 'O'
    is_win = False
    is_draw = False
    game_count = 1
    board = {}

    def draw(self):
        if self.is_win == False and \
                self.root.ids.btn1.disabled == True and \
                self.root.ids.btn2.disabled == True and \
                self.root.ids.btn3.disabled == True and \
                self.root.ids.btn4.disabled == True and \
                self.root.ids.btn5.disabled == True and \
                self.root.ids.btn6.disabled == True and \
                self.root.ids.btn7.disabled == True and \
                self.root.ids.btn8.disabled == True and \
                self.root.ids.btn9.disabled == True:
            self.root.ids.score.text = "It's a tie"
            self.is_draw = True

    def disable_all_buttons(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def end_game(self, a, b, c):
        self.is_win = True
        a.color = 'red'
        b.color = 'red'
        c.color = 'red'
        self.disable_all_buttons()
        if a.text == 'X':
            self.root.ids.score.text = 'Uff.. is that all you got?!!'

    def win(self):
        if self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn1.text == self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

        if self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn1.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

        if self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn1.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        if self.root.ids.btn2.text != '' and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn2.text == self.root.ids.btn8.text:
            self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

        if self.root.ids.btn3.text != '' and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn3.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

        if self.root.ids.btn4.text != '' and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn4.text == self.root.ids.btn6.text:
            self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

        if self.root.ids.btn7.text != '' and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn7.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

        if self.root.ids.btn3.text != '' and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn3.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

    def pressed(self, btn):
        board = {
            1: self.root.ids.btn1,
            2: self.root.ids.btn2,
            3: self.root.ids.btn3,
            4: self.root.ids.btn4,
            5: self.root.ids.btn5,
            6: self.root.ids.btn6,
            7: self.root.ids.btn7,
            8: self.root.ids.btn8,
            9: self.root.ids.btn9
        }
        if self.turn == 'X':
            btn.text = 'X'
            btn.disabled = True
            self.root.ids.score.text = "Your Turn"
            self.turn = 'O'
        else:
            btn.text = 'O'
            btn.disabled = True
            self.root.ids.score.text = "My Turn"
            self.turn = 'X'
            self.draw()
            if self.is_draw == False:
                self.pressed(board[self.computer_move()])

        self.win()
        self.draw()

    def restart(self):
        self.turn = 'O'
        self.root.ids.score.text = "Try to win against me!"
        self.is_draw = False
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False
        self.root.ids.btn1.text = ''
        self.root.ids.btn2.text = ''
        self.root.ids.btn3.text = ''
        self.root.ids.btn4.text = ''
        self.root.ids.btn5.text = ''
        self.root.ids.btn6.text = ''
        self.root.ids.btn7.text = ''
        self.root.ids.btn8.text = ''
        self.root.ids.btn9.text = ''
        self.root.ids.btn1.color = 'green'
        self.root.ids.btn2.color = 'green'
        self.root.ids.btn3.color = 'green'
        self.root.ids.btn4.color = 'green'
        self.root.ids.btn5.color = 'green'
        self.root.ids.btn6.color = 'green'
        self.root.ids.btn7.color = 'green'
        self.root.ids.btn8.color = 'green'
        self.root.ids.btn9.color = 'green'

    player = 'O'
    computer = 'X'

    def computer_move(self):
        board = {
            1: self.root.ids.btn1.text,
            2: self.root.ids.btn2.text,
            3: self.root.ids.btn3.text,
            4: self.root.ids.btn4.text,
            5: self.root.ids.btn5.text,
            6: self.root.ids.btn6.text,
            7: self.root.ids.btn7.text,
            8: self.root.ids.btn8.text,
            9: self.root.ids.btn9.text
        }

        def is_win():
            if board[1] == board[2] and board[1] == board[3] and board[1] != '':
                return board[1]
            elif board[4] == board[5] and board[4] == board[6] and board[4] != '':
                return board[4]
            elif board[7] == board[8] and board[7] == board[9] and board[7] != '':
                return board[7]
            elif board[1] == board[4] and board[1] == board[7] and board[1] != '':
                return board[1]
            elif board[2] == board[5] and board[2] == board[8] and board[2] != '':
                return board[2]
            elif board[3] == board[6] and board[3] == board[9] and board[3] != '':
                return board[3]
            elif board[1] == board[5] and board[1] == board[9] and board[1] != '':
                return board[1]
            elif board[7] == board[5] and board[7] == board[3] and board[7] != '':
                return board[7]
            else:
                return False

        def is_draw():
            for key in board.keys():
                if board[key] == '':
                    return False
            return True

        def minimax(board, is_maximizing):
            if is_win() == 'X':
                return 1
            elif is_win() == 'O':
                return -1
            elif is_draw():
                return 0
            if is_maximizing:
                best_score = -2
                for key in board.keys():
                    if board[key] == '':
                        board[key] = self.computer
                        score = minimax(board, False)
                        board[key] = ''
                        if score > best_score:
                            best_score = score
                return best_score
            else:
                best_score = 2
                for key in board.keys():
                    if board[key] == '':
                        board[key] = self.player
                        score = minimax(board, True)
                        board[key] = ''
                        if score < best_score:
                            best_score = score
                return best_score

        best_score = -800
        best_move = 0
        for key in board.keys():
            if board[key] == '':
                board[key] = self.computer
                score = minimax(board, False)
                board[key] = ''
                if score > best_score:
                    best_score = score
                    best_move = key
        return best_move


MainApp().run()
