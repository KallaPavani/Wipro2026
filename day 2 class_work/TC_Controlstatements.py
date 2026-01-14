num=8
if num%2==0:
    print("Even")
else:
    print("Odd")

marks=80
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
else:
    print("D")


for i in range(5):
    print(i)

    j=1
while j<=5:
    print(j)
    j+=1
    if j==3:
        break


day=4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
