n = int(input());
mas = [];
i = 0;
while i < n:
    mas += input();
    i += 1;
  #  mas += [i];
q = 1
for i in mas:
    if i != mas[q] and i < mas[q]:
        print(int(mas[q])-int(i))
    elif i != mas[q] and i >= mas[q]:
        print(-1)
        break;
    if q < n-1:    
        q +=1;
    
    
