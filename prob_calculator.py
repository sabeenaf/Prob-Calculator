import copy
import random
# Consider using the modules imported above.

class Hat:
  # constructor function
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_balls):
    if num_balls>len(self.contents):
      return self.contents
    draw_balls=[]
    while num_balls > 0:
        draw_balls.append(self.contents.pop(random.randrange(len(self.contents))))
        num_balls -= 1
    return draw_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M=0 #number of times we found the expected balls

  #looping over experiments
  for i in range(num_experiments):
    found=0
    CopyHat=copy.deepcopy(hat) #copy as we will remove elements from hat using draw method
    actual = CopyHat.draw(num_balls_drawn) #draw balls
    for key, value in expected_balls.items(): #traversiing expected balls to compare with drawn balls
      if actual.count(key) < value: #if we did not find the expected balls, break the loop
        found=0
        break
      else:
        found=1 #set flag to 1 if we found the expected balls
    if found==1: #if drawn balls match expected balls increment M
      M+=1

  probability=M/num_experiments #number of matches/ number of experiments
  return probability
