
"""
    
    Get shapes from the WoodGit ufo, then combine them in funny overlaying combinations.

"""
from AppKit import NSImage, NSGraphicsContext, NSRectFill, NSColor, NSGradient
from fontTools.pens.cocoaPen import CocoaPen
from robofab.world import OpenFont

import os


def drawMultiply():
    image = NSImage.alloc().initWithSize_(size)
    image.lockFocus()
    NSColor.whiteColor().set()
    NSRectFill(NSRect((0,0), size))
    gc = NSGraphicsContext.currentContext()
    gp = gc.graphicsPort()
    CGContextSetBlendMode(gp, kCGBlendModeMultiply)
    #gc.setCompositingOperation_(NSCompositePlusDarker)
    gradient = NSGradient.alloc().initWithColors_([verticalColor, NSColor.clearColor()])
    gradient.drawFromPoint_toPoint_options_((0,0), (0,size[1]), 0)
    gradient = NSGradient.alloc().initWithColors_([horizontalColor, NSColor.clearColor()])
    gradient.drawFromPoint_toPoint_options_((0,0), (size[0],0), 0)
    image.unlockFocus()


ufoPath = u"wood/TypeMedia1314-WoodType.ufo"
ufoPath = os.path.join(os.path.dirname(os.getcwd()), ufoPath)
print os.path.exists(ufoPath)

f = OpenFont(ufoPath)
print f
