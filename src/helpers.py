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

def loading(text, count):
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

def countdown(text, count):
    while count > 0:
        if DONE_FLAG:
            sys.stdout.write(f'\r{text}    ')  # clear countdown timer symbol...
            sys.stdout.flush()
            break
        sys.stdout.write(f'\r{text} {count} ')  # some buffer to overwrite trailing numbers...
        sys.stdout.flush()
        time.sleep(1)
        count -= 1
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_animated_text(text, count=0, func=loading):
    """
    Prints a text followed by a kind of animation. MUST be used in pair with done()
    """
    global DONE_FLAG
    DONE_FLAG = False
    t = threading.Thread(target=func, args=(text, count,), daemon=True)
    t.start()

def done():
    global DONE_FLAG
    DONE_FLAG = True