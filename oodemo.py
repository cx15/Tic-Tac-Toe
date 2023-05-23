"""A demo of object orientation"""
import sys



class Circle:
  """This is the docstring for a circle"""
  def __init__(selforwhatever, radius):
    selforwhatever.myradius = radius

  def plotMe(somethingelse):
    print(f"Plotting a circle of radius {somethingelse.myradius}")

  #def __eq__(self, other):
  #  print("comparing two circles")
  #  sys.exit(5)  # <<-- crash the program!
  #  return False


"""

public abstract class Shape {
  public String getDescription("This is a shape");
  public abstract void plotMe();  // <-- 
}



public class Circle extend Shape {
  private double myradius;
  public Circle(double radius) {
    this.myradius = radius;
  }
  
  public void plotMe() {
    System.out.println("My radius is " + this.myradius);
  }
}

Circle circle1 = new Circle(5);
circle1.plotMe();

System.out.println(circle.getDescription());  /// Circle "inherits" the method getDescription

Shape shape = new Circle(5); 

shape.plotMe();

"""



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


class Wheel:
  """Represents a wheel"""
  def go(self):
    print("Wheel goes round")

class Engine:
  """Represents and engine"""

  def go(self):
    print("Engine goes vroom")

class Car:
  """This represents a car"""
  wheel1 = Wheel()
  wheel2 = Wheel()
  engine = Engine()
  def go(self):
    wheel1.go()
    wheel2.go()
    engine.go()



