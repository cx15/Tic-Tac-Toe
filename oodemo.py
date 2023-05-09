"""A demo of object orientation"""
import sys

class Circle:
  """This is the docstring for a circle"""
  def __init__(self, radius):
    self.radius = radius

  def plotMe(self):
    print(f"Plotting a circle of radius {self.radius}")

  #def __eq__(self, other):
  #  print("comparing two circles")
  #  sys.exit(5)  # <<-- crash the program!
  #  return False


class Square:
  def __init__(self, side):
    self.side = side

  def plotMe(self):
    print(f"Plotting a square of radius {self.side}")


if __name__ == "__main__":
  shapes = []
  circ = Circle(5)
  shapes.append(circ)
  shapes.append(Square(50))
  shapes.append(Circle(2))
  shapes.append(Square(5))

  for shape in shapes:
    shape.plotMe()

  #print(dir(circ))
  #print(circ.__doc__)


class CpuRandomStrategy:
  def makeMove(self):
    pass


class CpuSmartStrategy:
  def makeMove(self):
    pass


class CpuAIStrategy:
  def makeMove(self):
    pass



skillLevel = 7
cpuStrat = None
if skillLevel < 5:
  cpuStrat = CpuRandomStrategy()
elif skillLevel < 10:
  cpuStrat = CpuSmartStrategy()
else:
  cpuStrat = CpuAIStrategy()

cpuStrat.makeMove()



