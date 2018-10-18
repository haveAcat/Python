#
#   字串前加字元'r'，以防止將Escape Character轉譯與執行
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

str1 = "Hello!\nPython"

print("不含r字元的輸出")

print(str1)

#============================================

str2 = r"Hello!\nPython"

print("含r字元的輸出")

print(str2, '\n')

#============================================

input('Please enter any key to exit...')
