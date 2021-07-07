import random
import time
print ('Введите help для помощи.')
while True:
    x=input()
    if x == "help":
        print("Новая игра: введите шанс выигрыша в процентах.")
        print ("Выход: exit .")
        print ("Рулетка: ruletka.")
    elif x == "ruletka":
        print("Введите кол-во чисел")
        vfr=input()
        if vfr.isdigit() == False:
            print('Неверная команда, для получения помощи введите help .')
        else:    
            x=random.randint(0, int(vfr))
            print("Введите число")
            qwerty=input()
            if qwerty.isdigit() == False:
                print('Неверная команда, для получения помощи введите help .')
            else:
                if int(qwerty)==x:
                    print ("Вы выиграли.")
                    time.sleep(0.3)
                    print ("Приходи ещё :)")
                else:
                    print ("Вы проиграли.")
                    time.sleep(0.3)
                    print ("Не расстраивайтесь!")
                    time.sleep(0.3)
                    print ("Приходи ещё :)")
            
    elif x == "exit":
        break
    elif x.isdigit() == False:
        print('Неверная команда, для получения помощи введите help .')
    elif int(x)>100:
        print('Неверная команда, для получения помощи введите help .')
    else:
        
        #x=x-30
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        if random.randint(0, 100)<=int(x):
            print ("Вы выиграли.")
        else:
            print ("Вы проиграли.")
            time.sleep(0.3)
            print ("Не расстраивайтесь!")
            time.sleep(0.3)
        print ("Приходи ещё :)")
