import json

try:
    with open("banco de dados.json", "r") as dado:
        voos = json.load(dado)
except FileNotFoundError:
    voos = {}

def add_voos(n_voo, partida, destino, data, passageiro):
    infos_voos = {
        'partida': partida,
        'destino': destino,
        'data': data,
        'passageiro': passageiro,
    }

    voos[n_voo] = infos_voos
    salvar_json()

def mostrar_voos():
    for n_voo, info in voos.items():
        print(f"Voo: {n_voo}")
        print(f"De: {info['partida']}") 
        print(f"Para: {info['destino']}")
        print(f"Data: {info['data']}")
        print(f"Passageiros: {info['passageiro']}")
        print()

def deletar_json(n_voo):
    if n_voo in voos:
        del voos[n_voo]
        salvar_json()
        print(f"O voo {n_voo} foi deletado!")
    else:
        print(f"O voo {n_voo} não foi encontrado.")

def salvar_json():
    with open("banco de dados.json", 'w') as dado:
        json.dump(voos, dado)

if __name__ == "__main__":
    while True:
        print("Bem-vindo ao sistema de reserva de voos do IFBA!")
        print("1. Criar voo")
        print("2. Deletar voos")
        print("3. Mostrar voos")
        print("4. Sair")
        
        pergunta = input("Selecione uma opção: ")

        if pergunta == "1":
            n_voo = input("Digite por favor o número do voo: ")    
            partida = input("Digite onde será a partida: ")
            destino = input("Digite onde será o destino: ")
            data = input("Digite a data do voo: ")
            passageiro = input("Digite o nome dos passageiros: ")
            print("Voo registrado com sucesso!")
            add_voos(n_voo,partida,destino,data,passageiro)

        elif pergunta == "2":
            n_voo = input("Digite o voo que deseje apagar ")
            deletar_json(n_voo)

        elif pergunta == "3":
            mostrar_voos()

        elif pergunta =="4":
            break

        else:
            print("Opção invalida")
