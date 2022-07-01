# Convert-an-NFA-to-a-DFA

## Compute epsilon closures of the NFA
Input: epsilon-closure followed by an NFA.  
Output: One line per state, giving the epsilon closure of that state. E(q0) = fq0; q2; q3g would be output as q0:q0,q2,q3

## Construct an equivalent epsilon-free NFA
Input: nfa-to-efnfa followed by an NFA and its epsilon closures.  
Output: The states in the new NFA should have the same names as the corresponding states in the original one.

## Construct an equivalent DFA
Input: efnfa-to-dfa followed by an epsilon-free NFA.  
Output: A string representing the equivalent DFA, in the format described in the appendices.  

## Decide if the strings are in the language
Input: compute-dfa followed by a DFA, then one or more strings to test.
Output: For each string, output 1 or 0 only, indicating whether that string was accepted by the DFA.

## Format
