import board
import random


class Strategy:
    def make_turn(self):
        raise NotImplementedError("You need to implement this")


class CpuRandomStrategy(Strategy):
    def make_turn(self):
        cpu_choice = random.choice(list(board.POSSIBLE_NUMBERS))
        print("\nCpu choice: ", cpu_choice)
        if cpu_choice in board.POSSIBLE_NUMBERS:
            board.modify_array(cpu_choice, 'O')
            board.POSSIBLE_NUMBERS.remove(cpu_choice)


class CpuBetterStrategy(Strategy):
    def check_for_winning_move(self, symbol):
        """Check the board to see if there's a winning move available for the given
    symbol.

    If there's a winning move return the number corresponding to it.
    Returns None if there's no winning move.

    symbol - either an X or a O
    """
        # Check to see if there's a complete row
        for row in range(0, 3):
            symbol_count = 0
            empty_col_index = None
            for col in range(0, 3):
                if board.board[row][col] == symbol:
                    symbol_count += 1
                elif board.board[row][col] in range(0, 10):
                    empty_col_index = board.board[row][col]
            if symbol_count == 2:
                # We have a winning move!
                return empty_col_index

        # Now do the same for a winning column.
        for col in range(0, 3):
            symbol_count = 0
            empty_col_index = None
            for row in range(0, 3):
                if board.board[row][col] == symbol:
                    symbol_count += 1
                elif board.board[row][col] in range(0, 10):
                    empty_col_index = board.board[row][col]
            if symbol_count == 2:
                # We have a winning move!
                return empty_col_index
        # (Ahmed): Implement the diagonal check.
        symbol = board[1][1]
        if (symbol in ['X', 'O'] and board[0][0] == symbol and board[2][2] == symbol):
          return symbol
        elif (symbol in ['X', 'O'] and board[0][2] == symbol and board[2][0] == symbol):
          return symbol
        return None

        """
    # Cross wins
    symbol = board[1][1]
    if (symbol in ['X', 'O'] and board[0][0] == symbol and board[2][2] == symbol):
      return symbol
    elif (symbol in ['X', 'O'] and board[0][2] == symbol and board[2][0] == symbol):
      return symbol

    # board is full
    for row in range(0, 3):
      for collom in range(0, 3):
        symbol = board[row][collom]
        # print(f"Symbol: {symbol}")
        if symbol not in ['X', 'O']:
          return None
    return "N"
    """

    def make_turn(self):
        cpu_choice = random.choice(list(board.POSSIBLE_NUMBERS))
        # Check for a winning move
        winning_move = self.check_for_winning_move("O")
        if winning_move:
            print("We spotted a winning move!")
            cpu_choice = winning_move

        # (Ahmed): if there's no winning move - check to see if you can
        # block the human.
        for row in range(0, 3):
            for col in range(0, 3):
                symbol = self[row][col]
                # print(f"Symbol: {symbol}")
                if symbol not in ['X', 'O']:
                    return None
        return "N"

        print("\nCpu choice: ", cpu_choice)
        if cpu_choice in board.POSSIBLE_NUMBERS:
            board.modify_array(cpu_choice, 'O')
            board.POSSIBLE_NUMBERS.remove(cpu_choice)
