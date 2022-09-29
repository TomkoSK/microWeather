pin0 = None
def set_tempo(self, ticks=4, bpm=120):
    "Sets the approximate tempo for playback."
def get_tempo(self):
    "Gets the current tempo as a tuple of integers: (ticks, bpm)."
    return (4, 120)
def play(self, music, pin=pin0, wait=True, loop=False):
    "If wait is set to True, this function is blocking. If loop is set to True, the tune repeats until stop is called (see below) or the blocking call is interrupted."
def pitch(self, frequency, duration=-1, pin=pin0, wait=True):
    pass
def stop(self, pin=pin0):
    "Stops all music playback on a given pin, eg. music.stop(pin1). If no pin is given, eg. music.stop() pin0 is assumed."
def reset():
    pass

DADADADUM = None
ENTERTAINER = None
PRELUDE = None
ODE = None
NYAN = None
RINGTONE = None
FUNK = None
BLUES = None
BIRTHDAY = None
WEDDING = None
FUNERAL = None
PUNCHLINE = None
PYTHON = None
BADDY = None
CHASE = None
BA_DING = None
WAWAWAWAA = None
JUMP_UP = None
JUMP_DOWN = None
POWER_UP = None
POWER_DOWN = None