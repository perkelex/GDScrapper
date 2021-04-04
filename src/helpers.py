import itertools
import threading
import time
import sys


FORBIDDEN_FLAIRS = ["Console", "US Only", "Expired"]
DONE_FLAG = False


def contains_forbidden_flairs(submission):
        """
        Checks submission flair for values that would make the submission uninteresting.
        """

        for flair in FORBIDDEN_FLAIRS:
            if flair in submission.link_flair_text:
                return True
        return False

def animate(text):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if DONE_FLAG:
            sys.stdout.write(f'\r{text}  ')  # clear loading-simulaing symbol
            sys.stdout.flush()
            break
        sys.stdout.write(f'\r{text} {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\nDone!\n')
    sys.stdout.flush()

def print_animated_text(text):
    """
    Prints a text followed by a loading animation. MUST be used in pair with done()
    """
    global DONE_FLAG
    DONE_FLAG = False
    t = threading.Thread(target=animate, args=(text,), daemon=True)
    t.start()

def done():
    global DONE_FLAG
    DONE_FLAG = True