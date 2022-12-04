#!/usr/bin/python3.6

IF = open("day03p2.data")
#IF = open("day03p2.example")
o2 = 0
co2 = 0
lsr = 0

lines = IF.readlines()
lines = [line.rstrip() for line in lines]
#print( lines )

o2lines = lines.copy()

bitspot = 0
#print("Starting lines: ", o2lines )
while len(o2lines) > 1:

  #print("O2 lines lenght: %d" % (len(o2lines)))
  bittest = 0

  #find the most commont bit in bitspot
  for line in o2lines:
      #print( "%s" % ( line ) )
      #print( "line[%d]: %s" % (bitspot, line[bitspot] ) )
      if int(line[bitspot]) == 1:
          bittest += 1
      else:
          bittest -= 1
  
  #print("Bittest: %d" % (bittest) )
  if bittest >= 0:
      #print("Most common bit in column[%d] is 1"% (bitspot) )
      deletetarget = 0
  else:
      #print("Most common bit in column[%d] is 0"% (bitspot) )
      deletetarget = 1
  
  #build list of lines to delete
  lines2delete = []
  linenumber = 0
  for line in o2lines:
      if int(line[bitspot]) == deletetarget :
          lines2delete.append(linenumber)
      linenumber += 1
  
  #print("Lines to delete: ", lines2delete )
  
  #delete the lines
  while len(lines2delete) > 0:
      target = lines2delete.pop()
      o2lines.pop(target)

  #print("Remaining lines: ", o2lines )
  o2lines = o2lines.copy()
  bitspot += 1

print("O2 bits: %s" % (o2lines[0] ) )
o2bits = o2lines[0]
for bit in o2bits:
    #print("Converting bit: %s"  % (bit ) )
    if int(bit) == 1:
        #print("Adding a bit" ) 
        o2 += 1
    #else:
        #print("Adding a zero" ) 
    o2 = o2 << 1
    #print("oxygen generator rating: %d (%s)" % (o2, str(bin(o2))) )

o2 = o2 >> 1

co2lines = lines.copy()

bitspot = 0
#print("Starting lines: ", co2lines )
while len(co2lines) > 1:

  #print("CO2 lines lenght: %d" % (len(co2lines)))
  bittest = 0

  #find the most commont bit in bitspot
  for line in co2lines:
      #print( "%s" % ( line ) )
      #print( "line[%d]: %s" % (bitspot, line[bitspot] ) )
      if int(line[bitspot]) == 1:
          bittest += 1
      else:
          bittest -= 1
  
  #print("Bittest: %d" % (bittest) )
  if bittest >= 0:
      #print("Least common bit in column[%d] is 0"% (bitspot) )
      deletetarget = 1
  else:
      #print("Least common bit in column[%d] is 1"% (bitspot) )
      deletetarget = 0
  
  #build list of lines to delete
  lines2delete = []
  linenumber = 0
  for line in co2lines:
      if int(line[bitspot]) == deletetarget :
          lines2delete.append(linenumber)
      linenumber += 1
  
  #print("Lines to delete: ", lines2delete )
  
  #delete the lines
  while len(lines2delete) > 0:
      target = lines2delete.pop()
      co2lines.pop(target)

  #print("Remaining lines: ", co2lines )
  co2lines = co2lines.copy()
  bitspot += 1

print("CO2 bits: %s" % (co2lines[0] ) )
co2bits = co2lines[0]
for bit in co2bits:
    #print("Converting bit: %s"  % (bit ) )
    if int(bit) == 1:
        #print("Adding a bit" ) 
        co2 += 1
    #else:
        #print("Adding a zero" ) 
    co2 = co2 << 1
    #print("CO2 generator rating: %d (%s)" % (co2, str(bin(co2))) )

co2 = co2 >> 1

print("oxygen generator rating: %d (%s)" % (o2, str(bin(o2))) )
print("CO2 scrubber rating: %d (%s)" % (co2, str(bin(co2)) ) )
lsr = o2 * co2
print( "Life Support Rating: %d " % ( lsr ) )
