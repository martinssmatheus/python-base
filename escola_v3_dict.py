#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lisa de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"


# DADOS
sala1 = set(["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"])
sala2 = set(["Joao", "Antonio", "Carlos", "Maria", "Isolda"])

aula_ingles = set(["Erik", "Maia", "Joana", "Carlos", "Antonio"])
aula_musica = set(["Erik", "Carlos", "Maria"])
aula_danca = set(["Gustavo", "Sofia", "Joana", "Antonio"])

atividades = {
    "Ingles": aula_ingles,
    "Musica": aula_musica,
    "Dança": aula_danca,
}

for chave, valor in atividades.items():
    print(f"***Aula de {chave}***")
    
    atividade_sala1 = sala1 & valor
    atividade_sala2 = sala2 & valor

    print(
        f"\nSala-1 {atividade_sala1}"
        f"\nSala-2 {atividade_sala2}"
        f"\n{'-' * 50}"
    )
