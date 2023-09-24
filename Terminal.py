#class Screen:
#    color=lambda up,down:'\033[48;2;{};{};{}m\033[38;2;{};{};{}m\u2584\033[0m'.format(up[0],up[1],up[2],down[0],down[1],down[2])
#    def __init__(self,width,height):
#        self.width=width
#        self.height=height
#        self.pixels=[[[0]*3]*width]*2*height
#    def display(self):
#        for h in range(self.height):
#            for w in range(self.width):
#                print(Screen.color(self.pixels[2*h][w],self.pixels[2*h+1][w]),end='')
#            print()
#    def rect(self,x,y,w,h,r,g,b):
#        for i in range(y,y+h):
#            for j in range(x,x+w):
#                self.pixels[i][j]=[r,g,b]

class Screen:
    color=lambda r,g,b:'\033[48;2;{};{};{}m \033[0m'.format(r,g,b)
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.pixels=[[[0]*3]*width]*height
    def display(self):
        for h in range(self.height):
            for w in range(self.width):
                print(Screen.color(*self.pixels[h][w]))
            print()
    def rect(self,x,y,w,h,r,g,b):
        for i in range(y,y+h):
            for j in range(x,x+w):
                self.pixels[i][j]=[r,g,b]
