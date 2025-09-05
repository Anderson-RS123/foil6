import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import textwrap


class Evento:
    def __init__(self, ano, descricao, imagem):
        self.ano = ano
        self.descricao = descricao
        self.imagem = imagem


class Timeline:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, ano, descricao, imagem):
        evento = Evento(ano, descricao, imagem)
        self.eventos.append(evento)

    def entrada_dinamica(self):
        print("=== Inserção de eventos na timeline ===")
        while True:
            try:
                opc = int(input("Digite uma opção:\n1 - Adicionar evento\n2 - Finalizar entrada\n"))
            except ValueError:
                print("Digite apenas 1 ou 2!")
                continue

            if opc == 1:
                try:
                    ano = int(input("Ano do evento: "))
                except ValueError:
                    print("Ano inválido! Tente novamente.")
                    continue
                descricao = input("Descrição do evento: ")
                imagem = input("Caminho da imagem (ex: C:\\Users\\Usuario\\Pictures\\foto.jpg): ")
                imagem = imagem.strip('"').replace("\\", "/")  # corrige barras e aspas
                self.adicionar_evento(ano, descricao, imagem)
                print("Evento adicionado!\n")
            elif opc == 2:
                print("Entrada de eventos finalizada.\n")
                break
            else:
                print("Digite apenas 1 ou 2!")

    def gerar(self, saida_pdf="timeline.pdf"):
        if not self.eventos:
            print("Nenhum evento para exibir!")
            return

        # Distância fixa entre eventos
        espaco = 5
        posicoes = list(range(len(self.eventos) * espaco, 0, -espaco))

        fig, ax = plt.subplots(figsize=(12, 20))

        # Linha central e bolinhas
        ax.vlines(1, min(posicoes) - espaco, max(posicoes) + espaco, color="gray", alpha=0.7)
        ax.scatter([1] * len(posicoes), posicoes, s=200, c="steelblue", zorder=3)

        # Adiciona textos e imagens
        for evento, y in zip(self.eventos, posicoes):
            texto_quebrado = "\n".join(textwrap.wrap(f"{evento.ano} - {evento.descricao}", width=60))
            ax.text(1.1, y, texto_quebrado, va="center", ha="left",
                    fontsize=11, linespacing=1.4)
            try:
                img = mpimg.imread(evento.imagem)
                imagebox = OffsetImage(img, zoom=0.03)
                ab = AnnotationBbox(imagebox, (0.7, y), frameon=False)
                ax.add_artist(ab)
            except FileNotFoundError:
                print(f"Imagem não encontrada: {evento.imagem}")

        # Ajusta limites
        ax.set_xlim(0.4, 1.8)
        ax.set_ylim(0, max(posicoes) + espaco)
        ax.axis("off")

        fig.savefig(saida_pdf, bbox_inches="tight", dpi=300)


# inicio do codigo
if __name__ == "__main__":
    timeline = Timeline()
    
    # Exemplos
    timeline.adicionar_evento(1980, "retirei a descricao e as imagens por questão de privacidade.", r"C:\Users\Usuario\Pictures\foto.jpg")
    timeline.adicionar_evento(2000, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\paimae.jpg")
    timeline.adicionar_evento(2004, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\paimae.jpg")
    timeline.adicionar_evento(2004, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\terneiro.jpg")
    timeline.adicionar_evento(2010, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\terneiro.jpg")
    timeline.adicionar_evento(2013, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\medalha.jpg")
    timeline.adicionar_evento(2015, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\medalha.jpg")
    timeline.adicionar_evento(2018, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\formatura.jpg")
    timeline.adicionar_evento(2021, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\foto.jpg")
    timeline.adicionar_evento(2024, "retirei a descricao e as imagens por questão de privacidade", r"C:\Users\Usuario\Pictures\viagem.jpg")
    # Entrada dinâmica de eventos
    #timeline.entrada_dinamica()

    # Gera PDF com a timeline
    timeline.gerar("timeline2.pdf")

print("Fim")

