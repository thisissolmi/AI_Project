# exercise 2

start = int(input("Enter the start day (0~6)>>"))
finish = int(input("Enter the number of days (28~31)>>"))

calendar = {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'}
print("Sun Mon Tue Wed Thu Fri Sat")

for i in range(start):
    print("   ", end=" ")

for day in range(1, finish + 1):
    print(f"{day:3}", end=" ") #날짜간 간격 설정 
    
    if (start + day) % 7 == 0: 
        print()

if (start + finish) % 7 != 0:
    print()

            
    






