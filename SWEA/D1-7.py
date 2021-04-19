# KCY
# D1-7

k = int(input())
md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(0, k):
    cal = input()
    year = int(cal[0:4])
    month = int(cal[4:6])
    day = int(cal[6:8])

    print("#%d " %(i+1), end = '')

    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        md[1] = 29
        
    if month <= 0 or month >= 13:
        print(-1)
        
    else:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            if(day>0 and day <32):
                print("%.4d/%.2d/%.2d" %(year, month, day))
            else:
                print(-1)
        else:
            if(month == 2):
                if (day>0 and day<=md[1]):
                    print("%.4d/%.2d/%.2d" %(year, month, day))
                else:
                    print(-1)
            else:
                if(day>0 and day <31):
                    print("%.4d/%.2d/%.2d" %(year, month, day))
                else:
                    print(-1)
