#
#   認識變數 - 使用程式計算每年可以儲存多少錢
#

hourly_salary = 125                             # 設定時薪

annual_salary = hourly_salary * 8 * 300         # 計算年薪

monthly_fee = 9000                              # 設定每月花費

annual_fee = monthly_fee * 12                   # 計算每年花費

annual_savings = annual_salary - annual_fee     # 計算每年儲存金額

print(annual_savings)                           # 列出每年儲存金額

#=============================================================================

input('Please enter any key to exit...')        # 提示使用者按下任一鍵結束程式
