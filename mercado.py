from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('###############################################################')
    print('####################### Bem Vindo(a) ##########################')
    print('###################### Valentim House #########################')

    print('Selecione uma opção abaixo')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)    # Aguardar 2 segundo antes de fecha
        exit(0)
    else:
        print('Opção Inválida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('  Cadastrar Produto ')
    print('######################')

    nome: str = str(input('Informe o nome do produto: '))
    preco: float = float(input('Informe o preco do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('  Listar Produtos ')
        print('######################')
        for produto in produtos:
            print(produto)
            print('___________________')
            sleep(1)
    else:
        print('Nenhum produto cadastrado!')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('         Adicione ao carrinho: ')
        print('########################################')
        print('++++++++ Produtos disponíveis ++++++++++')
        for produto in produtos:
            print(produto)
            print('______________________________')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'Produto: {produto.nome} Quantidade: {quant + 1}')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'Produto: {produto.nome} adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'{produto.nome} adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'Código do produto não encontrado: {codigo}')
            sleep(2)
            menu()

    else:
        print('Produto inexistente!')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                sleep(1)
    else:
        print('Carrinho vazio')
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('   Seu carrinho   ')
        print('######################')
        for iten in carrinho:
            for dados in iten.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('___________________')
                sleep(1)
        print(f'Total do seu carrinho: {formata_float_str_moeda(valor_total)}')
        confirmar: int = int(input('Confirme sua compra: \n1 - Confirmar: \n2 - Cancelar: \n'))
        if confirmar == 1:
            print('Compra confirmada!')
            print('Volte sempre!')
            carrinho.clear()
            sleep(3)
        else:
            print('Tem certeza que deseja cancelar?')
            confirmacao: int = int(input('\n1 - Sim, cancelar compra: \n2 - Não, voltar ao pedido: \n'))
            if confirmar == 1:
                carrinho.clear()
                sleep(3)
            else:
                fechar_pedido()
    else:
        print('Carrinho vazio')
        sleep(2)
        menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
