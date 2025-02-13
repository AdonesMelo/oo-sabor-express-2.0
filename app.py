from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Paozinho', 2.00, 'O melhor da cidade')
prato_pao.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 20.00, 'Gelado', 'Médio', 'O sabor incomparável')
sobremesa_pudim.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)

restaurante_praca.receber_avaliacao('adones', 4.8) # Exemplo 

restaurante_praca.alternar_status() # Para alterna o status ativado/desativado

def main():  
    Restaurante.listar_restaurantes() #Para listar todos restaurante
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()