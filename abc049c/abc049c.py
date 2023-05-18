import os

dirname = os.path.dirname(__file__)

in_file = dirname + "/input1.txt"
f = open(in_file, "r", encoding="UTF-8")

text = f.readlines()
s = text[0]
strings = ["dream", "dreamer", "erase", "eraser"]
t = ""
answer = "NO"
