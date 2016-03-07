import pygame
import time
import random 

bif = 'background_3.png'
mif = 'arrow-small-right.png'

WIDTH = 500
HEIGHT = 500


class model(object):
    """This is he model that stores the game state """
    def __init__ (self, ball, ball2, ball3, pacman, point):
        self.ball = ball
        self.ball2 = ball2
        self.ball3 = ball3
        self.pacman = pacman
        self.point = point

    def update(self):
        # self.ball = ball #sets the ball equal to the equation that defines it
        # self.pacman = pacman #Defines the pacman by its equation.
        self.ball.update(self.pacman) #Updates each character each round (?)
        #self.update(self.ball) #Updates each character each round (?)

        # self.point = point
        self.ball2.update(self.pacman)
        self.ball3.update(self.pacman)


class pacman(object):
    """ This is our pacman who dies from ghosts and eats balls!"""
    def __init__(self, x, y, radius):
        self.x = x #center coordinates/dimensions defining the pacman shape
        self.y = y
        self.radius = radius
        #Liv: Is pacman currently a ball? Should we make him into a sprite?


class ball (object):
    """this is the ball that pacman eats and scores points by eating!"""

    def __init__ (self, x, y, radius): #Another circle defining the
        self.x = x
        self.y = y
        self.radius = radius

    def update (self, pacman):

        if self.x == pacman.x and self.y == pacman.y:
            self.x = random.choice(range(0, WIDTH, 10))
            self.y = random.choice(range(0, HEIGHT, 10))

           #todo: when pacman eats me, disappear
           #More specifically, when the Pacman is the same

class ball2 (object):
    """this is the ball that pacman eats and scores points by eating!"""

    def __init__ (self, x, y, radius): #Another circle defining the
        self.x = x
        self.y = y
        self.radius = radius

    def update (self, pacman):

        if self.x == pacman.x and self.y == pacman.y:
            self.x = random.choice(range(0, WIDTH, 10))
            self.y = random.choice(range(0, HEIGHT, 10))

           #todo: when pacman eats me, disappear
           #More specifically, when the Pacman is the same

class ball3 (object):
    """this is the ball that pacman eats and scores points by eating!"""

    def __init__ (self, x, y, radius): #Another circle defining the
        self.x = x
        self.y = y
        self.radius = radius

    def update (self, pacman):

        if self.x == pacman.x and self.y == pacman.y:
            self.x = random.choice(range(0, WIDTH, 10))
            self.y = random.choice(range(0, HEIGHT, 10))

           #todo: when pacman eats me, disappear
           #More specifically, when the Pacman is the same

class point(object):
    """ this is what you earn when you collect the point rectangle :)"""
    def __init__ (self,number):
        self.number = number # Making an initial number.
    def add_point(self):
        self.number = self.number + 1 #Adding to this
        #(and making a function out of it so we can use it later independently of the class.)
        return self.number # do I need to return this
    def show(self):
        point_string = str(self.number)
        return point_string

class game_controller (object):
    def __init__(self,model):
        self.model = model #Creating a model. (What's that? Just an overarching structure?)
    def handle_event (self, event):
        """ This is the controlled where user input (arrow keys or openCV) changes the model"""
        # code in this section HEAVILY modified and extended from http://www.nerdparadise.com/tech/python/pygame/basics/part6/
        # also documentation here: http://www.pygame.org/docs/ref/key.html
        #while True:

        #for event in pygame.event.get():

        # determine if X was clicked, or Ctrl+W or Alt+F4 was used
        if event.type == pygame.QUIT:
            return
        #If the game quits, none of the below happen.
        if event.type == pygame.KEYDOWN:


        #If ___ key is pressed something is added or subtracted to one of the axis.
            if event.key == pygame.K_UP:
                if model.pacman.y == 0:
                    model.pacman.y = model.pacman.y
                else:
                    model.pacman.y = model.pacman.y - 10 #For example, going up is going in a positive direction in the y axis (by 1 for 1 press of the key.)


            if event.key == pygame.K_DOWN:
                if model.pacman.y == HEIGHT:
                    model.pacman.y = model.pacman.y
                else:
                    model.pacman.y = model.pacman.y + 10

            if event.key == pygame.K_LEFT:
                if model.pacman.x == 0:
                    model.pacman.x = model.pacman.x
                else:
                    model.pacman.x = model.pacman.x - 10

            if event.key == pygame.K_RIGHT:
                   if model.pacman.x == WIDTH:
                        model.pacman.x = model.pacman.x
                   else:
                        model.pacman.x = model.pacman.x + 10



class pygameview (object):
    """ Provides a view of the pacman model in a pygame window """
    def __init__(self, model, screen):
        """ Initialize with the specified model """
        self.model = model # The model is a model.
        self.screen = screen #The display is equal to the function that define's it's results

    def draw(self):
        """ Draw the game to the pygame window """
        # draw all the bricks to the screen
        self.screen.fill(pygame.Color('white'))
        background = pygame.Surface(screen.get_size()) #this is just making a surface because we have to do this uncool thing called blitting to make the text show
        background = background.convert() #increases speed
        background.fill((255, 255, 255)) #needs to match color

        #This sequence draws pacman onto the screen with the dimensions we gave earlier.

        pygame.draw.circle(self.screen,
                           (255, 255, 0),
                           (self.model.pacman.x, self.model.pacman.y),
                           self.model.pacman.radius)

        #This draws a dot (we want several, though, right?)

        pygame.draw.circle(self.screen,
                        (0, 0, 255),
                        (self.model.ball.x,
                        self.model.ball.y),
                        self.model.ball.radius)

        pygame.draw.circle(self.screen,
                        (0, 0, 255),
                        (self.model.ball2.x,
                        self.model.ball2.y),
                        self.model.ball2.radius)

        pygame.draw.circle(self.screen,
                        (0, 0, 255),
                        (self.model.ball3.x,
                        self.model.ball3.y),
                        self.model.ball3.radius)

        # Display some text #http://www.pygame.org/docs/tut/tom/games2.html
        font = pygame.font.Font(None, 36)
        text = font.render(point.show(points_earned), 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = WIDTH - 300
        background.blit(text, textpos)
        screen.blit(background, (0, 0))



        pygame.display.update()

if __name__ == '__main__':
    """ Provides a view of the pacman model in a pygame window """
    # This part starts the display and loads the background.
    pygame.init()
    pygame.key.set_repeat(50, 50) #https://sivasantosh.wordpress.com/2012/07/18/keyboard-event-handling-pygame/
    # pygame.display.init()

    screen = pygame.display.set_mode([WIDTH,HEIGHT]) #Starting the display using bif and mif
    # background = pygame.image.load(bif).convert()
    # mouse_c= pygame.image.load(mif).convert_alpha()
    first_ball = ball(50, 100,10)
    second_ball = ball2(300, 200, 15)
    third_ball =  ball3(50, 200, 20)
    actual_pacman = pacman(60, 70, 50)
    points_earned = point(0)
    #model = model(ball(50, 100,10), ball2(300, 200, 15), ball3(50, 200, 20), pacman(60, 70, 50), point(0))
    model = model(first_ball,second_ball,third_ball,actual_pacman,points_earned)
    view = pygameview(model, screen)
    controller = game_controller(model)

    # This part runs the code until it's closed. (QUIT is built in.)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                controller.handle_event(event)
        model.update()
        view.draw() 
        time.sleep(.001) #todo: initialize all locations of pacman, ball AND make something appropriate happen when pacman eats a ball

    # def __init__(self, model, size):
    #     """ Initialize with the specified model """
    #     self.model = model
    #     self.screen = pygame.display.set_mode(size)



