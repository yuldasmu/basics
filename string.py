msg= "hello world"
print(msg)
#concatinations
fullname="Mekhribon Yuldasheva"
msg1= fullname.upper()+ ",\n\t"+msg.title()
print(msg1)

print(f"{fullname.upper()},\n\t\t\t{msg}")
#fstring
fullname= "Mekhribon Yuldasheva"
fullname= "Mekhribon Yuldasheva"
msg= 'She is one of the best students in the Python class...'
msg= 'She is one of the best students in the Python class...'
print(f"{msg.title()} ',' {fullname.upper()}")

#numbers
print("\n\t\t\tIntegers*******************")
num = 6
num2 = 10
print(f"num + num2= { num + num2}")
print(f"num2 - num= { num2 - num}")
print(f"num * num2= { num * num2}")
print(f"num2 / num= { num2 / num}")

print("Value of num is:" + str(num))
print(f"num + num2 = " + str(num))

num3 = "785"
print( f"num + num3 = {num + int(num3)}")

print(f"15*2 = {15*2}")
print(f"15**2 = {15**2}")
num4= 456.25
print(f"num4 / num= { num4 / num}")

num5= int(36.45)
print(f"num5 / num= { num5 / num}")

#Exercise
name = "Walt Disney"
quote= "'The way to get started is to quit talking and begin doing'"
print(f"{quote} said by {name}!!!")

number="4"
msg= "I was born in january"
print(f"{msg} birthday>>>>{number.isdigit()}")
print(f"{msg} {number}")
universe_age= 14_000_000_000
print(universe_age)

