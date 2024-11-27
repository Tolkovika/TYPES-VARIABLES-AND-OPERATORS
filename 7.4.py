
###
# A program that checks if a tree can be cut down
# based on its circumference.
#
circumference = int(input('Enter tree circumference in cm: '))
pi = 3.14159
diameter = circumference / pi
can_be_cut_down = diameter >= 50
print(f'Tree can be cut down: {can_be_cut_down}')
