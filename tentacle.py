from phoenyx import *

from segment import Segment


def _map(x: float, x0: float, x1: float, y0: float, y1: float) -> float:
    """
    linear interpolation
    """
    return (y0 * (x1-x) + y1 * (x-x0)) / (x1-x0)


class Tentacle:
    """
    Tentacle
    ========
    based on the ``Renderer`` renderer in python and ``Vector`` class\\
    uses ``Segment``

    Tencacle has:
     * a ``size`` for the number of Segments
     * the length of all its segments ``seg_length``
     * a ``base``
    """
    def __init__(self,
                 renderer: Renderer,
                 win: tuple,
                 size: int,
                 seg_length: float = None,
                 base: Vector = None) -> None:
        """
        new Tentacle instance

        Parameters
        ----------
            renderer : Renderer
                main Renderer
            win : tuple
                size of windows
            size : int
                number of Segments
            seg_length : (float, optional)
                length of all Segments
                Defaults to None
            base : (Vector, optional)
                a fixed base or a free Tentacle
                Defaults to None
        """
        self.base = base
        self.has_base = True
        if base is None:
            self.base = Vector()
            self.has_base = False

        self.size = size
        self.seg_length = (seg_length, 100)[seg_length is None]

        self._renderer = renderer

        setupX = (self.base.x, win[0])[base is None]
        setupY = (self.base.y, win[1])[base is None]
        self.array = [
            Segment(self._renderer, setupX, setupY, self.seg_length, 0,
                    _map(i, 0, self.size - 1, 1, 5)) for i in range(self.size)
        ]

    def show(self) -> None:
        """
        calls draw method from Segment
        """
        for segment in self.array:
            segment.show()

    def follow(self, target: Vector) -> None:
        """
        makes Tentacle follow target:
        1) last Segment follows target
        2) calls follow method for each other Segment on the point a of the Segment before
        3) sets the base if any
        """
        self.array[-1].follow(target)

        for i in range(self.size - 1)[::-1]:
            self.array[i].follow(self.array[i + 1].a)

        if self.has_base:
            self.array[0].set_a(self.base)
            for i in range(1, self.size):
                self.array[i].set_a(self.array[i - 1].b)
