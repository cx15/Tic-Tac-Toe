"""A demo of object orientation"""
class Strategy:  # abstract  <---
  def makeMove(self):
    pass

  def getDescription(self):
    return "This is a computer strategy for TicTacToe"



class CpuRandomStrategy(Strategy):
  def makeMove(self):
    pass


class CpuSmartStrategy(Strategy):
  def makeMove(self):
    pass


class CpuAIStrategy(Strategy):
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

print(cpuStrat.getDescription())  #<--
cpuStrat.makeMove()



