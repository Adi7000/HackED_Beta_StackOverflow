import math
def greedy(points):
    path = [points[0]]
    lastP = points.pop(0)
    while len(points) != 0:    
        lst = []
        for i in range(len(points)):
            lst.append(dist(lastP, points[i]))
        minid = lst.index(min(lst))
        path.append(points[minid])
        lastP = points.pop(minid)
    return path


    
class section():
    def __init__(self, points, quadrant):
        self.numofp = len(points)
        self.quadnum = quadrant #tuple (x,y)
        self.points = points
        
    def greedy(self):
        if len(self.points)>0:
            
            path = [self.points[0]]
            lastP = self.points.pop(0)
            while len(self.points) != 0:    
                lst = []
                for i in range(len(self.points)):
                    lst.append(dist(lastP, self.points[i]))
                minid = lst.index(min(lst))
                path.append(self.points[minid])
                lastP = self.points.pop(minid)
            return path
        else:
            return []
        
def sectional(points, sep=100):
    startpoint = points[0]
    size = [max(i[0] for i in points), max(i[1] for i in points)]
    quadrants = [math.ceil(size[0]/sep)-1, math.ceil(size[1]/sep)-1]
    
    # create sections/quads
    quads = {}
    for i in range(quadrants[0] + 1):
        if i == 0:
            for j in range(quadrants[1] + 1):
                if j == 0:
                    secpoints = [k for k in points if k[0]<=(i+1)*sep and k[1]<=(j+1)*sep and k[0]>=i*sep and k[1]>=j*sep] # determine what points belong in the section
                    quads[(i,j)] = section(secpoints,(i,j))
                    if startpoint in secpoints:
                        startquad = (i,j)
                else:
                    secpoints = [k for k in points if k[0]<=(i+1)*sep and k[1]<=(j+1)*sep and k[0]>=i*sep and k[1]>j*sep] # determine what points belong in the section
                    quads[(i,j)] = section(secpoints,(i,j))
                    if startpoint in secpoints:
                        startquad = (i,j)                    
                    
        else:
            for j in range(quadrants[1] + 1):
                if j == 0:
                    secpoints = [k for k in points if k[0]<=(i+1)*sep and k[1]<=(j+1)*sep and k[0]>i*sep and k[1]>=j*sep] # determine what points belong in the section
                    quads[(i,j)] = section(secpoints,(i,j))
                    if startpoint in secpoints:
                        startquad = (i,j)
                else:
                    secpoints = [k for k in points if k[0]<=(i+1)*sep and k[1]<=(j+1)*sep and k[0]>i*sep and k[1]>j*sep] # determine what points belong in the section
                    quads[(i,j)] = section(secpoints,(i,j))
                    if startpoint in secpoints:
                        startquad = (i,j)                
                
    # determine path by quad   
    path = quads[startquad].greedy()
    i, j = startquad
    # go down 
    while j > 0:
        j -= 1
        path += quads[(i,j)].greedy()
        
    # go left
    while i > 0:
        i -= 1
        path += quads[(i,j)].greedy()

    # oscilate up and down while moving right (repeats wont affect as their points are emptied after use)
    a = 1

    while i < startquad[0]:
        if a == 1: # go up
            while j < quadrants[1]:
                path += quads[(i,j)].greedy()
                j += 1
                path += quads[(i,j)].greedy()
                
            a = -1
        elif a == -1: # go down
            while j > 0:
                path += quads[(i,j)].greedy()
                j -= 1
                path += quads[(i,j)].greedy() 
                
            a = 1
                
        i += 1
            
    b = 1
    if a == -1: # if it last went up then oscilate right to left while going down
        while j >= 0:
            if b == 1:   # go right
                while i < quadrants[0]:
                    path += quads[(i,j)].greedy()
                    i += 1
                    path += quads[(i,j)].greedy()
                b = -1
            elif b == -1: # go left
                while i > startquad[0]:
                    path += quads[(i,j)].greedy()
                    i -= 1
                    path += quads[(i,j)].greedy()
                b = 1
            j -= 1
            
    elif a == 1: # if it last went down then oscilate right to left while going up
        while j <= quadrants[1]:
            if b == 1:   # go right
                while i < quadrants[0]:
                    path += quads[(i,j)].greedy()
                    i += 1
                    path += quads[(i,j)].greedy()
                b = -1
            elif b == -1: # go left
                while i > startquad[0]:
                    path += quads[(i,j)].greedy()
                    i -= 1
                    path += quads[(i,j)].greedy()
                b = 1
            j += 1
    return path

def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1]- p1[1])**2)**(1/2)
    

# if __name__ == "__main__":
#     #points = [(0,0),(0,1),(0,2),(1,5),(2,1),(2,3),(5,5),(6,7),(8,8),(7,8),(6,7),(9,9),(8,7),(7,6),(5,6),(7,5)]
#     points = []
#     for i in range(10):
#         for j in range(10):
#             points.append((i,j))
#
#     path = sectional(points)
#     print(path)
#     print(len(path))
#     print(len(points))





