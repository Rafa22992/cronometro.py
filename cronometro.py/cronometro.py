from time import  sleep

bordas = '-' * 15

def cronometro():
    c = int( input('Digite o tempo no cronômetro: '))
    print(bordas)
    while c > 0:
     c-= 1
     yield c
     sleep(1)
     if c == 6:
         print('=' * 15)
         print('esta acabando seu tempo')
         print('=' * 15)
     if c == 0:
         print('=' * 15)
         print('Acabou o tempo')
         print('=' * 15)

t = cronometro()

for tempo in t:
   if tempo % 60 == 0:
       formata_min = f'{tempo}min'
       min = f'{formata_min:_^15}'
       print(f'{min}')
       print(bordas)

   else:
       formata_seg = f'{tempo}s'
       seg = f'{formata_seg:-^15}'
       print(f'{seg}')
       print(bordas)