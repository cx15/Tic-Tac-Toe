import board
import random


class Strategy:
    def make_turn(self, cpu_x: str, game_board: board.Board) -> int:
        """
        Returns the move that was made and updates the game board.
        """
        raise NotImplementedError("You need to implement this")

class CpuRandomStrategy(Strategy):
    def make_turn(self, cpu_x: str, game_board: board.Board) -> int:
        cpu_choice = random.choice(game_board.get_open_positions())
        # print("\nCpu choice: ", cpu_choice)
        game_board.modify_board(cpu_choice, cpu_x)
        return cpu_choice


class CpuBetterStrategy(Strategy):
    def check_for_winning_move( self, board_to_check: board.Board, symbol: str,):
        """Check the board to see if there's a winning move available for the
        given symbol.

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
            if symbol_count == 2 and empty_col_index:
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
            if symbol_count == 2 and empty_col_index:
                # We have a winning move!
                return empty_col_index

        symbol_count = 0
        empty_col_index = None
        for idx in range(0, 3):
            if board_to_check.get_symbol(idx, idx) == symbol:
                symbol_count += 1
            elif board_to_check.get_symbol(idx, idx) in range(0, 10):
                empty_col_index = board_to_check.get_symbol(idx, idx)
        if symbol_count == 2 and empty_col_index:
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
        if symbol_count == 2 and empty_col_index:
            # We have a winning move!
            return empty_col_index
        return None

    def make_turn(self, game_board: board.Board, cpu_x: str) -> int:
        cpu_choice = random.choice(game_board.get_open_positions())
        # Check for a winning move
        winning_move = self.check_for_winning_move(game_board, cpu_x)

        blocking_move = self.check_for_winning_move(game_board,"O" if cpu_x == "X" else "X")
        if blocking_move:
            #print("We spotted a blocking move!")
            cpu_choice = blocking_move

        if winning_move:
            #print("We spotted a winning move!")
            cpu_choice = winning_move

        # print("\nCpu choice: ", cpu_choice)
        if game_board.is_valid_play(cpu_choice):
            game_board.modify_board(cpu_choice, cpu_x)
        else:
            raise Exception("CPU choice wasn't a valid play")
        return cpu_choice

class CpuMirrorStrategy(Strategy):
    """
    This Cpu strategy just tries to copy what the human player does.
    """
    def make_turn(self, game_board: board.Board) -> int:
        # Go through all the positions and find the opposite
        """
        Actually don't need this map as the formula is simple: if the
        human plays X the computer should play 10-X
        opposites_map = {
            1: 9,
            2: 8,
            3: 7,
            4: 6,
            5: 5,
            6: 4,
            7: 3,
            8: 2,
            9: 1
        }
        """
        for pos in range(1, 10):
          symbol = game_board.get_symbol_by_pos(pos)
          if symbol == "X":
            possible_cpu_pos = 10 - pos
            if game_board.is_valid_play(possible_cpu_pos):
              game_board.modify_board(possible_cpu_pos, "O")
              return possible_cpu_pos

        # None of the opposites were valid, so just pick randomly.
        cpu_choice = random.choice(game_board.get_open_positions())
        if game_board.is_valid_play(cpu_choice):
            game_board.modify_board(cpu_choice, 'O')
        else:
            raise Exception("CPU choice wasn't valid play")
        return cpu_choice
