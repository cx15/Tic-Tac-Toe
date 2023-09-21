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
            board.modify_board(cpu_choice, 'O')
            board.POSSIBLE_NUMBERS.remove(cpu_choice)


class CpuBetterStrategy(Strategy):
    def check_for_winning_move(
        self, board_to_check: board.Board, symbol: str):
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
                if board_to_check.get_symbol(row, col) == symbol:
                    symbol_count += 1
                elif board_to_check.get_symbol(row, col) in range(0, 10):
                    empty_col_index = board_to_check.get_symbol(
                        col=col, row=row)
            if symbol_count == 2:
                # We have a winning move!
                return empty_col_index

        # Now do the same for a winning column.
        for col in range(0, 3):
            symbol_count = 0
            empty_col_index = None
            for row in range(0, 3):
                if board_to_check.get_symbol(row, col) == symbol:
                    symbol_count += 1
                elif board_to_check.get_symbol(row, col) in range(0, 10):
                    empty_col_index = board_to_check.get_symbol(row, col)
            if symbol_count == 2:
                # We have a winning move!
                return empty_col_index

        symbol_count = 0
        empty_col_index = None
        for idx in range(0, 3):
            if board_to_check.get_symbol(idx, idx) == symbol:
                symbol_count += 1
            elif board_to_check.get_symbol(idx, idx) in range(0, 10):
                empty_col_index = board_to_check.get_symbol(idx, idx)
        if symbol_count == 2:
            # We have a winning move!
            return empty_col_index

        symbol_count = 0
        empty_col_index = None
        for idx in range(0, 3):
            col = 2-idx
            if board_to_check.get_symbol(idx, col) == symbol:
                symbol_count += 1
            elif board_to_check.get_symbol(idx, col) in range(0, 10):
                empty_col_index = board_to_check.get_symbol(idx, col)
        if symbol_count == 2:
            # We have a winning move!
            return empty_col_index
        return None

    def make_turn(self, game_board: board.Board) -> None:
        cpu_choice = random.choice(list(board.POSSIBLE_NUMBERS))
        # Check for a winning move
        winning_move = self.check_for_winning_move(game_board, "O")

        blocking_move = self.check_for_winning_move(game_board, "X")
        if blocking_move:
            #print("We spotted a blocking move!")
            cpu_choice = blocking_move

        if winning_move:
            #print("We spotted a winning move!")
            cpu_choice = winning_move

        print("\nCpu choice: ", cpu_choice)
        if cpu_choice in board.POSSIBLE_NUMBERS:
            game_board.modify_board(cpu_choice, 'O')
            board.POSSIBLE_NUMBERS.remove(cpu_choice)


