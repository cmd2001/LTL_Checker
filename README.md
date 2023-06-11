# LTL_Checker

CS3959 Project

## Requirements

- python 3.11
- antlr4

## How to run

```sh
conda create -n ltl_checker python=3.11
conda activate ltl_checker
pip install -r ./requirements.txt
cp test-case/* src/
cd src
python3 ./test.py
```

## Implement

### Parser

in `src/Parser`

We are using Antlr4 as a third-party parser, a visitor is implemented to convert the abstract syntax tree to a LTL formula.

### LTL to GNBA

in `src/BA/GNBA`

Following the proof of Theorem 5.37 (page 278 of Principles of Model Checking)

### GNBA to BA

in `src/BA/NBA`

Following the proof of Theorem 4.56 (page 195 of Principles of Model Checking)

### Cross product of TS and NBA

in `src/TS/ProductTS`

Following Definition 4.62 (page 200 of Principles of Model Checking)

### Persistence Checking

in `src/TS/ProductTS`, the method `nested_dfs` of `ProductTS` class.

Following the nested depth-first search (page 211 of Principles of Model Checking)

## Structures

This project just **DOES NOT** pass all the example testcases, however the output of intermediate structure seems correct.

Maybe there are just more details to be figured out.

We can just uncomment some `print` sentence in `src/test.py` to get intermediate structure details.

Here are some examples:

### TS

```
Printing Transition System...
n_states: 6, n_init_states: 1
initial states are:
0
formula at each state are:
0: a | b
1: a | b | c
2: b | c
3: a | c
4: a | c
5: a | b
transitions are:
0: 1 3
1: 4
2: 1
3: 1
4: 1 5
5: 2 1
```

### GNBA

```
Printing GNBA
n_nodes: 7, n_start_nodes: 4, n_accept_sets: 1
start nodes are:
0 2 4 6
accept sets are:
1 3 5 6
formula set at each node are:
0: (True) U (NOT ((a) OR (b))) | True | (a) OR (b) | a | b
1: NOT ((True) U (NOT ((a) OR (b)))) | True | (a) OR (b) | a | b
2: (True) U (NOT ((a) OR (b))) | True | (a) OR (b) | NOT (a) | b
3: NOT ((True) U (NOT ((a) OR (b)))) | True | (a) OR (b) | NOT (a) | b
4: (True) U (NOT ((a) OR (b))) | True | (a) OR (b) | a | NOT (b)
5: NOT ((True) U (NOT ((a) OR (b)))) | True | (a) OR (b) | a | NOT (b)
6: (True) U (NOT ((a) OR (b))) | True | NOT ((a) OR (b)) | NOT (a) | NOT (b)
edges are:
0: 0 2 4 6
1: 1 3 5
2: 0 2 4 6
3: 1 3 5
4: 0 2 4 6
5: 1 3 5
6: 0 1 2 3 4 5 6
```

### NBA

```
Printing GNBA
n_nodes: 7, n_start_nodes: 4, n_accept_set: 4
start nodes are:
0 2 4 6
accept sets are:
1 3 5 6
formula set at each node are:
0: (True) U (NOT ((a) OR (b))) | True | (a) OR (b) | a | b
1: NOT ((True) U (NOT ((a) OR (b)))) | True | (a) OR (b) | a | b
2: (True) U (NOT ((a) OR (b))) | True | (a) OR (b) | NOT (a) | b
3: NOT ((True) U (NOT ((a) OR (b)))) | True | (a) OR (b) | NOT (a) | b
4: (True) U (NOT ((a) OR (b))) | True | (a) OR (b) | a | NOT (b)
5: NOT ((True) U (NOT ((a) OR (b)))) | True | (a) OR (b) | a | NOT (b)
6: (True) U (NOT ((a) OR (b))) | True | NOT ((a) OR (b)) | NOT (a) | NOT (b)
edges are:
0: 0 2 4 6
1: 1 3 5
2: 0 2 4 6
3: 1 3 5
4: 0 2 4 6
5: 1 3 5
6: 0 1 2 3 4 5 6
```

### ProductTS

```
Printing Transition System...
n_states: 42, n_init_states: 4
initial states are:
0 2 4 6
mapping to TS and NBA is:
0: (0, 0) 1: (0, 1) 2: (0, 2) 3: (0, 3) 4: (0, 4) 5: (0, 5) 6: (0, 6)
7: (1, 0) 8: (1, 1) 9: (1, 2) 10: (1, 3) 11: (1, 4) 12: (1, 5) 13: (1, 6)
14: (2, 0) 15: (2, 1) 16: (2, 2) 17: (2, 3) 18: (2, 4) 19: (2, 5) 20: (2, 6)
21: (3, 0) 22: (3, 1) 23: (3, 2) 24: (3, 3) 25: (3, 4) 26: (3, 5) 27: (3, 6)
28: (4, 0) 29: (4, 1) 30: (4, 2) 31: (4, 3) 32: (4, 4) 33: (4, 5) 34: (4, 6)
35: (5, 0) 36: (5, 1) 37: (5, 2) 38: (5, 3) 39: (5, 4) 40: (5, 5) 41: (5, 6)
transitions are:
0: 7 9 11 13
1: 8 10 12
2:
3:
4: 21 23 25 27
5: 22 24 26
6:
7:
8:
9:
10:
11: 28 30 32 34
12: 29 31 33
13:
14: 7 9 11 13
15: 8 10 12
16:
17:
18:
19:
20:
21: 7 9 11 13
22: 8 10 12
23:
24:
25:
26:
27:
28: 7 9 11 13 35 37 39 41
29: 8 10 12 36 38 40
30:
31:
32:
33:
34:
35: 7 9 11 13
36: 8 10 12
37: 14 16 18 20
38: 15 17 19
39:
40:
41:
```
