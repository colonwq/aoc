#!/usr/bin/python3
'''
Day 16 part 1... some kind of protocol decoder
'''

#import re

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
        [BIN_STRING.append(x) for x in HEX_TO_BIN_2[alpha]]
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

def decode_bin(bit_len):
    '''
    This function decodes the incoming bin string into something
    '''
    global VERSION_SUM
    print("bin: %s" % (BIN_STRING))
    print("packet size: %d" % (bit_len))
    tmp_string = ""
    for x in BIN_STRING:
        tmp_string += x 
    print("%s"% ( tmp_string))
    print("TTTVVV....")
    version_str = ""
    type_string = ""
    #version = in_string[0:3]
    #while len(in_string) > 0:
    version_str += BIN_STRING.pop(0)
    version_str += BIN_STRING.pop(0)
    version_str += BIN_STRING.pop(0)
    type_string += BIN_STRING.pop(0)
    type_string += BIN_STRING.pop(0)
    type_string += BIN_STRING.pop(0)
    version = bin_to_int(version_str)
    VERSION_SUM += version
    type_id = bin_to_int(type_string)
    #print("Version: %s Type: %s" % ( version_str, type_string ) )
    print("Version: %d Type: %d" % ( version, type_id ) )
    if type_id == 4:
        print("A literal message")
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
        print("Literal bin string: %s" %(literal_string))
        #print("Literal string: %d" %(int(bin(literal_string))))
        digit = bin_to_int(literal_string)
        print("Converted digit: %d" %(digit))
    #elif type_string == "":
    #elif type_id == 3 or type_id == 6:
    else:

        print("An operator message")
        print("bin: %s" % (BIN_STRING))
        length_id = int(BIN_STRING.pop(0))

        if length_id == 0:
            print("15 bit length for sub packets length")
            for x in BIN_STRING:
                tmp_string += x 
            print("%s"% ( tmp_string))
            print("LLLLLLLLLLLLLLLAAA...")
            sub_packet_len_str = ""
            i = 0
            while i <15:
                sub_packet_len_str += BIN_STRING.pop(0)
                i += 1
            sub_packet_len = bin_to_int(sub_packet_len_str)
            print("Packet len: %s" %(sub_packet_len))
            print(BIN_STRING)
            init_bin_len = len(BIN_STRING)
            print("Initial bit str len: %d" % (init_bin_len))
            while len(BIN_STRING) > init_bin_len - sub_packet_len:
                print("Calling recursive decode_bin()")
                decode_bin(sub_packet_len)
        else:
            print("11 bit length for number of sub packets")
            tmp_string = ""
            for x in BIN_STRING:
                tmp_string += x 
            print("%s"% ( tmp_string))
            print("LLLLLLLLLLLAAA...")
            i = 0
            sub_packet_str = ""
            while i <11:
                sub_packet_str += BIN_STRING.pop(0)
                i += 1
            sub_packet_cnt = bin_to_int(sub_packet_str)
            print("Packet len: %s" %(sub_packet_cnt))
            i = 0
            while i < sub_packet_cnt:
                decode_bin(-1)
                i += 1

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
        print("Line: %s" % (line))

        for char in line:
            hex_string.append(char)

        #print(hex_string)

        #bin_string = decode_hex(hex_string)
        decode_hex(hex_string)
        #print("bin string: %s" % (bin_string))
        #decode_bin(bin_string)
        decode_bin(len(BIN_STRING))

        hex_string = []
    print("Version sum: %d"%(VERSION_SUM))


if __name__ == "__main__":
    main()
