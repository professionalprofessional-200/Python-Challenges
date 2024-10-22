#celsius to fareheit

Temperature=float(input("Temperature(celsius):"))

result=((Temperature*9/5)+32)

print(f"{result:.2f} degrees fareheit")

#fareheit to celsius

Temperature=float(input("Temperature(farenheit):"))

result=((Temperature-32)*5/9)

print(f"{result:.2f} degrees celsius")
