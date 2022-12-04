#!/usr/bin/python3.6

IF = open("day02.data")
#IF = open("day02.example")
last = -1

A = 0
B = 0
C = 0
D = 0
increase = 0
NR = 1

for line in IF:
  #print(line)
  depth = int(line)

  if NR%4 == 1:
    if NR > 4:
      A += depth
      B = 0
      C += depth
      D += depth;
      if C > last:
         print( "C: %d (increased)" % (C) )
         increase += 1
      elif C < last:
         print( "C: %d (decreased)" % (C) )
      else:
         print( "C: %d (no change)" % (C) )
      last = C
    else:
      A += depth
  if NR%4 == 2:
    if NR>5:
      A += depth
      B += depth
      C = 0
      D += depth
      if D > last:
         print( "D: %d (increased)" % (D) )
         increase += 1
      elif D < last:
         print( "D: %d (decreased)" % (D) )
      else:
         print( "D: %d (no change)" % (D) )
      last = D
    else:
      A += depth
      B += depth
  if NR%4 == 3:
      if NR > 6:
          A += depth
          B += depth
          C += depth
          D = 0
      else:
           A += depth
           B += depth
           C += depth

      if last < 0:
         print( "A: %d (N/A - no previous sum)" % (A) )
      elif A > last:
         print( "A: %d (increased)" % (A) )
         increase += 1
      elif A < last:
         print( "A: %d (decreased)" % (A) )
      else:
         print( "A: %d (no change)" % (A) )

      last = A
  if NR%4 == 0:
    A = 0
    B += depth
    C += depth
    D += depth
    if B > last:
       print( "B: %d (increased)" % (B) )
       increase += 1
    elif B < last:
       print( "B: %d (decreased)" % (B) )
    else:
       print( "B: %d (no change)" % (B) )
    last = B
  NR += 1

print( "Number of increases: %d " % ( increase ) )
