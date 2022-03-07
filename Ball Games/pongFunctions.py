import math

def circlecoord(x, y, xvel, yvel, r, width, height):

    if x + r >= width: # if circle hits right border change x vel
        x = width - r
        xvel *= -1

    elif x - r <= 0: # if circle hits left border change x vel
        x = r
        xvel *= -1
        
    if y + r >= height: # if hits top border change y vel
        y = height - r
        yvel *= -1

    elif y - r <= 0: # if hits bottom border change y vel
        y = r
        yvel *= -1

    return(x,y,xvel,yvel)


def checkcontactbounce(x, y, xvel, yvel, r, iter):

    xcurrent = x[iter]
    ycurrent = y[iter]
    d = [None]*len(x)

    for i in range(0,len(x)):
        d = math.sqrt((x[iter] - x[i])**2 + (y[iter] - y[i])**2) # calculates distance between balls
        if d < (r[i]+r[iter]):

            if (xvel[iter] > 0 and xvel[i] < 0) or (xvel[iter] < 0 and xvel[i] > 0):
                xvel[iter] *= -1
                xvel[i] *= -1

            if (yvel[iter] > 0 and yvel[i] < 0) or (yvel[iter] < 0 and yvel[i] > 0):
                yvel[iter] *= -1
                yvel[i] *= -1

    return xvel, yvel

