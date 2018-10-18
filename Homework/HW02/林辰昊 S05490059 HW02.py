#*********************************
#    Name:     林辰昊            *
#    Class:    資管系            *
#    SID:      S05490059         *
#    Function: Python程式設計    *
#    Homework: NO.2              *
#    Date:     2018/10/21        *
#*********************************




print("""****************************************
*          HW02   程式输出报表         *
****************************************\n\n""")


#-------------------項目（1）------------------------------
fruits=['apple','pineapple','banana','grap','orange','watermelon']     #產生一個串列物件fruits
print("(1)Answer:\nfruits = ",fruits)                                  #列印fruits串列

#-------------------項目（2）------------------------------
rep1_fruits=fruits[:3]+fruits[1:4]+fruits[2:5]+fruits[3:]              #利用+產生串列物件rep1_fruits
print("\n(2)Answer:\nrep1_fruits = ",rep1_fruits)                      #列印rep1_fruits串列

#-------------------項目（3）------------------------------
rep2_fruits=fruits[:3]                                                 
rep2_fruits.extend(fruits[1:4]+fruits[2:5]+fruits[3:])                 #利用extend()產生串列物件rep2_fruits
print("\n(3)Answer:\nrep2_fruits = ",rep2_fruits)                      #列印rep2_fruits串列

#-------------------項目（4）------------------------------
print("\n(4)Answer:\nOriginal list:\nrep1_fruits = ",rep1_fruits)      #列印初始串列
del rep1_fruits[2]                                                     #使用del刪除串列中第一個banana
print("\nDelete the first 'banana':\nrep1_fruits = ",rep1_fruits)      #列印刪除后的串列
del rep1_fruits[3]                                                     #（一共操作三次，刪除三個banana）
print("\nDelete the second 'banana':\nrep1_fruits = ",rep1_fruits)
del rep1_fruits[4]
print("\nDelete the third 'banana':\nrep1_fruits = ",rep1_fruits)
rep1_fruits.remove('grap')                                             #使用remove()移除串列中第一個grap
print("\nRemove the first 'grap':\nrep1_fruits = ",rep1_fruits)        #列印刪除后的串列
rep1_fruits.remove('grap')                                             #（一共操作三次，刪除三個grap）
print("\nRemove the second 'grap':\nrep1_fruits = ",rep1_fruits)
rep1_fruits.remove('grap')
print("\nRemove the third 'grap':\nrep1_fruits = ",rep1_fruits)

#-------------------項目（5）------------------------------
print("\n(5)Answer:\nOriginal list:\nrep2_fruits = ",rep2_fruits)               #列印初始串列
rep2_fruits.pop(11)                                                             #使用pop()刪除最後一位的watermelon
print("\nPop the last object named 'watermalon' off the list:",rep2_fruits)     #（以下再操作兩次，刪除兩個orange）
rep2_fruits.pop(10)
print("\nPop the last object named 'orange' off the list:",rep2_fruits)
rep2_fruits.pop(8)
print("\nPop the object named 'orange' off the list:",rep2_fruits)

#-------------------項目（6）------------------------------
rep3_fruits=tuple(rep2_fruits)                                                                                          #使用函式tuple將串列轉換成tuple
print("\n(6)Answer:\nrep3_fruits = ",rep3_fruits)                                                                       #列印tuple
sub="pineapple"                                                                                                         #設定sub為pineapple
num1=rep3_fruits.count(sub)                                                                                             #計算出tuple中pineapple的個數
print("\nThere are ",num1," object named 'pineapple' in the rep3_fruits.")                                              #列印出結果
print("\nThe index of the first object named 'pineapple' in the rep3_fruits is",rep3_fruits.index('pineapple'),".")     #列印出pineapple 物件第一次出現所在位置
check1="banana"                                                                                                         #設定要找的值是banana
print("\nIs the object named 'banana' in the rep3_fruits? : ",check1 in rep3_fruits)                                    #列印出banana是否存在於tuple中
check2="orange"                                                                                                         #設定要找的值是orange
print("\nIs the object named 'orange' in the rep3_fruits? : ",check2 in rep3_fruits)                                    #列印出orange是否存在於tuple中









