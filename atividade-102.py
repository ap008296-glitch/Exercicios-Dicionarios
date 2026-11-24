print("Programa que solicita o nome e a idade de 10 pessoas")
print()

print("GRUPO 1: Menores de 18 anos:")
print("-"* 30)
menores = [p for p in pessoas if p["idade"] < 18]

if menores:
    for p in menores:
        print(f"Nome: {p["nome"]: <20} idade: {p["Idade"]} anos")
else:
    print("Nenhuma pessoa cadastrada neste grupo")

print("\n" + "=" * 40)   
print("GRUPO 2: 18 anos ou mais")
print("-" * 30)
maiores = [p for p in pessoa if p["idade"] >= 18]

if maiores:
    for p in maiores:
        print(f"Nome: {p["nome"]:<20} idade: {p["idade"]} anos")
else:
    print("Nenhuma pessoa cadastrada neste grupo")        
