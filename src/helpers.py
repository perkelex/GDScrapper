import itertools
import threading
import time
import sys
import json
import paths
from datetime import datetime


DONE_FLAG = False


class Filter:

    def __init__(self, watchlist=False):
        super().__init__()
        self.WATCHLIST = watchlist
        self.forbidden_flairs = parse_config("forbidden_flairs")

    def contains_forbidden_flairs(self, submission):
        """
        Checks submission flair for values that would make the submission uninteresting.
        """

        if submission.link_flair_text is None:
            return False

        for flair in self.forbidden_flairs:
            if flair in submission.link_flair_text:
                return True
        return False

    def filter_flair(self, submission):
        if not self.contains_forbidden_flairs(submission):
            return True
        return False

    def filter_watchlist(self, submission, watchlist):
        if not self.filter_flair(submission):
            return False

        for game_names in watchlist:
            for game_name_variant in game_names:
                if game_name_variant in submission.title:
                    submission.keyword = game_name_variant
                    return True
        return False

    def filter(self, submission, watchlist):
        if self.WATCHLIST:
            return self.filter_watchlist(submission, watchlist)
        else:
            return self.filter_flair(submission)


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

def parse_config(key):
    with open(paths.CONFIG_FILE, "r") as config:
        return json.load(config)[key]

def get_nice_time(utc_time):
    return datetime.fromtimestamp(utc_time).strftime("%Y-%m-%d")
