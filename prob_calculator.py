import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **contents):
        self.contents = list()
        for i in contents:
            for p in range(contents[i]):
                self.contents.append(i)

    def draw(self, num):
        balls = list()
        if num >= len(self.contents):
            return self.contents
        else:
            for i in range(num):
                rand = random.randint(0, len(self.contents)-1)
                balls.append(self.contents[rand])
                self.contents.remove(self.contents[rand])
            return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    contentcopy = hat.contents.copy()
    count = 0
    counter = 0
    for i in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        for p in expected_balls:
            if drawn.count(p) >= expected_balls[p]:
                counter += 1
        if counter == len(expected_balls):
            count += 1
            counter = 0
        else:
            counter = 0
        hat.contents.clear()
        for f in contentcopy:
            hat.contents.append(f) 
    return count / num_experiments
