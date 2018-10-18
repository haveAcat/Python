#
#   輸出資料到檔案，其基本格式如下
#
#   file_obj = open(file, mode = "r")
#
#   file_obj : 用字串列出欲開啟的檔案
#
#   mode : 開啟檔案的模式，如果省略代表是 mode = "r"，使用時
#          如果 mode = "w" 或其它，也可以省略 mode = ，直接寫
#          "w"。 也可以同時具備多項模式，例如："wb"代表以二進
#          位檔案開啟以供寫入，意下是基本模式：
#
#           r - 這是預設，開啟檔案以供讀取(檔案必須先行存在，不然會出現錯誤)
#
#           w - 新建檔案寫入(檔案可不存在，若存在則清空)
#
#           a - 資料附加到舊檔案後面(游標指在EOF)，如果沒有檔案會自動建立檔案，
#               如果已經有檔案，游標的位置會在檔案的最後面
#
#           r+ - 讀取舊資料並寫入(檔案需存在且游標指在開頭)
#
#           w+ - 清空檔案內容，新寫入的東西可在讀出(檔案可不存在，會自行新增)
#
#           a+ - 資料附加到舊檔案後面(游標指在EOF)，可讀取資料
#
#           b - 二進位模式
#
#           t - 開啟文字檔案模式(這是預設的模式)
#
#           + - 開啟檔案以供更新使用(同時具有寫入和讀取的能力)
#
#           x - 開啟一個新的檔案以供寫入，如果檔案已經存在則會產生錯誤FileExistsError
#

import os   # 導入 os 模組

current_path = os.getcwd()  # 取得本程式目前在本機所在路徑

fstream1 = open(current_path +"\\out1.txt", mode = "w") # 取代先前資料

print("Testing for output", file = fstream1)

fstream1.close( )   # 關檔，**務必要做**

#============================================

fstream2 = open(current_path +"\\out2.txt", mode = "a") # 附加資料後面

print("Testing for output", file = fstream2)

fstream2.close( )   # 關檔，**務必要做**

#============================================

input('\nPlease enter any key to exit...')
