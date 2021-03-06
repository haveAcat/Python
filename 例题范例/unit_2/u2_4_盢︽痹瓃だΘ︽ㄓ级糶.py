# 
#   認識變數 - 將一行敘述分成多行來撰寫
#

a = b = c = 10

x = a + b + c + 12

print(x)

#==== 續行方法1 - 在裡面使用斜線符號 ====================

y = a +\
    b +\
    c +\
    12

print(y)


#==== 續行方法2 - 在外面使用小括號   ====================

z = ( a +     # 此處可以加上註解  
      b +
      c +
      12 )

print(z)

#=====================================

input('Please enter any key to exit...')
