from reddit import Reddit
from time import time

TARGET_SUBREDDIT = "GameDeals"


def main():
    reddit = Reddit(TARGET_SUBREDDIT)
    reddit.start()

def timedMain():
    startTime = time()
    main()
    execTime = time() - startTime
    print(f"Execution took {int(execTime)} seconds")


if __name__ == "__main__":
    timedMain()