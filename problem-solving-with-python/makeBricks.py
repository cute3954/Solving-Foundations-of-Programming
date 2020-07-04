# https://codingbat.com/prob/p183562
#
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return true if it is possible to make the goal by choosing from the given bricks.
# This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
#
# makeBricks(3, 1, 8) → true
# makeBricks(3, 1, 9) → false
# makeBricks(3, 2, 10) → true
class BricksMaker:
    def __init__(self):
        self.bricks = [
            {'small': 3, 'big': 1, 'goal': 8},
            {'small': 6, 'big': 0, 'goal': 11},
            {'small': 1, 'big': 4, 'goal': 12},
            {'small': 43, 'big': 1, 'goal': 46},
            {'small': 1000000, 'big': 1000, 'goal': 1000100},
            {'small': 2, 'big': 1000000, 'goal': 100003},
            {'small': 20, 'big': 4, 'goal': 39}
        ]
        for i in range(len(self.bricks)):
            result = self.makeBricks(self.bricks[i])
            print(result)

    def makeBricks(self, bricks):
        small = bricks['small']
        big = bricks['big']
        goal = bricks['goal']

        re = goal - big * 5 if goal >= big * 5 else  goal % 5
        result = False if re > small else True
        return result

BricksMaker()