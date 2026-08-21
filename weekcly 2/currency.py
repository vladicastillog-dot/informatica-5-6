def main():
    pesos = float(input("What do you have left in pesos?: "))
    soles = float(input("What do you have left in soles?: "))
    reais = float(input("What do you have left in reais?: "))

    colombia = pesos/3100.27
    peru = soles/3.37
    brazil = reais/5.21

    Usa = colombia + peru + brazil
    Mex = Usa * 17.07
    Usa = round(Usa,2)
    Mex = round(Mex,2)
    print(f"Usa{Usa}" )
    print (f"Mex{Mex}" )






if __name__== "__main__":
        main()
