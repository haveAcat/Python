#
#   輸入資料 - 使用input函數
#
#   語法：  value = input("prompt: ")
#
#           value所收到的 資料一律認定是字串型態，
#           如需轉換成其他資料型態，需使用以下函數
#           來完成：
#           eval(), int(), str(), float(), complex()
#

print("歡迎使用成績輸入系統")

name = input("請輸入姓名：")

engh = input("請輸入英文成績：")

math = input("請輸入數學成績：")

total = int(engh) + int(math)

print("%s 你的總分是 %d" % (name, total))

#============================================

input('\nPlease enter any key to exit...')
