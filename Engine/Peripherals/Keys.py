from enum import Enum

alphas = [chr(c) for c in range(65, 91)]
control = ["ALT", "CTRL"]
arrows = ["LEFT", "RIGHT", "DOWN", "UP"]

Keys = Enum(alphas + control + arrows)
