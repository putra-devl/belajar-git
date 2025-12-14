print("====Fahrenheit to Kelvin====")
fahrenheit = float(input("Masukkan Suhu Fahrenheit : "))
celcius = (5/9) * (fahrenheit - 32)
kelvin = (celcius + 273)
print("Suhu dalam Kelvin : ", kelvin)


print("====Kelvin to Fahrenheit====")
kelvin = float(input("Masukkan Suhu Kelvin : "))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit : ", fahrenheit)