#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:03:48 2017

@author: florian
"""
import random
import numpy as np

def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

def score_solution(x):
    total=0
    for i in range(len(mat)):
        total+= abs( 16 - mat[i][1] - diff_letters(x,mat[i][0]) )
    return(total)

def merge_solutions(a,b):
    x=[a,b]
    return(''.join([x[random.randint(0,1)][i] for i in range(16)]))

def randomize_solution(x):
    y = list(x)
    y[random.randint(0,len(y)-1)] = str(random.randint(0,9))
    return(''.join(y))

def full_randomize_solution(x):
    y = list(x)
    sols=[]
    
    for i in range(16):
        for j in range(10):
            new_sol = list(y)
            new_sol[i] = str(j)
            sols.append( ''.join(new_sol))
    return(sols)

    

def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [idx for idx,item in enumerate(seq) if item in seen or seen_add(item)]

#'7045065478946533',
#'5040871491886503',
#'5040871491886523',


a = list(open("data/euler185.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [x.split(' ;') for x in mat]

for i in range(len(mat)):
    mat[i][1] = int(mat[i][1][0])

solutions = [''.join(map(str,[random.randint(0,9) for x in range(16)])) for y in range(800)]
scores = [score_solution(x) for x in solutions]

while(min(scores)>0):
        
        # optimizing solutions
        optim_sols = []
        for i in [random.randint(0,len(solutions)-1) for x in range(20)]:
            optim_sols = optim_sols + full_randomize_solution(solutions[i])
            
        optim_sols_scores = [score_solution(x) for x in optim_sols]   
    
        # merging solutions
        sols_a = [random.randint(0,len(solutions)-1) for x in range(75)]
        sols_b = [random.randint(0,len(solutions)-1) for x in range(75)]
        new_solutions = [merge_solutions(solutions[a],solutions[b]) for a in sols_a for b in sols_b if a!=b]
        new_scores = [score_solution(x) for x in new_solutions]    
       
        # randomization
        new_solutions2 = [randomize_solution(x) for x in solutions]
        new_scores2 = [score_solution(x) for x in new_solutions2]
        
        # add new solutions
        solutions = solutions + new_solutions
        scores = scores + new_scores
        solutions = solutions + new_solutions2
        scores = scores + new_scores2
        solutions = solutions + optim_sols
        scores = scores + optim_sols_scores
        
        duplicates = list_duplicates(solutions)
        solutions = [i for j, i in enumerate(solutions) if j not in duplicates]
        scores = [i for j, i in enumerate(scores) if j not in duplicates]       
        best = np.argsort(scores)[0:800]
        
        scores=[scores[i] for i in best]
        solutions=[solutions[i] for i in best]
        print(min(scores))