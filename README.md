# Convert-an-NFA-to-a-DFA

## Compute epsilon closures of the NFA
Input: epsilon-closure followed by an NFA.  
Output: One line per state, giving the epsilon closure of that state. You can output the lines (and contents of the sets) in any order. E(q0) = fq0; q2; q3g would be output as q0:q0,q2,q3

## Construct an equivalent epsilon-free NFA
Input: nfa-to-efnfa followed by an NFA and its epsilon closures.  
Output: A string representing the equivalent epsilon-free NFA constructed using the algorithm given in lectures. The states in the new NFA should have the same names as the corresponding states in the original one.

## Construct an equivalent DFA
Input: efnfa-to-dfa followed by an epsilon-free NFA.  
Output: A string representing the equivalent DFA, in the format described in the appendices.  

## Format
