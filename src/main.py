import argparse
from reddit import Reddit
from time import time, sleep


TARGET_SUBREDDIT = "GameDeals"


def main():
    startTime = time()
    parser = argparse.ArgumentParser(description='Scraps /r/GameDeals for yuge deal.')
    parser.add_argument('--sleep', type=int, default=5, help='Sleep duration before autorun cmd window closes')

    args = parser.parse_args()

    reddit = Reddit(TARGET_SUBREDDIT)
    reddit.start()

    execTime = time() - startTime

    sleep(0.5)

    print(f"Execution took {int(execTime)} seconds")

    sleep(args.sleep)

if __name__ == "__main__":
    main()
