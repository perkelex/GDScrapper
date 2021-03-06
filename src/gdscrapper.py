import argparse
import helpers
from reddit import Reddit
from time import time, sleep


TARGET_SUBREDDIT = "GameDeals"


def main():
    startTime = time()
    parser = argparse.ArgumentParser(description='Scraps /r/GameDeals for yuge deals.')
    # parser.add_argument('--sleep', type=int, default=5, help='Sleep duration before autorun cmd window closes')
    # parser.add_argument('--cmd', default=False, type=bool, help="Adds delay if manually ran in CMD mode")

    args = parser.parse_args()

    reddit = Reddit(TARGET_SUBREDDIT)
    reddit.start()

    execTime = time() - startTime

    sleep(0.5)

    print(f"Execution took {int(execTime)} seconds")

    sleep(2)
    # if args.cmd:
    #     helpers.print_animated_text("Exiting in", args.sleep, helpers.countdown)
    #     sleep(args.sleep)
    helpers.done()

if __name__ == "__main__":
    main()
