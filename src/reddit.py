import praw
import re
import helpers
import paths
from watchlist import WatchlistEntry
from decouple import config
from requests import Session


class Reddit():
    def __init__(self, subreddit, output_file_name=paths.OUTPUT_FILE):
        super().__init__()
        self.filter = helpers.Filter(watchlist=True)
        self.session = Session()
        self.reddit = self.init_connection()
        self.subreddit = subreddit
        self.output_file_name = output_file_name
        self.watchlist = helpers.parse_config("watchlist")
        self.watchlist_hits: List[WatchlistEntry] = []
        self.submissions = []
        self.subs_100_off = []
        self.subs_90_off = []
        self.subs_80_off = []
        self.subs_70_off = []
        self.subs_60_off = []
        self.subs_50_off = []
        self.subs_40_off = []
        self.subs_30_off = []
        self.subs_20_off = []
        self.subs_10_off = []

    def init_connection(self):
        return praw.Reddit(
        client_id=config("CLIENT_ID"),
        client_secret=config("CLIENT_SECRET"),
        password=config("PASSWORD"),
        requestor_kwargs={"session": self.session},
        user_agent=config("USER_AGENT"),
        username=config("USER"),
        )

    def start(self):
        helpers.print_animated_text("Scrapping...")
        self.get_submissions()
        self.parse_submissions()
        self.write_output()
        helpers.done()

    def write_output(self, path=f"{paths.OUTPUT_FILE}"):
        """
        Writes the links to the submissions whose title passed the parsing criteria to file.
        """

        if len(self.submissions) == 0:
            print("ERROR: Submission list is empty!")
            return

        with open(f"{self.output_file_name}", "w", encoding='utf-8') as out:
            self.write_header(out, "Watchlist hits")
            self.write_watchlist_hits(out)

            self.write_separator(out)

            self.write_header(out, r"100% off | FREE")
            self.write_entries(out, self.subs_100_off)

            self.write_separator(out)

            self.write_header(out, r"90% off")
            self.write_entries(out, self.subs_90_off)

            self.write_separator(out)

            self.write_header(out, r"80% off")
            self.write_entries(out, self.subs_80_off)

            self.write_separator(out)

            self.write_header(out, r"70% off")
            self.write_entries(out, self.subs_70_off)

            self.write_separator(out)

            self.write_header(out, r"60% off")
            self.write_entries(out, self.subs_60_off)

            self.write_separator(out)

    def parse_submissions(self):
        """
        Parses each submission according to given regex
        """

        for sub in self.submissions:
            if "100%" in sub.title:
                self.subs_100_off.append(sub)
            elif re.compile(r"9\d%").search(sub.title):
                self.subs_90_off.append(sub)
            elif re.compile(r"8\d%").search(sub.title):
                self.subs_80_off.append(sub)
            elif re.compile(r"7\d%").search(sub.title):
                self.subs_70_off.append(sub)
            elif re.compile(r"6\d%").search(sub.title):
                self.subs_60_off.append(sub)

    def get_submissions(self):
        """
        Fetches and filters submissions from preconfigured subreddit.
        """

        for submission in self.reddit.subreddit(self.subreddit).new(limit=1000):
            if self.filter.filter_watchlist(submission, self.watchlist):
                self.watchlist_hits.append(WatchlistEntry(submission))
            elif self.filter.filter_flair(submission):
                self.submissions.append(submission)

    def get_reddit_url(self):
        return self.reddit.config.reddit_url

    def write_entries(self, handler, sub_list):
        count = 0
        for sub in sub_list:
            count += 1
            handler.write(f"{count}. {helpers.get_nice_time(sub.created_utc)}\n")
            handler.write(f"{count}. [{sub.link_flair_text}]{sub.title}\n")
            handler.write(f"{count}. {self.get_reddit_url()}{sub.permalink}\n")
            handler.write(f"{count}. {sub.url}\n\n")

    def write_separator(self, handler):
        handler.write("{0:=>100}\n".format(""))

    def write_header(self, handler, text):
        handler.write(f"{text}\n\n")

    def write_watchlist_hits(self, handler):
        count = 0
        for sub in self.watchlist_hits:
            count += 1
            handler.write(f"{count}. {sub.keyword}\n")
            handler.write(f"{count}. {helpers.get_nice_time(sub.created)}\n")
            handler.write(f"{count}. [{sub.flair}]{sub.title}\n")
            handler.write(f"{count}. {self.get_reddit_url()}{sub.permalink}\n")
            handler.write(f"{count}. {sub.url}\n\n")