from math import cos, sin

from engine import Engine
from vector import Vector


class Segment:
    """
    Segment
    =======
    based on the ``Engine`` renderer in python and ``Vector`` class

    Segment has:
     * point ``a`` used as a reference
     * a ``length``
     * an ``angle``
     * a ``weight`` used as thickness to draw
     * point ``b`` calculated from data above
    """
    def __init__(self,
                 renderer: Engine,
                 x: float,
                 y: float,
                 length: float,
                 angle: float,
                 weight: float = None) -> None:
        """
        new Segment instance

        Parameters
        ----------
            renderer : Engine
                main Engine
            x : float
                position along the x-axis
            y : float
                position along the y-axis
            length : float
                length of the Segment
            angle : float
                angle between Segment and the x-axis
            weight : (float, optional)
                weight of the Segment, used as thickness to draw
                Defaults to None
        """
        self.a = Vector(x, y)
        self.b = Vector()
        self.length = length
        self.angle = angle
        self.weight = (weight, 4)[weight is None]

        self._renderer = renderer

    def set_a(self, a: Vector) -> None:
        """
        sets a new a point for the current Segment\\
        then updates point b
        """
        self.a = a
        self.update_b()

    def update_b(self) -> None:
        """
        updates point B for current Segment
        """
        dx = cos(self.angle) * self.length
        dy = sin(self.angle) * self.length
        self.b.setCoord(x=self.a.x + dx, y=self.a.y + dy)

    def show(self) -> None:
        """
        calls draw methods from Engine
        """
        self._renderer.stroke = 255
        self._renderer.no_fill()
        self._renderer.stroke_weight = round(self.weight)
        self._renderer.line(self.a.rounded(), self.b.rounded())

    def follow(self, target: Vector) -> None:
        """
        makes Segment follow a target Vector :
        1) make Segment point towards designated target
        2) sets point a so that b is on target
        3) updates point b
        """
        d = target - self.a
        self.angle = d.heading
        d.magnitude = self.length
        d *= -1
        self.a = target + d
        self.update_b()
