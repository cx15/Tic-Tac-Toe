import board
import random


class Strategy:
  def make_turn(self):
    raise NotImplementedError("You need to implement this")


class CpuRandomStrategy(Strategy):
  def make_turn(self):
    cpu_choice = random.choice(list(board.possibleNumbers))
    print("\nCpu choice: ", cpu_choice)
    if cpu_choice in board.possibleNumbers:
      board.modifyArray(cpu_choice, 'O')
      board.possibleNumbers.remove(cpu_choice)


class CpuBetterStrategy(Strategy):
  def make_turn(self):
    # TODO: Update this
    cpu_choice = random.choice(list(board.possibleNumbers))
    print("\nCpu choice: ", cpu_choice)
    if cpu_choice in board.possibleNumbers:
      board.modifyArray(cpu_choice, 'O')
      board.possibleNumbers.remove(cpu_choice)
