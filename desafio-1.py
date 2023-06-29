#TODO: Imprimir a saída no padrão definido no enunciado deste desafio.
#Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings.

nomeRestaurante = input()
tempoEstimadoEntrega = int(input())


def mensagem_tempo_entrega(nomeRestaurante, tempoEstimadoEntrega):
    mensagem = f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."
    return mensagem
    
mensagem = mensagem_tempo_entrega(nomeRestaurante, tempoEstimadoEntrega)
print(mensagem)