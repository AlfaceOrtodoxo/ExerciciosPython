

print('------ BANCO ABC ------')
asacar = int(input('Quanto você quer sacar? R$  '))
print('------ AGUARDE ------')

ced = 100
totced = 0

while True:
    if asacar >= ced:
        asacar -= ced
        totced += 1
    else:
       if totced > 0:
         print(f'Total de cédulas de R$ {ced}: {totced}.')
       totced = 0
       if ced == 100:
          ced = 50
       elif ced == 50:
          ced = 20
       elif ced == 20:
          ced = 10
       elif ced == 10:
          ced = 5
       elif ced == 5:
          ced = 2
       elif ced == 2:
          ced = 1
       if asacar == 0:
          break
       
print('------ VOLTE SEMPRE!! ------')


        

                            




