#
#  格式化資料輸出使用print()
#
#    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#    
#    Prints the values to a stream, or to sys.stdout by default.
#
#    Optional keyword arguments:
#    value: 表示想要輸出的資料，可以一次輸出多筆資料，資料之間以逗號隔開。
#    file:  資料輸出的位置，預設是sys.stdout，也就是螢幕。
#    sep:   當輸出多筆資料時，可以插入各筆資料之間的分隔字元，預設是一個空白字元。
#    end:   當資料輸出結束時，所插入的字元，預設是一個換行字元('\n')。
#    flush: 是否要強制清除資料流的緩衝區，預設是不清除。
#

num1 = 222

num2 = 333

num3 = num1 + num2

print("這是數值相加", num3)

str1 = str(num1) + str(num2)

print("強制轉換為字串相加", str1, sep=" $$$ ") # 變更分隔字元


#============================================

input('Please enter any key to exit...')
