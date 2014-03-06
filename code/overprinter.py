
"""
    
    Get shapes from the WoodGit ufo, then combine them in funny overlaying combinations.

"""
from AppKit import NSImage, NSGraphicsContext, NSRectFill, NSColor, NSGradient
from Quartz import *

from fontTools.pens.cocoaPen import CocoaPen
from robofab.world import OpenFont

import os


#def drawMultiply():
#    image = NSImage.alloc().initWithSize_(size)
#    image.lockFocus()
#    NSColor.whiteColor().set()
#    NSRectFill(NSRect((0,0), size))
#    gc = NSGraphicsContext.currentContext()
#    gp = gc.graphicsPort()
#    CGContextSetBlendMode(gp, kCGBlendModeMultiply)
#    #gc.setCompositingOperation_(NSCompositePlusDarker)
#    gradient = NSGradient.alloc().initWithColors_([verticalColor, NSColor.clearColor()])
#    gradient.drawFromPoint_toPoint_options_((0,0), (0,size[1]), 0)
#    gradient = NSGradient.alloc().initWithColors_([horizontalColor, NSColor.clearColor()])
#    gradient.drawFromPoint_toPoint_options_((0,0), (size[0],0), 0)
#    image.unlockFocus()

def drawLetter(f, glyphName, fontSize):
    fontScale = float(fontSize) / f.info.unitsPerEm
    save()
    scale(fontScale)
    c = CocoaPen(f)
    f[glyphName].draw(c)
    drawPath(c.path)
    restore()

def drawOverprintLetter(items, fontSize, unitsPerEm):
    """ Let's put all the drawable items in a dict so that we can stack more than 2 if we want to. 
    
    This needs the new Drawbot to work. :)
    """
    maxGlyphWidth = None
    glyphHeight = fontSize
    for item in items:
        w = item['font'][item['glyphName']].width
        if maxGlyphWidth is None:
            maxGlyphWidth = w
        maxGlyphWidth = max(maxGlyphWidth, w)
    imageSize = (maxGlyphWidth*fontSize, unitsPerEm)
    overprintImage = NSImage.alloc().initWithSize_(imageSize)
    overprintImage.lockFocus()
    fontScale = float(fontSize) / unitsPerEm
    aT = NSAffineTransform.transform()
    aT.scaleBy_(fontScale)
    aT.concat()

    #gc = NSGraphicsContext.currentContext()
    #gp = gc.graphicsPort()
    #CGContextSetBlendMode(gp, kCGBlendModeMultiply)
    for item in items:
        save()
        f = item['font']
        color = item['color']
        #fill(color[0], color[1], color[2], color[3])
        nsc = NSColor.colorWithDeviceRed_green_blue_alpha_(color[0],color[1],color[2],color[3])
        nsc.set()
        c = CocoaPen(f)
        f[item["glyphName"]].draw(c)
        c.path.fill()
        #drawPath(c.path)
        restore()
    overprintImage.unlockFocus()
    # get drawbot to draw the image.
    image(overprintImage, (0,0))
    



ufoPath = u"wood/TypeMedia1314-WoodType.ufo"
ufoPath = os.path.join(os.path.dirname(os.getcwd()), ufoPath)
print os.path.exists(ufoPath)

f = OpenFont(ufoPath)
#names = f.keys()
names = [ "D", "F", "H", "N", "S", "Z", "five", "eight", "Gcounter", "one_unit", "Acounter", "Ocounter", "ecounter", "half_unit", "Xcounter", "Ccounter"]

names = [ "D", "F"]
print names
print f

cm = 28.3464567    # points in 1 centimeter

#a6width = 14.8*cm
#a6height = 10.5*cm
#size(a6width, a6height)
size(3000,1000)
fontSize = 100

translate(50,1000-2*fontSize)

gridWidth = 1414 * fontSize / f.info.unitsPerEm
for firstName in names:
    save()
    for secondName in names:
        items = [
            dict(font=f, color=(0,0,random(),0.5), glyphName=choice(names)),
        ]
        drawOverprintLetter(items, fontSize, f.info.unitsPerEm)
        translate(gridWidth+10,0)
    restore()
    translate(0,-fontSize*1.4)
    
