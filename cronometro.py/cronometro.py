from time import  sleep

def cronometro():
    c = int( input('Digite o tempo no cronômetro:'))
    while c > 0:
     c-= 1
     yield c
     sleep(1)
     if c == 6:
         print('esta acabando seu tempo')
     if c == 0:
         print('Acabou o tempo')

t = cronometro()

for tempo in t:
   if tempo % 60 == 0:
       print(f'{tempo}min')
   else:
       print(f'{tempo}s')