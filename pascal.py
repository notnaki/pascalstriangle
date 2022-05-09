import colorama
from colorama import init, Fore

init(convert=True, autoreset=True)

def space(a):
  time = 0
  while time < a:
    print("")
    time += 1

def main(a):
  global list

  a -= 1
  g=a
  b = 2
  list = [1,a]
  z = -1

  if a+1 == 1:
    list.remove(a)

  elif a+1 == 0:
    print("It starts from 1")

  elif a+1 == 2:
    
    list.remove(a)
    list.append(1)
    

  elif a+1 == 3:
    list.remove(a)
    list.append(2)
    list.append(1)
  
  elif a+1 == 5:
    list.remove(a)
    list.append(4)
    list.append(6)
    list.append(4)
    list.append(1)

  else:



    if (a+1)%2 == 0:
      c=a/2
      while b<c:
        a*=((g+z)/b)
        
        list.append(int(a))
        b+=1
        z-=1
      
      while b>=2:
        
        a/=((g+z)/b) 
        list.append(int(a))
        b-=1
        z+=1

      list.append(1)
    elif (a+1)%2 != 0:
      c=(-1+a)/2
      while b<c:
        a*=((g+z)/b)
        h=a
        
        list.append(int(a))
        b+=1
        z-=1
        
      h*=((g+z)/b)
      list.append(int(h))

      
      while b>=2:
        
        h/=((g+z)/b) 
        list.append(int(h))
        b-=1
        z+=1

      list.append(1)

    return(list)


def dirrect_row(a):
  main(a)
  print(list)



def full(to):
  
  p = 1
  time = 1
  g = []

  j = to+to/2
  u = time

  while p <= to:
    main(p)
    while time <= j:
      print(" ",end="")
      time += 0.55
    print(list)
    p+= 1
    u += 1
    time = u
    

tr = True
while tr == True:

    
    
  
    
  space(2)
  print(Fore.CYAN+"0(Direkt Sıra)         "+ Fore.YELLOW+"1(Tüm Sıralar)")
  print("")
  input1 = input("Direkt Sıra mı istersiniz yoksa o gireceğiniz sayıya kadar olan tüm sıraları mı istersiniz ? ")
  if input1 == "0":
    space(2)
    
    print(Fore.LIGHTMAGENTA_EX+"Hangi sırayı istersiniz ? ")
    in_direct = input()
    colorama.Fore.RESET
    main(int(in_direct))
    space(1)
    print(list)

  elif input1 == "1":
    space(2)
    
    print(Fore.LIGHTMAGENTA_EX + "Kaç adet sıra istersiniz ? " + Fore.RESET)
    in_full = input()
    
    space(1)
    full(int(in_full))

  print("Tekrar ister misiniz ?     "+ Fore.GREEN+"y"+ Fore.RESET+"/"+Fore.RED+"n   "+ Fore.RESET)
  input3 = input()
  if input3 == "n":
    tr = False

  elif input3 == "No":
    tr = False

  elif input3 == "NO":
    tr = False

  elif input3 == "no":
    tr = False

  elif input3 == "nO":
    tr = False

  else:
    pass

