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
__version__ = "0.1.3"
__autor__ = "Matheus Martins"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    # TODO tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
    

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO usar repetição
    if current_language is None:
        current_language = input(
            "Choose a language:"
        )

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!"
}

print(
    msg[current_language] * int(arguments["count"])
)
