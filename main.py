from math import cos, sin

from numpy import arange
from phoenyx import *

from ball import Ball
from tentacle import Tentacle

WIDTH, HEIGHT = 500, 400
N = 2
SIZE = 3
LENGTH = 50

renderer: Renderer = Renderer(WIDTH, HEIGHT, title="Inverse Kinematics")
renderer.fps = 60

tentacles: list[Tentacle] = []
ball: Ball = None


def reset_ball() -> None:
    ball.reset()


def setup() -> None:
    global tentacles, ball
    da = 2 * PI / N

    for a in arange(0, 2 * PI, step=da, dtype=float):
        x = WIDTH/2 + HEIGHT / 2 * cos(a)
        y = HEIGHT / 2 * (1 + sin(a))
        tentacles.append(
            Tentacle(renderer, (WIDTH, HEIGHT),
                     SIZE,
                     seg_length=LENGTH,
                     base=Vector(x, y)))

    ball = Ball(renderer, 100, 100, (WIDTH, HEIGHT))

    options = {
        "text_size": 9,
        "background": None,
    }
    renderer.create_menu("options", reset_ball=reset_ball, **options)

    renderer.text_size = 15
    renderer.text_color = 255


def draw() -> None:
    global tentacles, ball
    renderer.background(51)

    ball.update()

    for tentacle in tentacles:
        tentacle.follow(ball.pos)
        tentacle.show()

    ball.show()

    renderer.text(10, 10, f"fps : {round(renderer.fps)}")


if __name__ == "__main__":
    renderer.run()
