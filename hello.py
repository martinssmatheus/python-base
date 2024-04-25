#!/usr/bin/env python3
"""Hello Word Multi Linguas.

Dependendo da lingua configuada no ambiente o programa exibe a
mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./helloy.py
"""
__version__ = "0.1.2"
__autor__ = "Matheus Martins"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!"
}

print(msg[current_language])
