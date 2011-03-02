"""
This source code is for retrieving tokens.
"""

#!coding:utf-8


# -----------------------------------------------------------
# Define token kinds and keyword table.
# -----------------------------------------------------------
KEYWORD_DICT = {}
KIND_DICT = {}

TOKENS =\
("Lparen","Rparen","Plus","Minus","Multi","Divi","Equal","NotEq",\
"Less","LessEq","Great","GreatEq","SngQ","DblQ","Assign","Semicolon",\
"If","Else","Puts","Ident","IntNum",\
"String","Letter","Digit","NulKind","EofTkn","Others","END_list")
map( lambda x: KIND_DICT.setdefault(TOKENS[x],x) , xrange(0,len(TOKENS)) )

C_TYP = [KIND_DICT["Others"] for x in xrange(0,256)]
for i in xrange(ord('0'),ord('9')+1): C_TYP[i] = KIND_DICT['Digit']
for i in xrange(ord('A'),ord('Z')+1): C_TYP[i] = KIND_DICT['Letter']
for i in xrange(ord('a'),ord('z')+1): C_TYP[i] = KIND_DICT['Letter']
C_TYP[ord('_')] = KIND_DICT['Letter']
C_TYP[ord('=')] = KIND_DICT['Assign']
C_TYP[ord('(')] = KIND_DICT['Lparen']
# aborting...

key=KEYWORD_DICT
kind=KIND_DICT
key["if"] = kind["If"]; key["else"] = kind["Else"]; key["puts"] = kind["Puts"];
key["("] = kind["Lparen"]; key[")"] = kind["Rparen"]; key["+"] = kind["Plus"];
key["-"] = kind["Minus"]; key["/"] = kind["Divi"]; key["*"] = kind["Multi"];
key["=="] = kind["Equal"]; key["!="] = kind["NotEq"]; key["<"] = kind["Less"];
key["<="] = kind["LessEq"]; key[">"] = kind["Great"]; key[">="] = kind["GreatEq"];
key["="] = kind["Assign"]; key[";"] = kind["Semicolon"]; key[""] = kind["END_list"];


del(TOKENS); del(key); del(kind)


# -----------------------------------------------------------
# Define constant variables
# ----------------------------------------------------------- 
ID_SIZ  = 31
TEXT_SIZ = 100


# -----------------------------------------------------------
# Define class : Token
# ----------------------------------------------------------- 
"""
Token describes its type, integer value, and its test forms.
"""
class Token:
  def __init__(self,tkn_kind,int_val,text):
    self.tkn_kind = tkn_kind
    self.int_val = int_val
    self.text = text


# -----------------------------------------------------------
# Define class : Tokenizer
# ----------------------------------------------------------- 

class Tokenizer:
  # Kind table
  ctyp = []
  
