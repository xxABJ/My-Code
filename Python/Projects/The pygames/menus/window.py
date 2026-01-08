import pygame

class window:
    
    pygame.init()

    def __init__(self, w=400, h=400):
        self.w = w; self.h = h
        self.root = pygame.display.set_mode((w,h))

        #self.selectedbool = False
        self.selected = "main"


class draw(window):

    def __init__(self):
        super().__init__()
         #self.mm = mainMenu(self)
         #self.pm = pauseMenu(self)
        #self.state()


    def state(self):
        if self.selected == 'main':
            self.mm.run()
            pygame.draw.rect(self.root, "blue", rect=(10,10,10,10))
            pygame.display.update()
        if self.selected == 'pause':
            self.pm.run()
            pygame.draw.rect(self.root, "green", rect=(10,10,100,100))
            pygame.display.update()


class ui(draw):

    def __init__(self):
        super().__init__()
        self.mm = mainMenu(self)
        self.pm = pauseMenu(self)
        self.windowUI()

    def windowUI(self):
        while True:
            self.root.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("esc")
                        match self.selected:
                            case 'main':
                                self.selected = 'pause'
                                self.state()
                            case 'pause':
                                self.selected = 'main'
                                self.state()


                        #if self.selectedbool:
                        #    self.selected = "pause"
                        #    self.selectedbool = True
                        #    self.state()
                        #else:
                        #    self.selected = "main"
                        #    self.selectedbool = False
                        #    self.state()

            

class mainMenu():

    def __init__(self, window):
        self.window = window
        #super().__init__()
        #self.run()

    def run(self):
        self.window.root.fill("lightgreen")

class pauseMenu():

    def __init__(self, window):
        self.window = window
        #super().__init__()
        #self.run()

    def run(self):
        self.window.root.fill("lightblue")


if __name__ == "__main__":
    w = ui()