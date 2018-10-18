# 
#   Escape Character : 控制/跳脫/溢出/逸出 字元的使用
#
#   特殊字串 : 控制/跳脫/逸出 字元(escape character)
#
#   \\      倒斜線
#   \'      單引號
#   \"      雙引號
#   \a      鈴響
#   \b      退格
#   \n      換行
#   \t      縮排
#   \f      換頁
#   \o      8進位表示
#   \r      游標移至最左邊位置
#   \x      16進位表示
#   \v      垂直定位
#

#以下輸出使用單引號設定的字串，需使用\'

str1 = 'I can\'t stop loving you.'

print(str1)


#以下輸出使用雙引號設定的字串，不需使用\'

str2 = "I can't stop loving you."

print(str2)


#以下輸出有\t和\n字元

str3 = "I \tcan't stop \nloving you."

print(str3)

#============================================================

input('Please enter any key to exit...')
