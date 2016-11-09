import os
import re
import sys

from Algo23.Graph.AdjacencyList import *
from Algo23.Graph.ReachableVertices import *
from Algo23.Graph.TopologicalSort import *

class decouple_module:
    def __init__(self,code):
        self.code=code
        for i in range(len(code)):
            if code[i][-1]!='\n':
                code[i]+='\n'
        if code[0].split()[0]=='class':
            self.name=code[0].split()[1].split(':')[0]
        elif code[0].split()[0]=='def':
            self.name = code[0].split()[1].split('(')[0]
        else:
            self.name = code[0].split()[0].split('=')[0]
        self.refer=[]
    def make_refer(self,modules):
        for line in self.code:
            for i in re.findall('\w+',line):
                if i in modules and i !=self.name and not i in self.refer:
                    self.refer+=[i]

def decouple_is_irrelevant_line(line):
    t=line.split()
    return len(t)==0 or t[0]=='import' or t[0]=='from'

def decouple_modules_from_file(fileName,modules):
    file=open(fileName)
    lines=file.readlines()
    i=0
    while i<len(lines):
        if decouple_is_irrelevant_line(lines[i]):
            i+=1
        else:
            j=i
            while j+1<len(lines) and not decouple_is_irrelevant_line(lines[j+1]) and lines[j+1][0]==' ':
                j=j+1
            m=decouple_module(lines[i:j+1])
            modules[m.name]=m
            i=j+1
    file.close()
    return modules

def decouple():
    modules={}
    root=__file__
    while os.path.basename(root)!='Algo23':
        root=os.path.dirname(root)
    for n,d,f in os.walk(root):
        for i in map(os.path.splitext,f):
            if i[0]!='__init__'and i[1]=='.py':
                decouple_modules_from_file(n+os.sep+i[0]+i[1],modules)
    t=0
    a=[0]*len(modules)
    g=AdjacencyList(len(a),[])
    g2=AdjacencyList(len(a),[])
    for i in modules:
        modules[i].make_refer(modules)
        modules[i].id=t
        a[t]=modules[i]
        t+=1
    for i in modules:
        for j in modules[i].refer:
            g.add_edge((modules[j].id,modules[i].id))
            g2.add_edge((modules[i].id,modules[j].id))
    b=topological_sort(g)
    input=open(sys.argv[0])
    t=os.path.splitext(sys.argv[0])
    output=open(t[0]+'(decoupled)'+t[1],'w+')
    f=[0]*g.n
    buffer2=[]
    buffer=[]
    for line in input.readlines():
        if not 'decouple' in line and not 'Algo23' in line:
            buffer+=[line]
            for word in re.findall('\w+',line):
                if word in modules:
                    if f[modules[word].id]==0:
                        reachable_vertices(g2,modules[word].id,f)
    for i in b:
        if f[i]==1:
            buffer2+=a[i].code+['\n']
    for i in buffer2+buffer:
        output.write(i)
    input.close()


