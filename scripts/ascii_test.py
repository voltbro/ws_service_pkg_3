#!/usr/bin/env python3

from asciimatics.effects import Print, Clock, Matrix
from asciimatics.renderers import BarChart, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys
import math
import time
from random import randint


def fn():
    return randint(0, 40)
def fn2():
    return 15

def wv(x):
    return lambda: 1 + math.sin(math.pi * (2*time.time()+x) / 5)


def demo(screen):
    scenes = []
    if screen.width != 132 or screen.height != 24:
        pass
    #     effects = [
    #         Print(screen, FigletText("Resize to 132x24"),
    #               y=screen.height//2-3),
    #     ]
    if True:
        effects = [
            Print(screen,

                  BarChart(20, 40, [fn, fn, fn2],
                           char="d",
                           gradient=[(20, Screen.COLOUR_GREEN),
                                     (30, Screen.COLOUR_YELLOW),
                                     (40, Screen.COLOUR_RED)]),
                  x=1, y=1, transparent=False, speed=2, delete_count=50,),
            Matrix(screen, delete_count=50)
            # Clock(screen, x=10, y=10, r=10)
            # Print(screen,
            #       BarChart(
            #           13, 60,
            #           [wv(1), wv(2), wv(3), wv(4), wv(5), wv(7), wv(8), wv(9)],
            #           colour=Screen.COLOUR_GREEN,
            #           axes=BarChart.BOTH,
            #           scale=2.0),
            #       x=68, y=1, transparent=False, speed=2),
            # Print(screen,
            #       BarChart(
            #           7, 60, [lambda: time.time() * 10 % 101],
            #           gradient=[
            #               (33, Screen.COLOUR_RED, Screen.COLOUR_RED),
            #               (66, Screen.COLOUR_YELLOW, Screen.COLOUR_YELLOW),
            #               (100, Screen.COLOUR_WHITE, Screen.COLOUR_WHITE),
            #           ] if screen.colours < 256 else [
            #               (10, 234, 234), (20, 236, 236), (30, 238, 238),
            #               (40, 240, 240), (50, 242, 242), (60, 244, 244),
            #               (70, 246, 246), (80, 248, 248), (90, 250, 250),
            #               (100, 252, 252)
            #           ],
            #           char=">",
            #           scale=100.0,
            #           labels=True,
            #           axes=BarChart.X_AXIS),
            #       x=68, y=16, transparent=False, speed=2),
            # Print(screen,
            #       BarChart(
            #           10, 60,
            #           [wv(1), wv(2), wv(3), wv(4), wv(5), wv(7), wv(8), wv(9)],
            #           colour=[c for c in range(1, 8)],
            #           bg=[c for c in range(1, 8)],
            #           scale=2.0,
            #           axes=BarChart.X_AXIS,
            #           intervals=0.5,
            #           labels=True,
            #           border=False),
            #       x=3, y=13, transparent=False, speed=2)
        ]
    # if time.time() - start < delta:

    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)


delta = 20
start_time = time.time()
# while time.time() - start_time < delta:
#     try:
#         Screen.wrapper(demo, start_time, delta)
#         sys.exit(0)
#     except ResizeScreenError:
#         pass
Screen.wrapper(demo)
sys.exit(0)

# from random import randint
# from asciimatics.screen import Screen
#
# def demo(screen):
#     while True:
#         screen.print_at('Hello world!',
#                         randint(0, screen.width), randint(0, screen.height),
#                         colour=randint(0, screen.colours - 1),
#                         bg=randint(0, screen.colours - 1))
#         ev = screen.get_key()
#         if ev in (ord('Q'), ord('q')):
#             return
#         screen.refresh()
#
# Screen.wrapper(demo)


# from asciimatics.effects import Cycle, Stars
# from asciimatics.renderers import FigletText
# from asciimatics.scene import Scene
# from asciimatics.screen import Screen
#
# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("ASCIIMATICS", font='big'),
#             int(screen.height / 2 - 8)),
#         Cycle(
#             screen,
#             FigletText("ROCKS!", font='big'),
#             int(screen.height / 2 + 3)),
#         Stars(screen, 200)
#     ]
#     screen.play([Scene(effects, 500)])
#
# Screen.wrapper(demo)

