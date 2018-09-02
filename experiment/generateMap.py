import cv2
import numpy as np
import math

def longestVerticalLine(key,arr):
    ls = []
    for line in arr:
        ls.append(line[1])
        ls.append(line[3])
    ls = sorted(ls)
    return key,ls[0],key,ls[len(ls)-1]
def longestHoriLine(key,arr):
    ls = []
    for line in arr:
        ls.append(line[0])
        ls.append(line[2])
    ls = sorted(ls)
    return ls[0],key,ls[len(ls)-1],key


img = cv2.imread('loll.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,200,apertureSize = 3)
lines = cv2.HoughLinesP(
    edges,
    rho=6,
    theta=np.pi / 180,
    threshold=120,
    lines=np.array([]),
    minLineLength=50,
    maxLineGap=40
)
hori_line = []
vertical_line = []
for line in lines:
    for x1,y1,x2,y2 in line:
        if x1 != x2:
            slope = (y2 - y1) / (x2 - x1) # <-- Calculating the slope.
            if abs(slope) < 0.5:
               hori_line.append([x1, y1, x2, y2])
            else:
                vertical_line.append([x1, y1, x2, y2])


hori_line = sorted(hori_line,key=lambda x: x[1])
usy = hori_line[0][1]
udict = {}
udict[usy] = [hori_line[0]]
for line in hori_line:
     if abs(usy - line[1]) < 100:
         arr = udict[usy]
         arr.append(line)
         udict[usy] = arr
     else:
        usy =  line[1]
        udict[usy] = [line]

vertical_line = sorted(vertical_line,key=lambda x: x[0])
usy1 = vertical_line[0][0]
udict1 = {}
udict1[usy1] = [vertical_line[0]]
for line in vertical_line:
    if abs(usy1 - line[0]) < 100:
            arr = udict1[usy1]
            arr.append(line)
            udict1[usy1] = arr
    else:
        usy1 =  line[0]
        udict1[usy1] = [line]

for key in udict1.keys():
    x1,y1,x2,y2 = longestVerticalLine(key,udict1[key])
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

for key in udict.keys():
    x1,y1,x2,y2 =  longestHoriLine(key,udict[key])
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('done',img)
cv2.waitKey()