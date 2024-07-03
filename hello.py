import pygame

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.name


class Board:
    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}

    def display_board(self):
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])

    def update_board(self, position, symbol):
        self.board[position] = symbol

    def is_position_available(self, position):
        return self.board[position] == ' '


class GameState:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player = self.players[0]
        self.game_over = False

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def check_winner(self):
        b = self.board.board
        winning_conditions = [
            (b['7'], b['8'], b['9']),  # across the top
            (b['4'], b['5'], b['6']),  # across the middle
            (b['1'], b['2'], b['3']),  # across the bottom
            (b['7'], b['4'], b['1']),  # down the left side
            (b['8'], b['5'], b['2']),  # down the middle
            (b['9'], b['6'], b['3']),  # down the right side
            (b['7'], b['5'], b['3']),  # diagonal
            (b['1'], b['5'], b['9'])   # diagonal
        ]
        for condition in winning_conditions:
            if condition[0] == condition[1] == condition[2] != ' ':
                self.game_over = True
                return True
        return False

    def check_tie(self):
        for position in self.board.board.values():
            if position == ' ':
                return False
        self.game_over = True
        return True


class Game:
    def __init__(self):
        self.game_state = GameState()
        # Initialize Pygame
        pygame.init()
        # Set window size
        self.window_size = 300
        # Set number of rows and columns for the game board
        self.rows = 3
        self.cols = 3
        # Create game window
        self.game_window = pygame.display.set_mode((self.window_size, self.window_size))
        # Set font for displaying player symbols
        self.font = pygame.font.Font(None, 74)
        # Set font for displaying game result
        self.result_font = pygame.font.Font(None, 50)
        # Calculate grid size based on window size and number of rows/columns
        self.grid_size = self.window_size // self.rows
        # Variable to store the game result message
        self.game_result = None

    def draw_grid(self):
        for i in range(1, self.rows):
            pygame.draw.line(self.game_window, (0, 0, 0), (0, i * self.grid_size), (self.window_size, i * self.grid_size), 3)
            pygame.draw.line(self.game_window, (0, 0, 0), (i * self.grid_size, 0), (i * self.grid_size, self.window_size), 3)

    def handle_mouse_press(self, x, y):
        if 0 < x < self.grid_size:
            if 0 < y < self.grid_size:
                print('7')
            elif self.grid_size < y < 2 * self.grid_size:
                print('4')
            elif self.grid_size * 2 < y < self.grid_size * 3:
                print('1')  
        elif self.grid_size < x < 2 * self.grid_size:
            if 0 < y < self.grid_size:
                print('8')
            elif self.grid_size < y < 2 * self.grid_size:
                print('5')
            elif self.grid_size * 2 < y < self.grid_size * 3:
                print('2')
        elif 2 * self.grid_size < x < 3 * self.grid_size:
            if 0 < y < self.grid_size:
                print('9')
            elif self.grid_size < y < 2 * self.grid_size:
                print('6')
            elif self.grid_size * 2 < y < self.grid_size * 3:
                print('3')

    def play(self):
        while not self.game_state.game_over:
            self.game_window.fill((255, 255, 255))  # Clear the screen
            self.draw_grid()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.handle_mouse_press(x, y)
        pygame.quit()
        #     self.game_state.board.display_board()
        #     print(f"It's your turn, {self.game_state.current_player} - Move to which place?")
        #     move = input()
        #
        #     if move in self.game_state.board.board.keys() and self.game_state.board.is_position_available(move):
        #         self.game_state.board.update_board(move, self.game_state.current_player.symbol)
        #
        #         if self.game_state.check_winner():
        #             self.game_state.board.display_board()
        #             print(f"\nGame Over.\n{self.game_state.current_player} won.")
        #
        #         if self.game_state.check_tie():
        #             self.game_state.board.display_board()
        #             print("\nGame Over.\nIt's a Tie!!")
        #
        #         self.game_state.switch_player()
        #     else:
        #         print("Invalid move. Try again.")
        #
        # restart = input("Do you want to play Again? (y/n)")
        # if restart.lower() == "y":
        #     self.game_state = GameState()
        #     self.play()


if __name__ == "__main__":
    game = Game()
    game.play()