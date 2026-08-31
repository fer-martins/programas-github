# PROGRAMA PARA CALCULAR O VALOR LÓGICO DE:
# P OR (Q AND R)
p = input("Digite o valor de P (True/False): ").strip().lower() == 'true'
q = input("Digite o valor de Q (True/False): ").strip().lower() == 'true'
r = input("Digite o valor de R (True/False): ").strip().lower() == 'true'

if p or (q and r):
    print ("verdadeiro")


    print ("testeeeee")
    print ("testeeeee 2")

else:
    print("falso")