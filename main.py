#coding=utf-8
import sys

from lex import lexer
from yacc import parser
from htmlgen import render

#reload(sys)
#sys.setdefaultencoding('utf-8')





if len(sys.argv)>1:
    F=open(sys.argv[1])
    data=F.read()
else:
    data=sys.stdin.read()

result = parser.parse(data)
print(render(result))
