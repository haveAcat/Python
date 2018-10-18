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

clastname = input("請輸入中文姓氏：")

cfirstname = input("請輸入中文名字：")

cfullname = clastname + cfirstname

print("%s 歡迎使用本系統" % cfullname)

#========================================

lastname = input("請輸入英文Last Name：")

firstname = input("請輸入英文First Name：")

fullname = firstname + " " + lastname

print("%s Welcome to SSE System" % fullname)

#============================================

input('\nPlease enter any key to exit...')
