#
#
#   格式化字串時，所使用的%d、%f、%s等 與C語 言類似，之後使用%接上一個tuple('小括號()')，
#   也就是範例中以()包 括的實字表示部份。一些可用的字串格式字列舉如下： 
#
#
#   %%	        在字串中顯示%
#
#   %d	        將整數以10進位方式輸出
#
#   %f	        將浮點數(實數)以10進位方式輸出
#
#   %e, %E	將浮點數(實數)以10進位方式輸出，並使用科學記號
#
#   %o	        將整數以8進位方式輸出
#
#   %x, %X	將整數以16進位方式輸出
#
#   %s	        使用str()將字串輸出
#
#   %c	        以字元(character)方式輸出
#
#   %r	        使用repr()輸出字串
#

score = 90

str1 = "張大衛"

count = 1
                                        
# 注意: print("輸出格式化字串" % (依序輸出資料指定格式))
formatstr = "%s你的第 %d 次程式測驗成績是 %d"

print(formatstr % (str1, count, score))

#============================================

input('Please enter any key to exit...')
