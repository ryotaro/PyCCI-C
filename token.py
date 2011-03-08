"""
This source code is for retrieving tokens.
"""

#!coding:utf-8

# -----------------------------------------------------------
# Define constant variables
# -----------------------------------------------------------

# line characters limit
LINE_SIZE = 250 
ID_SIZ  = 31
TEXT_SIZ = 100



# -----------------------------------------------------------
# Define token kinds and keyword table.
# -----------------------------------------------------------
KEYWORD_DICT = {}
KIND_DICT = {}

KEYWORDS =\ 
("Void","Int","If","Else","For","While","Do","Switch","Case","Default","Break","Continue"\
,"Return","Printf","Input","Exit","Lparen","Rparen","Lbrace","Rbrace","Lbracket"\
,"Rbracket","Plus","Minus","Multi","Divi","Incre","Decre","Equal","NotEq","Less"\
,"LessEq","Great","GreatEq","And","Or","Not","Mod","Colon","Semicolon","Assign"\
,"Sharp","Yen","Comma","SngQ","DblQ","END_KeyList")

map( lambda x: KIND_DICT.setdefault(KEYWORDS[x],x) , xrange(0,len(KEYWORDS)) )
del(KEYWORDS)

C_TYP = [KIND_DICT["Others"] for x in xrange(0,256)]
for i in xrange(ord('0'),ord('9')+1): C_TYP[i] = KIND_DICT['Digit']
for i in xrange(ord('A'),ord('Z')+1): C_TYP[i] = KIND_DICT['Letter']
for i in xrange(ord('a'),ord('z')+1): C_TYP[i] = KIND_DICT['Letter']
C_TYP[ord('_')] = KIND_DICT['Letter']
C_TYP[ord('=')] = KIND_DICT['Assign']
C_TYP[ord('(')] = KIND_DICT['Lparen']
C_TYP[ord(')')] = KIND_DICT['Rparen']
C_TYP[ord('{')] = KIND_DICT['Lbrace']
C_TYP[ord('}')] = KIND_DICT['Rbrace']
C_TYP[ord('[')] = KIND_DICT['Lbracket']
C_TYP[ord(']')] = KIND_DICT['Rbracket']
C_TYP[ord('<')] = KIND_DICT['Less']
C_TYP[ord('>')] = KIND_DICT['Great']
C_TYP[ord('+')] = KIND_DICT['Plus']
C_TYP[ord('-')] = KIND_DICT['Minus']
C_TYP[ord('*')] = KIND_DICT['Multi']
C_TYP[ord('/')] = KIND_DICT['Divi']
C_TYP[ord('!')] = KIND_DICT['Not']
C_TYP[ord('%')] = KIND_DICT['Mod'] 
C_TYP[ord(':')] = KIND_DICT['Colon']
C_TYP[ord(';')] = KIND_DICT['Semicolon']
C_TYP[ord('=')] = KIND_DICT['Assign']
C_TYP[ord('\\')] = KIND_DICT['Yen']
C_TYP[ord(',')] = KIND_DICT['Comma']
C_TYP[ord('\"')] = KIND_DICT['DblQ']
C_TYP[ord('\'')] = KIND_DICT['SngQ']

KEYWORD_DICT["if"] = KIND_DICT["If"]; KEYWORD_DICT["else"] = KIND_DICT["Else"]; KEYWORD_DICT["puts"] = KIND_DICT["Puts"];
KEYWORD_DICT["("] = KIND_DICT["Lparen"]; KEYWORD_DICT[")"] = KIND_DICT["Rparen"]; KEYWORD_DICT["+"] = KIND_DICT["Plus"];
KEYWORD_DICT["-"] = KIND_DICT["Minus"]; KEYWORD_DICT["/"] = KIND_DICT["Divi"]; KEYWORD_DICT["*"] = KIND_DICT["Multi"];
KEYWORD_DICT["=="] = KIND_DICT["Equal"]; KEYWORD_DICT["!="] = KIND_DICT["NotEq"]; KEYWORD_DICT["<"] = KIND_DICT["Less"];
KEYWORD_DICT["<="] = KIND_DICT["LessEq"]; KEYWORD_DICT[">"] = KIND_DICT["Great"]; KEYWORD_DICT[">="] = KIND_DICT["GreatEq"];
KEYWORD_DICT["="] = KIND_DICT["Assign"]; KEYWORD_DICT[";"] = KIND_DICT["Semicolon"]; KEYWORD_DICT[""] = KIND_DICT["END_list"];





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
"""
Class Tokenizer provides each CCI-C tokens from passed file ( or any iterator 
that produces lines of text ).  

"""
class Tokenizer:
  # Kind table
  ctyp = []

  """
    Retrieve next token
  """
  def next_tkn(self):
    pass
  
  """
    Retrieve one charactor from passed iterator.
  """
  def next_ch(self):
    pass

  """
    Check whether this two arguments can be represented in double operands
  """
  def is_ope2(self,lhs,rhs):
    pass

  """
    Set token kind
  """
  def set_kind(tk):
    pass

  """
    It returns next token when tk.kind == kd, or returns tk
  """
  def chk_next_tkn(seflf,tk,kd):
    pass

  """
    It retrieves line number of the reading file.
  """
  def get_line_no(self):
    pass
