import os

#: Name of the person to say hello to
HELLO_NAME = os.environ.get("INPUT_HELLONAME", "")

#: Number of times to repeat the message
REPEATS = int(os.environ.get("INPUT_REPEATS", "1"))
