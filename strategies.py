import board
import random


def cpu_turn_random():
  cpu_choice = random.choice(list(board.possibleNumbers))
  print("\nCpu choice: ", cpu_choice)
  if cpu_choice in board.possibleNumbers:
    board.modifyArray(cpu_choice, 'O')
    board.possibleNumbers.remove(cpu_choice)


def cpu_turn_better():
  cpu_choice = random.choice(list(board.possibleNumbers))
  print("\nCpu choice: ", cpu_choice)
  if cpu_choice in board.possibleNumbers:
    board.modifyArray(cpu_choice, 'O')
    board.possibleNumbers.remove(cpu_choice)