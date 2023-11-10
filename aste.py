def lasit_datni():
    #pajautāsim ievadīt datnes nosaukumu
    datne_nosaukums=input("Ievadīt datnes nosaukumu: ")
    try:
    #kā ielādēt datnes saturu?
        with open(datne_nosaukums, 'r') as ff:
            saturs=ff.read()
            #print(saturs) pārliecinājos par to, ka datne ir skaitļi
            #izvadi simbolu skaitu datnē;
            print(f"simbolu skaits datnē ir {len(saturs)}")

            #Izvadīt pirmos desmit smbolus
            print(f"Pirmie desmit simboli ir:{saturs[:10]}")

            #Izvadi pirmo un pēdējo simbolu
            print(f"Izvadīt pirmo un pēdējo simbolu: {saturs[0]} un {saturs[-1]}")
            
    except FileNotFoundError:
        print("Datne nav atrasta!!!")
    except ValueError:
        print("Datu kļūda!!!")


if __name__=="__main__":
    lasit_datni()