import ezdxf
import numpy as np


class Circle:
    def __init__(self, entity):
        self.entity = entity

    def __repr__(self):
        return (f"{self.__class__.__name__}(\n"
                f"Layer: {self.entity.dxf.layer},\n"
                f"Line type: {self.entity.dxf.linetype},\n"
                f"Line type scale: {self.entity.dxf.ltscale},\n"
                f"Line weight: {self.entity.dxf.lineweight},\n"
                f"Color: {self.entity.dxf.color},\n"
                f"Center: {self.entity.dxf.center},\n"
                f"Radius: {self.entity.dxf.radius},\n"
                f"Diameter: {self.entity.dxf.radius * 2},\n"
                f"Perimeter: {self.entity.dxf.radius * 2 * np.pi},\n"
                f"Area: {self.entity.dxf.radius ** 2 * np.pi}\n"
                f")")


def parse(path):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    circles = []
    for e in msp:
        if e.dxftype() == "CIRCLE":
            circles.append(Circle(e))
    return circles
