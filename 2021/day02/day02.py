#!/usr/bin/python3.6

IF = open("day02.data")
#IF = open("day02.example")
horizontal = 0
depth = 0

#magic words:
#forward direction += amount
#down depth += amount
#up depth -= amount
for line in IF:
    #print(line)
    (direction, amount) = line.split()
    #print("Direction: %s Amount: %s" % (direction, amount))

    if direction == "forward":
        #print( "Move forward %d"% (int(amount) ) )
        horizontal += int(amount)
    elif direction == "up":
        #print( "Move up %d"% (int(amount) ) )
        depth -= int(amount)
    elif direction == "down":
        #print( "Move down %d"% (int(amount) ) )
        depth += int(amount)

print("Horizontal: %d Depth: %d" % (horizontal, depth ) )

answer = horizontal * depth
print( "Answer: %d " % ( answer ) )
