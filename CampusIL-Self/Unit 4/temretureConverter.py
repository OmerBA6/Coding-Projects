
temperature = input("Enter the temperature: ")
temperature_as_a_number = float(temperature[:len(temperature) - 1])

if(temperature[-1] == 'C' or temperature[-1] == 'c'):
    print(str((temperature_as_a_number * 9 / 5) + 32) + 'F')
elif(temperature[-1] == 'F' or temperature[-1] == 'f'):
    print(str((temperature_as_a_number - 32) * 5 / 9) + 'C')
else:
    print("Unknown Error!")
