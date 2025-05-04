marks =[[70,0,90],[80,90,90],[60,70,70]]
for i in range(3):
    total=marks[i][0]+marks[i][1]+marks[i][2]
    average=round(total/3,2)
    print(f"Student{i+1},Total:{total} Average:{average}")