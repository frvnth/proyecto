# titulo del programa

print("*"*60)
print("  calculadora01")
print("*"*20)


#solicitar dato por consola
numero1 = float(input("introducir primer numero:"))
numero2 = float(input("introducir segundo numero:"))

#imprimir operatoria
print("la suma es: ", numero1 + numero2)
print("la resta es: ", numero1 - numero2)
print("la multiplicacion es: ", numero1 * numero2)
print("la division es: ", numero1/numero2)

# este imput mantiene abierto el programa
input()

if __name__ == '__main__':
	sys.exit(main())