"""This module is the entry point to your assignment. There is some scaffolding
to help you get started. It will call the appropriate method (task_1, 2 etc.)
and load the input data. You can edit or remove as much of this code as you
wish to."""

from parser import Parser
from sys import stdin

def task_1(parser):
    """For each state of the NFA, compute the Epsilon closure and output
    it as a line of the form s:a,b,c where s is the state, and {a,b,c} is E(s)"""
    nfa = parser.parse_fa()
    # TODO: implement this
    states = nfa["states"]
    alphabet = nfa["alphabet"]
    delta = nfa["delta"]
    dic_closure = {}
    for i in states:
        dic_closure[i]=[]
    for tuples in delta:
        if tuples[1] == "":
            cur_state=tuples[0]
            cur_allclosure=dic_closure.get(cur_state)
            cur_closure=tuples[2]
            cur_allclosure.append(cur_closure)
    for cur_state in states:
        cur_allclosure=dic_closure.get(cur_state)
        i=0
        while i < len(cur_allclosure):
            cur_exam_state = cur_allclosure[i]
            cur_exam_allclosure = dic_closure.get(cur_exam_state)
            for new_closure in cur_exam_allclosure:
                if check_not_exists(cur_allclosure,new_closure):
                    cur_allclosure.append(new_closure)
            i+=1

    for cur_state in states:
        cur_allclosure=dic_closure.get(cur_state)
        print(cur_state+":",end="")
        i=0
        while i < len(cur_allclosure):
            print(cur_allclosure[i],end="")
            if i+1 < len(cur_allclosure):
                print(",",end="")
            i+=1
        print()
    print("end")

def check_not_exists(array,exam_string):
    for cur in array:
        if cur == exam_string:
            return False
    return True

def task_2(parser):
    """Construct and output an equivalent Epsilon free NFA.
    The state names should not change."""
    nfa = parser.parse_fa()
    closures = parser.parse_closures()
    # TODO: implement this
    print('TODO: print some output')

def task_3(parser):
    """Construct and output an equivalent DFA.
    The input is guaranteed to be an Epsilon Free NFA."""
    efnfa = parser.parse_fa()
    # TODO: implement this
    print('TODO: print some output')

def task_4(parser):
    """For each string, output 1 if the DFA accepts it, 0 otherwise.
    The input is guaranteed to be a DFA."""
    dfa = parser.parse_fa()
    test_strings = parser.parse_test_strings()
    # TODO: implement this
    print('TODO: print some output')

if __name__ == '__main__':

    parser = Parser()
    command = parser.parse_command()

    if command == 'epsilon-closure':
        task_1(parser)
    elif command == 'nfa-to-efnfa':
        task_2(parser)
    elif command == 'efnfa-to-dfa':
        task_3(parser)
    elif command == 'compute-dfa':
        task_4(parser)
    else:
        print(f'Command {repr(command)} not recognised.')
