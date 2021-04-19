#2
# Trump Card

list1 = ["Spade", "Heart", "Diamond", "Clover"]
list2 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
count = 1

for i in list1:
    for j in list2:
        print(count, i, j)
        count += 1

####################################################################################################

# 2-1

list1 = ["Spade", "Heart", "Diamond", "Clover"]
list2_1 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
trump = { } # 딕셔너리 선언
count = 1

for i in list1:
    for j in list2_1:
        trump[count] = [i + " " + j] # 딕셔너리에 저장
        count += 1

print(trump) # 딕셔너리 출력