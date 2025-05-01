temperature = []
for i in range(5):
    temp = float(input(f"Enter temperature {i+1}: "))
    temperature.append(temp)
avg = sum(temperature)/5
print("Avg. temperature: ",avg)
