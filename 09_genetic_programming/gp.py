# -*- coding: utf-8 -*-
from random import random, randint, choice
from copy import deepcopy
from math import log


class fwrapper:
    """
        関数ノードで利用される関数のラッパー。
        メンバー変数は関数の名前、関数自身、それが受け取るパラメータの数を持つ。
    """
    def __init__(self, function, childcount, name):
        self.function = function
        self.childcount = childcount
        self.name = name

class node:
    """
        関数ノード（子を持っているノード）のクラス。
        fwrapperによって初期化される。
        evaluate関数が呼び出されると、子ノードを評価して、関数をその結果に適用する。
    """
    def __init__(self, fw, children):
        self.function = fw.function
        self.name = fw.name
        self.children = children

    def evaluate(self, inp):
        results = [n.evaluate(inp) for n in self.children]
        return self.function(results)

    def display(self, indent=0):
        print(' ' * indent + self.name)
        for c in self.children:
            c.display(indent + 1)

class paramnode:
    """
        プログラムに渡されたパラメータたちの1つを返すだけのノードクラス。
        evaluateメソッドは、idxで指定されたパラメータを返す。
    """
    def __init__(self, idx):
        self.idx = idx

    def evaluate(self, inp):
        return inp[self.idx]

    def display(self, indent=0):
        print(" "*indent + "p" + str(self.idx))

class constnode:
    """
        定数のノード。
        evaluateメソッドは、単純に初期化された値を返す。
    """
    def __init__(self, v):
        self.v = v

    def evaluate(self, inp):
        return self.v

    def display(self, indent=0):
        print(" "*indent + str(self.v))        



# Functions list.
addw = fwrapper(lambda x:x[0]+x[1], 2, "add")
subw = fwrapper(lambda x:x[0]-x[1], 2, "subtract")
mulw = fwrapper(lambda x:x[0]*x[1], 2, "multiply")
ifw  = fwrapper(lambda x:x[1] if x[0]>0 else x[2], 3, "if")
gtw  = fwrapper(lambda x:1 if x[0]>x[1] else 0, 2, "isgreater")
flist = [addw, subw, ifw, gtw]

# Test
def exampletree():
    return node(ifw, [
            node(gtw,  [paramnode(0), constnode(3)]),
            node(addw, [paramnode(1), constnode(5)]),
            node(subw, [paramnode(1), constnode(2)])
        ])
exgp = exampletree()
# print(exgp.evaluate([2,3]))
# print(exgp.evaluate([5,3]))
# exgp.display()


# 最初の集団を作る
def makerandomtree(pc, maxdepth=4, fpr=0.5, ppr=0.6):
    """
        Make a tree random.
        @param pc       : the number of params which is set to this tree.
        @param maxdepth : the depth of tree.
        @param fpr      : the ratio of making a function node.
        @param ppr      : the ratio of making a param node.
    """
    if random() < fpr and maxdepth > 0:
        f = choice(flist)
        children = [makerandomtree(pc, maxdepth-1, fpr, ppr) for i in range(f.childcount)]
        return node(f, children)
    elif random()  < ppr:
        return paramnode(randint(0, pc-1))
    else:
        return constnode(randint(0, 10))

# test.
random1 = makerandomtree(2) 
random2 = makerandomtree(2)
# makerandomtree(2).display()

# This is a function which the Genetic Algorithm will find.
def hiddenfunction(x, y):
    return x**2+2*y+3*x+5

# Create a set which has params and answers.
def buildhiddenset():
    rows = []
    for i in range(200):
        x = randint(0, 40)
        y = randint(0, 40)
        rows.append([x, y, hiddenfunction(x, y)])
    return rows
hiddenset = buildhiddenset()

# Scoring tree performance.
def scorefunction(tree, s):
    diff = 0
    for data in s:
        v = tree.evaluate([data[0], data[1]])
        diff += abs(v - data[2])
    return diff

# Test
# print(scorefunction(random1, hiddenset))
# print(scorefunction(random2, hiddenset))


# Mutation evolution.
def mutate(t, pc, probchange=0.1):
    if random() < probchange:
        return makerandomtree(pc)
    else:
        result = deepcopy(t)
        if hasattr(t, "children"):
            result.children = [mutate(c, pc, probchange) for c in t.children]
        return result

# Test
# random2.display()
# print("-----")
# muttree = mutate(random2, 2)
# muttree.display()
# print("-----")
# print(scorefunction(random2, hiddenset))
# print(scorefunction(muttree, hiddenset))





















