import matplotlib.pyplot as plt

numeroBarra1 = [1, 3, 5, 7, 9]
tamanhoBarra1 = [2, 3, 7, 1, 0]

# Título do grafico
plt.title("Meu primeiro gráfico")

# Nomes dos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Informar os valores para criar o gráfico de pontos 
plt.scatter(
    numeroBarra1, 
    tamanhoBarra1, 
    label="Meus pontos", 
    color="r", 
    marker="h",
    s=200
)

# Imprime um grafico de linhas
plt.plot(
    numeroBarra1, 
    tamanhoBarra1,
    color="k",
    linestyle=":"
)

# Exibir as legendas
plt.legend()

plt.show()