running = True
while running:
    a = input("Enter your name(to end enter stop)")
    print(f"You entered: {a}")
    if a == "stop":
        print("Program stopped")
        running = False

a = 5
i = 1
while i<=10:
    print(f"{a}*{i} ={a*i}")
    i+=1

squres = 1
while squres<=10:
    print(f"squre of {squres} = {squres**2}")
    squres+=1

odd = 1
sum = 0
while odd<=30:
    print(odd)
    sum+=odd
    odd+=2
print("Sum of odd num",sum)

word = "python"
vowels = "aeiouAEIOU"
count = 0
i = 0
while i< len(word):
    print(word[i])
    if word[i] in vowels:
        count += 1
    i+=1
print(count)

