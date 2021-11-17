from phoenyx import *


def _constrain(value: float, low: float = None, hight: float = None) -> float:
    low = (low, value)[low is None]
    hight = (hight, value)[hight is None]
    value = (low, value)[low <= value]
    value = (hight, value)[hight >= value]
    return value


class Ball:
    """
    Ball
    ====
    based on the ``Renderer`` renderer in python and ``Vector`` class

    Ball has:
     * a ``position``
     * a ``GRAVITY`` force
     * a bounce method on the lower edge of the screen
    """
    GRAVITY = Vector(0, .07)
    RADIUS = 7
    VELOCITY = 4

    def __init__(self, renderer: Renderer, x: float, y: float,
                 win: tuple) -> None:
        """
        new Ball instance

        Parameters
        ----------
            renderer : Renderer
                main Renderer
            x : float
                ball position along the x-axis
            y : float
                ball position along the y-axis
            win : tuple
                size of the windows
        """
        self.pos = Vector(x, y)
        self.opos = self.pos.copy()
        self.win = win

        self.vel = Vector.random2d(mag=self.VELOCITY)
        self.vel.heading = _constrain(self.vel.heading, -PI / 8, PI / 8)

        self._renderer = renderer

    def reset(self) -> None:
        """
        resets the Ball to its original position
        """
        self.pos = self.opos.copy()
        self.vel = Vector.random2d(mag=self.VELOCITY)
        self.vel.heading = _constrain(self.vel.heading, -PI / 8, PI / 8)

    def show(self) -> None:
        """
        calls draw methods from Renderer
        """
        self._renderer.fill = 100, 255, 0
        self._renderer.no_stroke()
        self._renderer.circle(self.pos, self.RADIUS)

    def update(self) -> None:
        """
        updates the position of the Ball:
        1) apply forces (adds GRAVITY to current velocity)
        2) updates position
        3) makes the Ball bounce on left, right and bottom edge
        """
        self.vel += self.GRAVITY
        self.pos += self.vel

        if self.pos.x < self.RADIUS:
            self.pos.x = self.RADIUS
            self.vel.x *= -1

        if self.pos.x > self.win[0] - self.RADIUS:
            self.pos.x = self.win[0] - self.RADIUS
            self.vel.x *= -1

        if self.pos.y > self.win[1] - self.RADIUS:
            self.vel.y *= -1
            self.pos.y = self.win[1] - self.RADIUS
