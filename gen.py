try:
  from colorama import Fore, init, Style
  from random import randint, choices
  from os import system
  from time import sleep
except ModuleNotFoundError:
  print(Fore.RED)
  print("Modüller yükleniyor...")
  system("pip install colorama")
  print("Modüller yüklendi. Programı tekrar çalıştır")
  sleep(3)

live = 0
dec = 0
hits = ['']

def check(no, skt, cvc):
    global live
    global dec
    global hits
    if no.isdigit():
        last_digit = int(str(no)[-1])
        reverse_sequence = list(int(d) for d in str(int(no[-2::-1])))

        for i in range(0, len(reverse_sequence), 2):
            reverse_sequence[i] *= 2

        for i in range(len(reverse_sequence)):
            if reverse_sequence[i] > 9:
                reverse_sequence[i] -= 9

        sum_of_digits = 0
        for i in range(len(reverse_sequence)):
            sum_of_digits += reverse_sequence[i]

        result = divmod(sum_of_digits, 10)

        if result[1] == last_digit:
            cc = """
Live CC :
===============================
Kart Numarası: %s
Son Kullanma Tarihi : %s
CVC/CVV : %s
===============================
                    """ % (no, skt, cvc)
            print(Fore.LIGHTGREEN_EX)
            live += 1
            hit = "Kart no: %s | SKT: %s | CVC/CVV : %s"%(no, skt, cvc)
            hits.append(hit)
            sleep(0.5)

            return cc
        else:
            print(Fore.RED)
            print("Dec CC : %s|%s|%s" % (no, skt, cvc))
            dec += 1
            sleep(0.5)
    else:
        print("[ERROR] \" %s \" is not a valid sequence." % no)

    return ""

init()

print(Fore.RED)
print("""
=========================
     CC Generator
=========================
  Telegram : howertxd
  Discord : howert1337
=========================
""")
print(Fore.BLUE)

try:
  bin = int(input("Bin gir >> "))
  sayi = int(input("Kaç tane üretilsin? >> "))
except ValueError:
  print(Fore.RED)
  print("Sadece sayı girebilirsin!")

for _ in range(sayi):
    random = ''.join(choices('0123456789', k=10))
    no = str(bin).zfill(6) + str(random)
    skt = "%s/%s"%(randint(1,12),randint(24,30))
    cvc = randint(100,999)
    print(check(no, skt, cvc))

print(Fore.BLUE)
print("""
--------------
   Sonuçlar
--------------
Toplam : %s
Live : %s
Dec : %s
--------------
"""%(sayi,live,dec))
islem = int(input("İşlemler\n1 - Live CCleri yazdır\n2 - Çık\n >> "))
if islem == 1:
    system("cls")
    print(Fore.LIGHTGREEN_EX)
    for res in hits:
       result = res + "\n"
       print("Live CC:\n%s "%(result))
else:
    print(Fore.RED)
    print("Çıkış yapılıyor...")
