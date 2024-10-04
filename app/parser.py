import ezdxf
import numpy as np


class Circle:
    def __init__(self, entity):
        self.entity = entity

    def get_json(self):
        return {
            "Layer": self.entity.dxf.layer,
            "Line type": self.entity.dxf.linetype,
            "Line type scale": self.entity.dxf.ltscale,
            "Line weight": self.entity.dxf.lineweight,
            "Color": self.entity.dxf.color,
            "Center": (self.entity.dxf.center[0], self.entity.dxf.center[1]),
            "Radius": self.entity.dxf.radius,
            "Diameter": self.entity.dxf.radius * 2,
            "Perimeter": self.entity.dxf.radius * 2 * np.pi,
            "Area": self.entity.dxf.radius ** 2 * np.pi,
        }

    def __repr__(self):
        return f"{self.__class__.__name__}(\n" + ",\n".join(f"{k}: {v}" for k, v in self.get_json().items()) + "\n)"


def parse(path: str):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    return [Circle(e) for e in msp if e.dxftype() == "CIRCLE"]
