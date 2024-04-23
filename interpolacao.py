email_tmpl = """
    Ola, %(nome)s
    
    Tem interesse em comprar o %(produto)s?
    
    Este produto é ótimo para resolver %(texto)s
    
    Clique agora em %(link)s
    
    Apenas %(quantidade)d disponiveis
    
    Preço promocional %(preco).2f
    """

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
       email_tmpl
        % {
           "nome": cliente,
           "produto": "caneta",
           "texto": "Escrever demais",
           "link": "https://canetas.com",
           "quantidade": 1,
           "preco": 50.5
           }
    )
