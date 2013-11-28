import os

def menu():
  print ("__        _______ _     ____ ___  __  __ _____\n\ \      / / ____| |   / ___/ _ \|  \/  | ____|\n \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _| \n  \ V  V / | |___| |__| |__| |_| | |  | | |___ \n   \_/\_/  |_____|_____\____\___/|_|  |_|_____|\n")
  print ("1) Modificare il file GRUB.")
  print ("2) Modificare il file MKINITCPIO.conf.")
  print ("3) Apri il taskmanager (HTOP).")
  print ("4) Modificare le config di XORG.")
  print ("5) Modificare il file FSTAB.")
  print ("6) Uscita.\n")
  x = input(":: Come vuoi procedere >> ")
  return x



x = menu()
while x < "0" or x > "6":
   x = input("La scelta non è valida!! Reisenriscila:\n >>>  ")

while x != "6":

   
 if x == "1":
   os.system("sudo nano /etc/default/grub")
   y = input("## Vuoi ri-generare il file GRUB.cfg?[S,n] >>  ")
   if y == "S" or y == "s":
     os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
 
 elif x == "2": 
   os.system("sudo nano /etc/mkinitcpio.conf")
   y = input("## Vuoi ri-generare il kernel da preset? [S,n] >>  ")
   if y == "S" or y == "s":
     os.system("sudo mkinitcpio -p linux")

 elif x == "3":
   os.system("htop")
 
 elif x == "4":
   l = os.listdir("/etc/X11/xorg.conf.d")
   for i in range(len(l)):
     print(i,')' + l[i])
   y = eval(input("## Quale file vuoi modificare >> "))
   if y < 0 or y > len(l):
     print("La scelta non è valida!!")
   else:
     os.system("sudo nano /etc/X11/xorg.conf.d/"+l[y])
 
 elif x == "5":
   os.system("sudo nano /etc/fstab")
   
 os.system('clear')
 x = menu()
 
