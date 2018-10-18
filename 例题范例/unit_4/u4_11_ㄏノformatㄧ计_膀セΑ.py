#
#   使用format()是python增強版的格式化輸出功能，其格式如下
#
#   print("...輸出格式區..." . format(變數系列區, ... ))
#
#   在輸出格式區內的字串變數使用"{}"來表示。
#

score = 90

str1 = "張大衛"

count = 1

# 注意: print("依序包含{}輸出的格式化字串".format(依序輸出資料指定格式))                                        
print("{}你的第 {} 次程式測驗成績是 {}".format(str1, count, score))

#============================================

input('\nPlease enter any key to exit...')
