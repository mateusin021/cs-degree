texto = """
Irene preta
Irene boa
Irene sempre de bom humor.

Imagino Irene entrando no céu:
— Licença, meu branco!
E São Pedro bonachão:
— Entra, Irene. Você não precisa pedir licença.
"""
qtd = 0
for word in texto.split():
    if len(word) >=3:
        qtd +=1
print(qtd)