#!coding:utf-8

import unittest
import token

class TokenizerFileTreatingTest( unittest.TestCase ):
  def setUp(self):
    self.fp = open("testcode.cci","r")
    self.tokenizer = token.Tokenizer( self.fp )

  def tearDown(self):
    self.fp.close()

  def test_get_line(self):
    loop_n = 0
    while True:
      loop_n += 1
      s = self.tokenizer.get_line()
      if  s != u"":
        print s,
        assert self.tokenizer.line_no == loop_n 
      else:
        break
  
  def test_get_char(self):
    c_iter = self.tokenizer.get_char()
    for c in c_iter:
      print c,

    
suite = unittest.makeSuite( TokenizerFileTreatingTest )
tr = unittest.TextTestRunner().run(suite)
