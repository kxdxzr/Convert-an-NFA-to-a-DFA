# Convert-an-NFA-to-a-DFA
Done in 2019.
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
1.  Mode e.g. epsilon - closure, nfa -to - efnfa...
2. The set of states (as a comma separated list) e.g. q0,q1,q2,q3. State names should never contain ,, :, or whitespace characters.
3. The set of alphabet symbols (as a comma separated list) e.g. 0,1
4. The start state e.g. q0
5. The set of final states (as a comma separated list) e.g. q1,q3
6. A sequence of lines representing transitions, each being a comma separated list of three values s,c,t denoting a transition from s to t on symbol c.  
• DFA: s,c,t defines \delta (s; c) = t. There should be exactly one such line per (state, symbol) pair.  
• NFA: s,c,t defines t 2 \delta(s; c). There can be any number of such lines per (state, symbol) pair. \eplision is denoted by an empty string (i.e. s„t defines t 2 \delta(s; \eplision)).  
7. Finally, the word "end" on a line by itself.
