import tkinter
import time

DERECTIONS = {'Up': (0,-1),'Down' : (0,1),'Right' : (1,0),'Left' : (-1,0)}
IN_GAME = True

class Snake():
    def __init__(self,canvas) -> None:
        self.canvas = canvas
        self.segments = []
        self.direction = 'Down'
        for i in  range(2):
            self.add_segment(100*(2-i), 100)
        
        
    def add_segment(self,x,y):
        s = self.canvas.create_rectangle(x,y,x+20,y+20,fill = 'black')
        self.segments.append(s)

    def move(self):
        x1,y1,x2,y2 = self.canvas.coords(self.segments[0])
        dx,dy = DERECTIONS[self.direction]
        new_x = x1 + dx * 20
        new_y = y1 + dy * 20
        new_segment = self.canvas.create_rectangle(new_x,new_y,new_x + 20,new_y + 20,fill = 'black')
        self.segments = [new_segment] + self.segments[0:-1]
        self.canvas.delete(self.segments[-1])

    def growth(self):
         x1,y1,x2,y2 = self.canvas.coords(self.segments[-1])
         self.add_segments(x1,y1)

    def change_direction(self,new_dir):
        opposites = {'Up':'Down','Down':'Up','Right':'Left','Left':'Right'}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir
    def check_collision(self):
        x1,y1,x2,y2 = self.canvas.coords(self.segments[0])
        if x1 < 0 or y1 < 0 or x2 > 500 or y2 > 400:
            return True
        for segments in self.segments[1:]:
            if self.canvas.coords(segments) == [x1,y1,x2,y2 ]:
                return True
            
        return False
    
def game_loop():
    global IN_GAME
    if IN_GAME == True:
        snake.move()
        if snake.check_collision():
            IN_GAME = False
            canvas.create_text(250,200,text = 'Иди отсюда немощ', fill = 'red', font = ('Areal', 25))
        window.after(100,game_loop)

def change_direction(event):
    snake.change_direction(event.keysym)        









window = tkinter.Tk()
window.title("Snake")
canvas = tkinter.Canvas(window,width = 500,height = 400)
canvas.pack()

snake = Snake(canvas)









window.bind('<KeyPress>',change_direction)
game_loop()
window.mainloop()