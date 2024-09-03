tempCelsius = [5, 23, 17, 10, 2]

tempFH = list(map(lambda x: (x*9/5)+35 , tempCelsius))
print(f'Temperaturas em Fahrenheit: {tempFH}')