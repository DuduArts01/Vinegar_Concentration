from os import system

continueLoop = True
verificationLoop = True

while(continueLoop):
    system("clear")
    #clear console

    print("----------------------------------------------------------------------")
    print("\n                 Cálculo de Concentração do Vinágre\n")
    #Vinegar Concentration Calculation title
    print("----------------------------------------------------------------------")
    print("Made by DuduArts01\n")

    Ma = float(input("Massa Molar do ácido acético(em grama): "))
    #Mole mass in grama
    #molar mass of the titled

    print("\n")

    mb = float(input("Concentração do Titulante(em gramas): "))
    # mb is the concentration of the titrant in gramas

    print("\n")

    vinager = float(input("Volume do vinagre utilizado antes de todo experimento(em mL): "))

    print("\n")

    vinager_join_H2O = float(input("Volume da solução do vinagre com a água(em mL): "))
    #Volume vinager plus water in mL 

    print("\n")

    Vb = float(input("Volume gasto da base NaOH(em mL): "))
    # Volume spent of base NaOH

    Vb /= 1000
    # Convert mL in L

    #nA = nB (number of moles of acid = number of moles of base(NaOH))

    ma = Ma * mb * Vb 
    # ma/Ma = Mb * Vb (Mass of acid over molar mass = base mass times the volume added)

    uAcid = ma * vinager_join_H2O / vinager
    # Calculate the concentration of acetic acid from before adding water to after adding water in a larger volume 

    percentualAcid = uAcid * 100 / vinager
    # Calculate the percentage of acetic acid that was added to the water and added to the titrant

    print("\n----------------------------------------------------------------------")
    print(f"\nConcentação Percentual do Ácido Acético: {percentualAcid:.2f}%\n")
    print("----------------------------------------------------------------------")
    
    input("Pressione enter para continuar!")

    while(verificationLoop):
        system("clear")
        print("----------------------------------------------------------------------")
        print("\n                 Cálculo de Concentração do Vinágre\n")
        #Vinegar Concentration Calculation title
        print("----------------------------------------------------------------------")
        print("Made by DuduArts01\n")

        verificationContinueLoop = input("Deseja continuar? [S/N]: ").upper()

        if(verificationContinueLoop == 'N'):
            continueLoop = False
            verificationLoop = False
        elif(verificationContinueLoop == 'S'):
            verificationLoop = False
        else:
            print("Você digitou a letra errado, por favor, digite novamente a letra correta!")
            input("Pressione enter para continuar!")

system("clear")
print("----------------------------------------------------------------------")
print("\n                 Cálculo de Concentração do Vinágre\n")
#Vinegar Concentration Calculation title
print("----------------------------------------------------------------------")
print("Made by DuduArts01\n")
print("----------------------------------------------------------------------")
print("                     Programa Encerrado")
print("----------------------------------------------------------------------\n")
