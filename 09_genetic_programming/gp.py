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


## 01. 試しに使って見る
############################
addw = fwrapper(lambda x:x[0]+x[1], 2, "add")
subw = fwrapper(lambda x:x[0]-x[1], 2, "subtract")
mulw = fwrapper(lambda x:x[0]*x[1], 2, "multiply")
ifw  = fwrapper(lambda x:x[1] if x[0]>0 else x[2], 3, "if")
gtw  = fwrapper(lambda x:1 if x[0]>x[1] else 0, 2, "isgreater")
flist = [addw, subw, ifw, gtw]

def exampletree():
    return node(ifw, [
            node(gtw,  [paramnode(0), constnode(3)]),
            node(addw, [paramnode(1), constnode(5)]),
            node(subw, [paramnode(1), constnode(2)])
        ])
exgp = exampletree()
print(exgp.evaluate([2,3]))
print(exgp.evaluate([5,3]))
exgp.display()

# TODO コードリーディング
# 現状だとよくわからんw

"""
1
8
if
 isgreater
  p0
  3
 add
  p1
  5
 subtract
  p1
  2
"""




























