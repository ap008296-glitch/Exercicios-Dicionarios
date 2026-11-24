import csv
moedas = {}
with open("moedas (1).csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        if not linha:
         continue 

        codigo = linha[0].strip().upper()
        nome = linha[2].strip()
        cotacao = float(linha[3].replace(",", "."))
     
        moedas[codigo] = {
            "nome": nome,
            "cotacao": cotacao
        }

valor_reais = float(input("Informe o valor em R$: ").replace(",", "."))
moeda_destino = input("Informe a moeda do destino: ").strip().upper()

if moeda_destino in moedas:
    nome_moeda = moedas[moeda_destino]["nome"]
    cotacao = moedas[moeda_destino]["cotacao"]
    valor_convertido = valor_reais / cotacao

    print(f"Moeda: {nome_moeda}")
    print(f" Valor convertido: {valor_convertido:.2f}")

else:
    print("Moeda não encontrada")    