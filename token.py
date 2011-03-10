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

KEYWORDS = \
("Void","Int","If","Else","For","While","Do","Switch","Case","Default","Break","Continue"\
,"Return","Printf","Input","Exit","Lparen","Rparen","Lbrace","Rbrace","Lbracket"\
,"Rbracket","Plus","Minus","Multi","Divi","Incre","Decre","Equal","NotEq","Less"\
,"LessEq","Great","GreatEq","And","Or","Not","Mod","Colon","Semicolon","Assign"\
,"Sharp","Yen","Comma","SngQ","DblQ","END_list","Others","Digit","Letter","Puts")

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
  """
    Constructor. It requires iterator which provides lines of text data.
  """
  def __init__(self,it):
    self.fp = it    # File or something which has iterator interface.
    self.line_no = 0 # Line number which this program reads now
    self.ch = u"" # To possess previous charactor for self.next_ch

  """
    Retrieve next token
  """
  def next_tkn(self):
    pass
  
  """
    Retrieve one charactor from passed iterator.
    With function to reduce comment and white space.
  """
  def next_ch(self): 
    prev_ch = self.ch
    commenting = None
    for self.ch in self.get_char():
      # c represents one charactor 

      # Commenting Check
      if prev_ch == u'/':
        # beginning of comment
        if self.ch == u'*':
          # Area comment start
          commenting = u"Area"
        elif self.ch == u'/':
          # One line comment start
          commenting = u"Line"

      elif prev_ch == u'*':
        # It may end of comment?
        if self.ch == u'/':
          # Area comment end
          commenting = None

      if self.ch == u'\n':
        # Line comment will end!
        if commenting == u"Line":
          commenting = None
      
      if commenting != None:
        continue
      else:
        return self.ch
    # It ends when all files are read.
    return u""

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
  def chk_next_tkn(self,tk,kd):
    pass

  """
    It retrieves line number of the reading file.
  """
  def get_line_no(self):
    pass

  """
    It retrieves a line of self.fp and has a function that increases self.line_no 
    automatically when it calls .  
  """
  def get_line(self):
    try:
      line = self.fp.next()
      self.line_no += 1
      return line.decode('utf-8')
    except StopIteration:
      return u""

  """
    It generates generator which produces one character from passed data.
  """
  def get_char(self):
    while True:
      line = self.get_line()
      if len(line) == 0: 
        raise StopIteration
      for c in line:
        yield c
