import pygame, sys, pandas
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN, KEYDOWN, K_RETURN, K_ESCAPE
from math import ceil
DEAD = 0
ALIVE = 1
FPS = 10
WIDTH = 100
HEIGHT = 50
CELL_SIZE = 15
PROPORTION = 0.8
GAME = None
DEFAULT_FILL_COLORS = {
    'white': '#ffffff',
    'assets': '#688afc',
    'red': '#ff0000',
    'green': '#00ff00',
}


# klasa ktora wyswietla okno gry
class Board:
    def __init__(self, w, h, cs=10):
        self.w = int(w)
        self.h = int(h)
        self.cs = int(cs*PROPORTION)
        self.surface = pygame.display.set_mode((w*PROPORTION, h))
        pygame.display.set_caption("Game of life")

    # główna metoda odpowiedzialna za wyświetlanie rzeczy na ekranie
    def draw(self, buttons, *args):
        black = (0, 0, 0)
        white = (255, 255, 255)
        self.surface.fill(white)

        # rysowanie kratownicy
        for x in range(0, int(self.w*PROPORTION)+1):
            if x % self.cs == 0:
                pygame.draw.line(self.surface, black, (x, 0), (x, int(self.h*PROPORTION)))

        for y in range(0, int(self.h*PROPORTION)+1):
            if y % self.cs == 0:
                pygame.draw.line(self.surface, black, (0, y), (self.w, y))

        # rysowanie komorek
        for drawable in args:
            drawable.drawCells(self.surface)

        # rysowanie przyciskow
        for drawable in buttons:
            drawable.process()
            drawable.drawButton(self.surface)

        pygame.display.update()


# klasa ulatwiajaca nam tworzenie przyciskow
class Button:
    # mozemy okreslic polozenie przycisku, oraz jego wymiary, a takze czcionke (rodzaj oraz rozmiar) oraz okreslic jaką funkcje bedzie dany przycisk wywolywal
    # mozemy takze sprawic zeby mozliwe bylo ptrzytrzymanie przycisku dluzej
    def __init__(self, x, y, width, height, font, fontPaddingX=0, fontPaddingY=0, buttonText="Button", onclick=None, longPress=False, oneColor=False, color=None):
        self.x = x
        # Y liczony od dolu ekranu, do dolu przycisku -> lewy dolny rog przycisku
        global HEIGHT, CELL_SIZE
        self.y = HEIGHT * CELL_SIZE - y - height
        self.width = width
        self.height = height
        self.font = font
        self.onClick = onclick
        self.onePress = longPress
        self.fontPaddingX = fontPaddingX
        self.fontPaddingY = fontPaddingY
        self.alreadyPressed = False
        self.fillColors = {
            'normal': '#d4d4d4',
            'hover': '#c4c4c4',
            'pressed': '#999999',
            'disabled': '#383838',
        }

        if color is not None:
            self.fillColors['normal'] = color
        self.currentColor = self.fillColors['normal']
        self.color = color
        self.oneColor = oneColor
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonText = buttonText
        self.text_surface = self.font.render(self.buttonText, True, (0, 0, 0))
        self.textCenter = ((self.x + fontPaddingX), (self.y + fontPaddingY))

    def drawButton(self, board):
        pygame.draw.rect(board, self.currentColor, self.buttonRect)
        board.blit(self.text_surface, self.textCenter)

    def updateButton(self):
        self.currentColor = self.color
        self.text_surface = self.font.render(self.buttonText, True, (0, 0, 0))
        self.textCenter = ((self.x + self.fontPaddingX), (self.y + self.fontPaddingY))

    def process(self):
        if self.oneColor:
            return
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.currentColor = self.fillColors['hover']
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.currentColor = self.fillColors['pressed']
                if self.onePress:
                    self.onClick()
                elif not self.alreadyPressed:
                    self.onClick()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        else:
            self.currentColor = self.fillColors['normal']


# glowna klasa gry, odpowiada za stworzenie ekranu, populacji komorek, oraz za rozmieszczenie przyciskow i ich funkcjonalnosci
class Game:
    def __init__(self, w, h, cs=10):
        # Gra
        self.started = None
        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.population = Population(w, int(h), int(cs * PROPORTION))
        self.w = w
        self.h = h
        self.cs = cs

        # Przyciski
        pygame.font.init()
        self.ButtonsFont = pygame.font.SysFont("Arial", 20)
        self.TextFont = pygame.font.SysFont("Arial", 15)
        self.buttons = self.CreateButtons()
        self.board = Board(w * cs, h * cs, cs)

    def CreateButtons(self):
        # w przyciskach Y liczony jest od dolu do lewego dolnego rogu przycisku
        d = [
            Button(20, 80, 120, 50, self.ButtonsFont, buttonText="Play/Pause", onclick=self.StartStop, fontPaddingY=15, fontPaddingX=12),
            Button(20, 20, 120, 50, self.ButtonsFont, buttonText="Exit", onclick=self.ExitGame, fontPaddingY=15, fontPaddingX=40),
            Button(150, 20, 120, 50, self.ButtonsFont, buttonText="Export", onclick=self.Export, fontPaddingY=15, fontPaddingX=30),
            Button(150, 80, 120, 50, self.ButtonsFont, buttonText="Import", onclick=self.Import, fontPaddingY=15, fontPaddingX=30),
            Button(280, 20, 55, 50, self.ButtonsFont, buttonText="+", onclick=self.Enlarge, fontPaddingY=15, fontPaddingX=18),
            Button(345, 20, 55, 50, self.ButtonsFont, buttonText="-", onclick=self.Reduce, fontPaddingY=13, fontPaddingX=24),
            Button(280, 80, 120, 15, self.TextFont, buttonText="Resize Window:", fontPaddingY=0, fontPaddingX=10, oneColor=True, color=DEFAULT_FILL_COLORS['white']),
            Button(410, 20, 120, 50, self.ButtonsFont, buttonText="Clear", onclick=self.Clear, fontPaddingY=15, fontPaddingX=35),
            Button(540, 115, 120, 15, self.TextFont, buttonText="Assets:", fontPaddingY=0, fontPaddingX=10, oneColor=True, color=DEFAULT_FILL_COLORS['white']),
            Button(670, 80, 120, 50, self.ButtonsFont, buttonText="Worm", fontPaddingY=15, fontPaddingX=35, onclick=self.loadWorm, color=DEFAULT_FILL_COLORS['assets']),
            Button(670, 20, 120, 50, self.ButtonsFont, buttonText="Oscilator 1", fontPaddingY=15, fontPaddingX=15, onclick=self.loadOs1, color=DEFAULT_FILL_COLORS['assets']),
            Button(800, 80, 120, 50, self.ButtonsFont, buttonText="Heart", fontPaddingY=15, fontPaddingX=30, onclick=self.loadHeart, color=DEFAULT_FILL_COLORS['assets']),
            Button(800, 20, 120, 50, self.ButtonsFont, buttonText="Infinite 1", fontPaddingY=15, fontPaddingX=25, onclick=self.LoadInf1, color=DEFAULT_FILL_COLORS['assets']),

        ]
        return d

    # funkcjonalnosci przyciskow
    def Export(self):
        data = pandas.DataFrame(self.population.generation)
        data.to_json('save.json')

    def Importer(self, name):
        try:
            boardData = pandas.read_json(name)
            self.buttons[3].color = DEFAULT_FILL_COLORS['green']
            self.buttons[3].buttonText = "Imported!"
            self.buttons[3].fontPaddingX = 15
            self.buttons[3].updateButton()
        except FileNotFoundError:
            self.pause("save not found")
            self.buttons[3].color = DEFAULT_FILL_COLORS['red']
            self.buttons[3].buttonText = "Not Found!"
            self.buttons[3].fontPaddingX = 15
            self.buttons[3].updateButton()
            return

        global WIDTH, HEIGHT
        boardSize = boardData.shape
        WIDTH = boardSize[0]
        HEIGHT = boardSize[1]

        if WIDTH != self.w or HEIGHT != self.h:
            self.Resize()
        self.population.generation = boardData.values.tolist()

    def Import(self):
        self.Importer('save.json')

    def loadWorm(self):
        self.Importer('worm1.json')

    def loadOs1(self):
        self.Importer('oscilator1.json')

    def loadHeart(self):
        self.Importer('heart.json')

    def LoadInf1(self):
        self.Importer('infinite1.json')

    def StartStop(self):
        if self.started is None or self.started is False:
            self.resume()
        else:
            self.pause()

    def ExitGame(self):
        pygame.quit()
        sys.exit()

    def Clear(self):
        self.started = None
        del self.population
        self.population = Population(self.w, int(self.h), int(self.cs * PROPORTION))

    def Resize(self):
        self.w = WIDTH
        self.h = HEIGHT
        del self.board
        del self.population
        self.board = Board(self.w * self.cs, self.h * self.cs, self.cs)
        self.population = Population(self.w, int(self.h), int(self.cs * PROPORTION))
        self.buttons = self.CreateButtons()

    def Enlarge(self):
        global WIDTH, HEIGHT
        WIDTH += 1
        HEIGHT += 1
        self.Resize()

    def Reduce(self):
        global WIDTH, HEIGHT
        if WIDTH >= 96 or HEIGHT >= 46:
            WIDTH -= 1
            HEIGHT -= 1
            self.Resize()
        else:
            self.buttons[5].oneColor = True
            self.buttons[5].color = DEFAULT_FILL_COLORS['red']
            self.buttons[5].updateButton(self.buttons[5].fillColors['disabled'])

    # metoda odpowiedzialna za rozgrywke, a takze za jej pauze
    def play(self):
        while not self.handle():
            self.board.draw(self.buttons, self.population)

            if getattr(self, "started", None):
                self.population.nextGeneration()
            self.fps_clock.tick(FPS)

            # jesli nie ma zadnych zywych komorek, gra pauzuje sie
            count = len(list(self.population.aliveCells()))
            tick = pygame.time.get_ticks()
            if ceil(tick / 1000) % 2 == 0:
                if count == 0:
                    self.pause()

    def pause(self, reason="paused"):
        self.started = False
        pygame.display.set_caption("Game of life - " + str(reason))

    def resume(self):
        self.started = True
        pygame.display.set_caption("Game of life - started")

    # metoda odpowiedzialna za zajmowanie sie inputem uzytkownika
    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
                inboard = self.MousePressedInsideBoard()
                if inboard is not None and inboard[2]:
                    self.population.mouseHandler(inboard[0], inboard[1], inboard[3])
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.resume()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.pause()

    def MousePressedInsideBoard(self):
        mouseButton = pygame.mouse.get_pressed()
        if not any(mouseButton):
            return

        LPM = True if mouseButton[0] else False

        x, y = pygame.mouse.get_pos()
        if x >= WIDTH * CELL_SIZE * PROPORTION or y >= HEIGHT * CELL_SIZE * PROPORTION:
            return x, y, False, LPM
        return x, y, True, LPM


# populacja to wszystkie komorki, zywe lub nie, na planszy
class Population:
    def __init__(self, w, h, cs=10):
        self.bs = cs
        self.h = h
        self.w = w
        self.generation = self.resetGeneration()

    # tworzy nam nowa pusta generacje komorek
    def resetGeneration(self):
        generation = []
        for x in range(self.w):
            col = []
            for y in range(self.h):
                col.append(DEAD)
            generation.append(col)
        return generation

    # jesli uzytkownik kliknal na plansze LPM to tworzy nowa komorke, jesli PPM to usuwa istniejaca w tym miejscu komorke
    def mouseHandler(self, x, y, alive):
        x /= self.bs
        y /= self.bs
        self.generation[int(x)][int(y)] = ALIVE if alive else DEAD

    # wyswietlanie komorek na planszy
    def drawCells(self, board):
        for x, y in self.aliveCells():
            size = (self.bs, self.bs)
            position = (x * self.bs, y * self.bs)
            pygame.draw.rect(board, (0, 0, 0), pygame.Rect(position, size))

    # zwraca koordynaty na planszy, gdzie znajduja sie zywe komorki
    def aliveCells(self):
        for x in range(len(self.generation)):
            for y in range(len(self.generation[x])):
                if self.generation[x][y] == ALIVE:
                    yield x, y

    # sprawdzanie czy sasiednia komorka jest zapelniona, do tego sprawdzamy "zawijanie brzegow" czyli jesli nasza komorka jest na samej gorze ekranu,
    # to komorka w tej samej kolumnie na samym dole ekranu tez jest liczona jako komorka sasiadujaca
    def neighbors(self, x, y):
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx == x and ny == y:
                    continue
                if nx >= self.w:
                    nx = 0
                elif nx < 0:
                    nx = self.w - 1
                if ny >= self.h:
                    ny = 0
                elif ny < 0:
                    ny = self.h - 1
                yield self.generation[nx][ny]

    # uzywajac metody powyzej, sprawdzamy iel sasiadow ma nasza komorka i na tej podstawie decydujemy czy bedzie ona
    # w nastepnej generacji zyc, czy umrze
    def nextGeneration(self):
        nextGen = self.resetGeneration()
        for x in range(len(self.generation)):
            for y in range(len(self.generation[x])):
                count = sum(self.neighbors(x, y))
                if count == 3:
                    nextGen[x][y] = ALIVE
                elif count == 2:
                    nextGen[x][y] = self.generation[x][y]
                else:
                    nextGen[x][y] = DEAD
        self.generation = nextGen


if __name__ == "__main__":
    GAME = Game(WIDTH, HEIGHT, CELL_SIZE)
    GAME.play()
    
