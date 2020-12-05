from math import cos, pi, sin

from numpy import arange

from ball import Ball
from engine import Engine
from tentacle import Tentacle
from vector import Vector

WIDTH, HEIGHT = 500, 400
N = 2
SIZE = 3
LENGTH = 50

renderer = Engine(WIDTH, HEIGHT, title="Inverse Kinematics")
renderer.fps = 60

tentacles = []
ball: Ball


def setup() -> None:
    """
    setup function for ``Engine`` class
    """
    global tentacles, ball
    da = 2 * pi / N

    for a in arange(0, 2 * pi, step=da, dtype=float):
        x = WIDTH / 2 + HEIGHT / 2 * cos(a)
        y = HEIGHT / 2 * (1 + sin(a))
        tentacles.append(Tentacle(renderer, (WIDTH, HEIGHT), SIZE, seg_length=LENGTH, base=Vector(x, y)))

    ball = Ball(renderer, 100, 100, (WIDTH, HEIGHT))

    renderer.text_size = 15
    renderer.text_color = 255


def draw() -> None:
    """
    draw function for ``Engine`` class
    """
    global tentacles, ball
    renderer.background(51)

    ball.update()

    for tentacle in tentacles:
        tentacle.follow(ball.pos)
        tentacle.show()

    ball.show()

    renderer.text(10, 10, f"fps : {round(renderer.fps)}")


if __name__ == "__main__":
    renderer.run(draw, setup=setup)
