#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def build_monkeys(lines):
    '''take a set of lines and build
    a list of monkey dicts based on a fsm'''

    monkeys = []
    monkey = {}

    for line in lines:
        if len(line) == 0:
            if len(monkey.keys()) > 0:
                monkey.update({'inspection': 0})
                #print("Adding a monkey: " , monkey)
                monkeys.append(monkey)
            #print("new monkey")
            monkey = {}

        if line.startswith("Starting"):
            _, items = line.split(":")
            items = items.replace(",","")
            items = items.split()
            #print("Items: ", items)
            i = 0
            while i < len(items):
                #print("Item: %d" %(int(items[i])))
                items[i] = int(items[i])
                i+=1
            #print("Items: ", items)
            monkey.update({"items": items})
        if line.startswith("Operation"):
            parts = line.split()
            value = parts.pop()
            if value == "old":
                value = ''
            operation = parts.pop()
            #print("Operation: %s Value ." %(operation), value)
            monkey.update({'operation': operation})
            monkey.update({'value': value})
        if line.startswith("Test"):
            parts = line.split()
            test = parts.pop()
            test = int(test)
            monkey.update({'test': test})
        if line.startswith("If true"):
            parts = line.split()
            dest = parts.pop()
            dest = int(dest)
            monkey.update({"true": dest})
        if line.startswith("If false"):
            parts= line.split()
            dest = parts.pop()
            dest = int(dest)
            monkey.update({"false": dest})

    if len(monkey.keys()) > 0:
        monkey.update({'inspection': 0})
        #print("Adding a monkey: " , monkey)
        monkeys.append(monkey)

    return monkeys

def monkey_toss(monkeys, modulo=0 ):
    '''the monkeys will toss items and
    return the new monkey dict'''

    for monkey in monkeys:
        #print("Monkey items: ", monkey['items'])
        true_count = 0
        false_count = 0

        while len(monkey['items']) > 0:
            item = monkey['items'].pop(0)
            #print("Looking at item: %d"%(item))

            #fetch operation
            oper = monkey['operation']
            value = monkey['value']
            if len(value) == 0:
                value = item
            else:
                value = int(value)
            #run the operation
            #print("Operation: %s Value: %d"%(oper, value))
            w_l = 0
            if oper=="+":
                w_l = item + value
            elif oper.startswith("*"):
                w_l = item * value
            #print("Worry level: %d"% (w_l))
            #w_l = int(w_l/3)
            w_l = w_l%modulo
            #print("Bored level: %d" %(w_l))
            #run the test
            if w_l%monkey['test'] == 0:
                #print("True Move to: %d"%(monkey['true']))
                dest = monkey['true']
                true_count += 1
            else:
                #print("False Move to: %d"%(monkey['false']))
                dest = monkey['false']
                false_count += 1
            monkeys[dest]['items'].append(w_l)
            monkey['inspection'] += 1
        #print("True count: %d False count: %d" %(true_count, false_count))


#    for monkey in monkeys:
#        print("Monkey items: ", monkey['items'])
#    print("")
    return monkeys

def find_answer(monkeys):
    ''' will return the product of
    two highest inspection counts'''
    answer = 0
    inspections = []

    for monkey in monkeys:
        inspections.append(monkey['inspection'])
    #print(inspections)
    inspections.sort(reverse=True)
    answer = inspections[0] * inspections[1]
    return answer

def find_modulo(monkeys):
    '''find the modulo of all of the tests'''
    modulo = 1
    for monkey in monkeys:
        modulo *= monkey['test']

    return modulo

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    lines = []

    monkeys = []

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    for line in file_input:
        line = line.strip("\n")
        line = line.strip()
        #print("Line: %s" %(line) )
        lines.append(line)

    monkeys = build_monkeys(lines)
    #print("Monkeys:%d"%(len(monkeys)))

    modulo = find_modulo(monkeys)
    #print("Modulo: %d" %(modulo))
    i = 0
    while i <10000:
        monkeys = monkey_toss(monkeys, modulo=modulo )
        #print("%d"%i)
        #answer = find_answer(monkeys)
        i+=1

    answer = find_answer(monkeys)

    print("Wrong answer: 271331058 (dont submit the example answer)")
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
