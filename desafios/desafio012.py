preco = float(input('Digite o preço do produto: '))
desconto = preco - (preco * 5/100)
print(f'O preço do produto que custa {preco:.2f}R$, com o desconto de 5% aplicado custa: {desconto:.2f}R$')
