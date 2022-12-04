#!/usr/bin/python3
'''
Day 16 part 1... some kind of protocol decoder
'''

#import re
import numpy as np

VERSION_SUM = 0
BIN_STRING = []

HEX_TO_BIN_2 = {
        #"0": "0000",
        "0": ["0","0","0","0"],
        #"1": "0001",
        "1": ["0","0","0","1"],
        #"2": "0010",
        "2": ["0","0","1","0"],
        #"3": "0011",
        "3": ["0","0","1","1"],
        #4 :"0100",
        "4": ["0","1","0","0"],
        #"5": "0101",
        "5": ["0","1","0","1"],
        #"6": "0110",
        "6": ["0","1","1","0"],
        #"7": "0111",
        "7": ["0","1","1","1"],
        #"8": "1000",
        "8": ["1","0","0","0"],
        #"9": "1001",
        "9": ["1","0","0","1"],
        #"A": "1010",
        "A": ["1","0","1","0"],
        #"B": "1011",
        "B": ["1","0","1","1"],
        #"C": "1100",
        "C": ["1","1","0","0"],
        #"D": "1101",
        "D": ["1","1","0","1"],
        #"E": "1110",
        "E": ["1","1","1","0"],
        #"F": "1111",
        "F": ["1","1","1","1"],
        }

HEX_TO_BIN_1 = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
        }

def decode_hex(in_string):
#{{{
    '''
    This function converts a hex to bin
    '''

    #bin_string = []
    for alpha in in_string:
        blarg = [BIN_STRING.append(x) for x in HEX_TO_BIN_2[alpha]]
    if len(blarg) < 1:
        print("Nothing")
#}}}

def bin_to_int( string ):
#{{{
    '''
    convert sting of 01s to int
    '''
    #print("Input string: %s" % (string))
    output = 0
    for i in string:
        #print("Looking at %s"%(i))
        if i == "1":
            output += 1
        output = output << 1
    output = output >> 1
    #print("Built number %d" % (output))
    return output
#}}}

def process_literal():
    '''
    prcoess the BIN_STRING for a literal packet
    '''
    #a literal message is a series of 5 bit packets starting with a MSB of 1
    # until the last packet. The last packet has a MSB of 0
    final_packet = False
    literal_string = ""
    while not final_packet:
        packet = ""
        packet += BIN_STRING.pop(0)
        packet += BIN_STRING.pop(0)
        packet += BIN_STRING.pop(0)
        packet += BIN_STRING.pop(0)
        packet += BIN_STRING.pop(0)
        #print("Built packet: %s" % (packet))
        literal_string += packet[1:]
        #print("packet add: %s"%(packet[1:]))
        if packet[0] == "0":
            final_packet = True
    digit = bin_to_int(literal_string)
    return digit

def decode_bin():
    '''
    This function decodes the incoming bin string into something
    '''
    global VERSION_SUM
    digits = []
    digit = 0

    version = bin_to_int(BIN_STRING.pop(0) + BIN_STRING.pop(0) + BIN_STRING.pop(0))
    VERSION_SUM += version
    type_id = bin_to_int(BIN_STRING.pop(0) + BIN_STRING.pop(0) + BIN_STRING.pop(0))
    #print("Version: %d Type: %d" % ( version, type_id ) )
    if type_id == 4:
        #print("A literal message")
        digit = process_literal()
        #print("Converted digit: %d" %(digit))
    else:

        #print("An operator message: %s"%(type_id))
        length_id = int(BIN_STRING.pop(0))

        if length_id == 0:
            #print("15 bit length for sub packets length")
            sub_packet_len_str = ""
            i = 0
            while i <15:
                sub_packet_len_str += BIN_STRING.pop(0)
                i += 1
            sub_packet_len = bin_to_int(sub_packet_len_str)
            #print("Packet len: %s" %(sub_packet_len))
            init_bin_len = len(BIN_STRING)
            while len(BIN_STRING) > init_bin_len - sub_packet_len:
                #print("Calling recursive decode_bin()")
                digits.append(decode_bin())
        else:
            #print("11 bit length for number of sub packets")
            i = 0
            sub_packet_str = ""
            while i <11:
                sub_packet_str += BIN_STRING.pop(0)
                i += 1
            sub_packet_cnt = bin_to_int(sub_packet_str)
            #print("Packet count: %s" %(sub_packet_cnt))
            i = 0
            while i < sub_packet_cnt:
                digits.append(decode_bin())
                #digit = decode_bin()
                i += 1

        #print("Returned digits: ", digits)
        if type_id == 0:
            #print("Sum operator")
            digit = sum(digits)
            #print("Sum of digits: %d" % (digit))
        elif type_id == 1:
            #print("Product operator")
            #print("Number of products: %d"% len(digits))
            digit = np.prod(digits)
            #print("Product of digits: %d"%(digit))
        elif type_id == 2:
            #print("Minimum operator")
            digit = min(digits)
            #print("Min: %d"%(digit))
        elif type_id == 3:
            #print("Maxium operator")
            digit = max(digits)
            #print("Max: %d"%(digit))
        elif type_id == 5:
            #print("Greater operator")
            if digits[0] > digits[1]:
                digit = 1
            else:
                digit = 0
            #print("Great return: %d"%(digit))
        elif type_id == 6:
            #print("Less than operator")
            if digits[0] < digits[1]:
                digit = 1
            else:
                digit = 0
            #print("Less return: %d"%(digit))
        elif type_id == 7:
            #print("Equal to operator")
            if digits[0] == digits[1]:
                digit = 1
            else:
                digit = 0
            #print("Equal return: %d"%(digit))
        else:
            print("Unknown operator")
    return digit

def main():
    '''
    Here is where dragons occur
    '''
    in_file = open("../day16.data")
    #in_file = open("../day16.demo")
    #in_file = open("../day16.2")
    #in_file = open("../day16.D2")
    #in_file = open("../day16.38")
    #in_file = open("../day16.EE")
    #in_file = open("../day16.8A")
    #in_file = open("../day16.62")
    #in_file = open("../day16.C0")
    #in_file = open("../day16.A0")
    hex_string = []

    for line in in_file:
        line = line.rstrip("\r\n")
        #print("Line: %s" % (line))

        for char in line:
            hex_string.append(char)

        decode_hex(hex_string)
        final_math = decode_bin()

        hex_string = []
    print("Version sum: %d"%(VERSION_SUM))
    print("Final math: %d" % (final_math))


if __name__ == "__main__":
    main()
