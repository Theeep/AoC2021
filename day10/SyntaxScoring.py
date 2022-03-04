from sys import stdin
from statistics import median
'''
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
'''


points = {')':3,']':57,'}':1197,'>':25137}
ipoints = {')':1,']':2,'}':3,'>':4} 

def corrupted(syntax):
    score = 0
    invalid_syntax = []
    for line in syntax:
        lineScore = 0
        corrupted = False
        stack = []
        for symbol in line:
            if symbol == '(':
                stack.append(')')
            elif symbol == '[':
                stack.append(']')
            elif symbol == '{':
                stack.append('}')
            elif symbol == '<':
                stack.append('>')
            else:
                top = stack.pop()
                if(top != symbol):
                    lineScore += points[symbol]
                    corrupted = True
        score+=lineScore
        if not corrupted:
            invalid_syntax.append(''.join(stack[::-1]))
    return invalid_syntax,score



syntax = []
for line in stdin:
    syntax.append(line.strip())
        
invalid,score = corrupted(syntax)

iScores = []
for line in invalid:
    iScore = 0
    for symbol in line:
        iScore *= 5
        iScore += ipoints[symbol]
    iScores.append(iScore)
print(median(iScores))

