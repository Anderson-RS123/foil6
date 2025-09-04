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
    timeline.adicionar_evento(1980, "Pais se conheceram - Os pais se conheceram quando eram jovens. Se eu não engano, eram vizinhos.", r"C:\Users\Usuario\Pictures\foto.jpg")
    timeline.adicionar_evento(2000, "Ficaram Juntos - Em torno dessa data, os 2 ficaram juntos.  Pai: Aldo Afonso Menegassi(55 anos). Gosta de viver em contato com a natureza, pescar, assistir futebol. Mãe: Lisete Steuernagel(54 anos). Gosta de conversar, sempre está ativa, gosta de cuidar do ambiente que vive. Situação atual: estão separados a cerca de 19 anos.", r"C:\Users\Usuario\Pictures\paimae.jpg")
    timeline.adicionar_evento(2004, "Meu nascimento - Meu nascimento em 19/03/2004, signo peixes. Apelido quando pequeno: Neni. Irmão mais velho: Dionas(10 anos e 5 meses de diferença). Características quando pequeno: Gostava de bricar com carinhos e jogar futebol. Brincava com os animais, chorava bastante, ficava bastande doente.  Imagens mais antigas: Minha mãe ensinando matemática básica; Buscar lenha para o fogão com um carrinho de madeira. Adulto-mãe: Minha vó materna.", r"C:\Users\Usuario\Pictures\paimae.jpg")
    timeline.adicionar_evento(2004, "0 a 5 anos - Ficava bastante doente, por causa da bronquite asmática(já estou curado); Pais se separaram; Batizado; Idade que começei a falar(11 meses).", r"C:\Users\Usuario\Pictures\terneiro.jpg")
    timeline.adicionar_evento(2010, "5 a 7 anos - Início na escola; Viajar de ônibus; 1° Professora: Patrícia; Os primeiros dias na escola, eu chorava bastante; Aprender a ler e escrever; Brincava sozinho, fazendo estradas no galpão; Andar de bicicleta sem rodinhas;", r"C:\Users\Usuario\Pictures\terneiro.jpg")
    timeline.adicionar_evento(2013, "8 a 10 anos - Primeira medalha olímpica municipal, de 2° lugar, em salto em altura; Gostava de jogar futebol; Melhores amigos: Gadiel, Maicon, Gabriel; Dirigia o carro do meu pai(mexia apenas o volante)", r"C:\Users\Usuario\Pictures\medalha.jpg")
    timeline.adicionar_evento(2015, "10 a 12 anos - Pescar com meu pai; Nasceu meu irmão mais novo por parte de pai; Mais medalhas das olimpiadas; Inventava bricadeiras de futebol;", r"C:\Users\Usuario\Pictures\medalha.jpg")
    timeline.adicionar_evento(2018, "13 a 15 anos - Formatura no 9° ano; Início no ensino médio; Jogava jogos como: Call of Dutty, Need for Speed, GTA San Andreas, CS, jogos de futebol no celular, o principal: Dream League Soccer; Dirigia trator;", r"C:\Users\Usuario\Pictures\formatura.jpg")
    timeline.adicionar_evento(2021, "15 a 18 anos - Pandemia, só ficava em casa; Formatura no Ensino Médio; Começei a morar na cidade; Início na faculdade; Estágio de Assistente Técnico de computadores; CNH; Serviço Militar Obrigatório;", r"C:\Users\Usuario\Pictures\foto.jpg")
    timeline.adicionar_evento(2024, "18 até hoje - Emprego na área; Viagem Foil para Minas Gerais e viagem internacional para Itália e França. Compra do carro;", r"C:\Users\Usuario\Pictures\viagem.jpg")
    # Entrada dinâmica de eventos
    #timeline.entrada_dinamica()

    # Gera PDF com a timeline
    timeline.gerar("timeline2.pdf")

print("Fim")
