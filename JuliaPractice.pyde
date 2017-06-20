from __future__ import division

'''Julia Set Exploration
June 19, 2017
It finally works
Color is not like Shiffman's, though'''

xmin = -2
xmax = 2
rangex = xmax - xmin
rangey = rangex

#scale factors for graphing:
xscl = 600.0/rangex
yscl = -600.0/rangey

#choose a z, examples on Wikipedia
z = [-0.4, 0.6]
zList = []

def setup():
    size(600,600)
    colorMode(HSB)
    
def draw():
    background(0) #black
    #origin in center:
    translate(width/2,height/2) 
    #draw the x-y axes if you want
    grid()
    #starting c
    c = [-0.4,0.6]
    #x goes from xmin to xmax by tiny steps
    #but not by xscl for some reason
    for x in arange(xmin,xmax,0.01):
        #y, too
        for y in arange(xmin,xmax,0.01):
            #declare z
            z = [x,y]
            #put it into the julia program
            col = julia(z,c,100)
            #if julia returns 0
            if col == 0:
                stroke(0) #black fill and stroke
                fill(0)
            else:
                #map the color from 0 to 100
                #to 0 to 255
                col1 = map(col,0,100,0,255)
                #color for stroke and fill
                stroke(col1,360,360)
                fill(col1,360,360)
            #draw a tiny rectangle
            rect(x*xscl,y*yscl,1,1)

def zSquaredPlusC(z,c):
    '''does the transformation
    zn+1 = z**2 + c'''
    return addComp(cMult(z,z),c)  

def julia(z,c, num):
    '''runs the julia set num times
    and returns the diverge count'''
    count = 0
    #define z2 as z
    z2 = z
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(z2) > 4.0:
            #return the step it diverged on
            return count
        #iterate z
        z2 = zSquaredPlusC(z2,c)
        count += 1
    #if z hasn't diverged by the end
    return 0            
            
def grid():
    '''draws the x- and y-axes'''
    stroke(255)
    line(-300,0,300,0)
    line(0,-300,0,300)            
    
def addComp(a,b):
    '''adds two complex numbers together'''
    return [a[0]+b[0],a[1]+b[1]]   

def cMult(a,b):
    '''multiplies two complex numbers'''
    return [a[0]*b[0]-a[1]*b[1],a[1]*b[0]+a[0]*b[1]]

def graphComp(z):
    '''graphs a complex number
    z = x + iy'''
    fill(0) #black point
    ellipse(z[0]*xscl,z[1]*yscl,5,5)
    
def arange(start,stop,step):
    output = []
    n = start
    while n < stop:
        output.append(n)
        n += step
    return output

def magnitude(z):
    #returns the square of the 
    #distance from the origin
    return z[0]*z[0] + z[1]*z[1]