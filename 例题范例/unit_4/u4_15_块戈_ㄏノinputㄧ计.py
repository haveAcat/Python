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

name = input("請輸入姓名：")

engh = input("請輸入成績：")

print("name資料類型是", type(name))  # 確認輸入資料的型態

print("engh資料類型是", type(engh))

#============================================

input('\nPlease enter any key to exit...')
