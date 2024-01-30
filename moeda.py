# Script de conversão de moeda em python
# Autor - CK
# Data - 1/2024
# Conclusão
import time

valor = ""
conversao = ""
int_valor = 0.0
int_conversao = 0.0


print("""\033[32m                                                                                                                                                                      
                         s                                                                                                                                             
        CCCCCCCCCCCCC                                                                                                                                                 
     CCC::::::::::::C                                                                                                                                                 
   CC:::::::::::::::C                                                                                                                                                 
  C:::::CCCCCCCC::::C                                                                                                                                                 
 C:::::C       CCCCCC   ooooooooooo   nnnn  nnnnnnnn vvvvvvv           vvvvvvv eeeeeeeeeeee    rrrrr   rrrrrrrrr       ssssssssss     aaaaaaaaaaaaa     ooooooooooo   
C:::::C               oo:::::::::::oo n:::nn::::::::nnv:::::v         v:::::vee::::::::::::ee  r::::rrr:::::::::r    ss::::::::::s    a::::::::::::a  oo:::::::::::oo 
C:::::C              o:::::::::::::::on::::::::::::::nnv:::::v       v:::::ve::::::eeeee:::::eer:::::::::::::::::r ss:::::::::::::s   aaaaaaaaa:::::ao:::::::::::::::o
C:::::C              o:::::ooooo:::::onn:::::::::::::::nv:::::v     v:::::ve::::::e     e:::::err::::::rrrrr::::::rs::::::ssss:::::s           a::::ao:::::ooooo:::::o
C:::::C              o::::o     o::::o  n:::::nnnn:::::n v:::::v   v:::::v e:::::::eeeee::::::e r:::::r     r:::::r s:::::s  ssssss     aaaaaaa:::::ao::::o     o::::o
C:::::C              o::::o     o::::o  n::::n    n::::n  v:::::v v:::::v  e:::::::::::::::::e  r:::::r     rrrrrrr   s::::::s        aa::::::::::::ao::::o     o::::o
C:::::C              o::::o     o::::o  n::::n    n::::n   v:::::v:::::v   e::::::eeeeeeeeeee   r:::::r                  s::::::s    a::::aaaa::::::ao::::o     o::::o
 C:::::C       CCCCCCo::::o     o::::o  n::::n    n::::n    v:::::::::v    e:::::::e            r:::::r            ssssss   s:::::s a::::a    a:::::ao::::o     o::::o
  C:::::CCCCCCCC::::Co:::::ooooo:::::o  n::::n    n::::n     v:::::::v     e::::::::e           r:::::r            s:::::ssss::::::sa::::a    a:::::ao:::::ooooo:::::o
   CC:::::::::::::::Co:::::::::::::::o  n::::n    n::::n      v:::::v       e::::::::eeeeeeee   r:::::r            s::::::::::::::s a:::::aaaa::::::ao:::::::::::::::o
     CCC::::::::::::C oo:::::::::::oo   n::::n    n::::n       v:::v         ee:::::::::::::e   r:::::r             s:::::::::::ss   a::::::::::aa:::aoo:::::::::::oo 
        CCCCCCCCCCCCC   ooooooooooo     nnnnnn    nnnnnn        vvv            eeeeeeeeeeeeee   rrrrrrr              sssssssssss      aaaaaaaaaa  aaaa  ooooooooooo   

\033[0m""")


"""time.sleep(1)
for i in range(10):
    print("")
int_valor = float(input("Insira: "))
conversao = input('''
                  1- Euro
                  2- Dollar
                  3- Real
                  4- Libra
                  5- Rublo Russo
                  6- 
                  
                  Conversão: ''')

if conversao == "1":
    print(int_valor)
elif conversao == "2":
    print(f"{int_valor* 1.08} $")
"""



def verificar_command(command):
    if command == "exit":
        exit()
    elif command == "/login":
        user = str(input(" "))
        password = str(input("password: "))
        if user and password == user and password:
            print(f"Bem vindo, {user}: ")
    else:
        print("Error or command doesn't exist")

user = "André"
commando = ""
while commando != "exit":
    commando  = input("")
    verificar_command(commando)

    
