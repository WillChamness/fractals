import pygame as pg

class App:
    def __init__(self, width, height, fast_mode=True):
        self.width = width
        self.height = height
        self.fast_mode = fast_mode
        self.res = (width, height)
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        pg.display.set_caption("mandelbrot")
        


    def run(self):
        stop = False
        while not stop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    stop = True
            
            self.fractal()
            pg.display.update()

    
    def draw(self, x, y, color):
        self.screen.set_at((x, y), color)
        if not self.fast_mode:
            pg.display.update()
        

    def fractal(self):
        def f(z, c):
            return z**2 + c

        ITERATIONS = 255

        for x in range(self.width):
            for y in range(self.height):
                z0 = complex(3.5*x/self.width - 2.5, 2*y/self.height - 1.5) # shift & stretch the graph to display the entire thing
                z = complex(0, 0)
                c = complex(x / self.width, y / self.height)
                counter = 0
                for _ in range(ITERATIONS):
                    z = f(z, c) + z0
                    if abs(z) > 2:
                        break
                    counter += 1
                color = (counter, counter, counter)
                self.draw(x, y, color)
    


def main():
    SCALAR = 120
    app = App(16*SCALAR, 9*SCALAR)
    app.run()

if __name__ == "__main__":
    main()
