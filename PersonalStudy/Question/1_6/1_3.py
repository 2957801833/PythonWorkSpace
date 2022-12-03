#编写程序显示下面的模式
#FFFFFFF    U               U       NN       NN
#FF         U               U       NNN      NN
#FFFFFFF    U               U       NN  N    NN
#FF            U         U          NN    N  NN
#FF                UUU              NN      NNN

print( (( "F" ) * 7) , ("U") ,("     ") , ("U") , ("NN"),("    "),("NN") )
print( (( "F" ) * 2) ,("    "), ("U") ,("     ") , ("U") , ("NNN"),("   "),("NN") )
print( (( "F" ) * 7) ,("U") ,("     ") , ("U") , ("NN"),(""),("N"),(" "),("NN") )
print( (( "F" ) * 2) ,("     "), ("U") ,("   ") , ("U") ,(""), ("NN"),("  "),("N"),("NN") )
print( (( "F" ) * 2) ,("       "),("UUU"),("  "),("NN"),("   "),("NNN") )