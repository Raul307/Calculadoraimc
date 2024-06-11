Altura = float(input("digite sua altura"))
print(Altura)
Peso = float(input("digite seu peso"))
print(Peso)
Altura2 = Altura**2
IMC = Peso/Altura2
print(IMC)
if (IMC <=18):
    print("abaixo do peso")
    print("meu amigo vamos comer mais um pouco, soprou vuou")
if (IMC >18 and IMC <=24):
    print("peso normal")
    print("você tem meu parabens continue assim, faça uma academia tambem")
if (IMC >25 and IMC <=29):
    print("sobrepeso")
    print("meu amigo vamos procurar uma dieta, academia um pouco de amor proprio")
if (IMC >30 and IMC <=34):
    print("obesidade grau I")
    print("mano tem gente preocupado, vamo exercitar parar de comer muito")
if (IMC >35 and IMC <=39):
    print("obesidade grau II")
    print("meu amigo por isso tem gente morando na rua, come ate reboco de parede")
if (IMC >=40):
    print("obesidade grau III")
    print("...")