#
#   輸出資料 - 使用print(), repr() 與 物件.__repr__() 函數
#
#               print() => 輸出給人看的，容易閱讀
#               repr(), 物件.__repr__() => 輸出給機器內部讀的，以供處理
#

string = '''
This
is
a
book.
'''

string          # 在IDLE模式上看不到

print()         # 換行，等同執行'\n'

print(string)


print()

print(repr(string))


print()

print(string.__repr__())


#============================================

input('\nPlease enter any key to exit...')
