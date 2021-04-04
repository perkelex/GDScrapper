import praw
import re
import helpers
from decouple import config
from requests import Session


class Reddit():
    def __init__(self, subreddit, output_file_name="hits.txt"):
        super().__init__()
        self.session = Session()
        self.reddit = self.init_connection()
        self.subreddit = subreddit
        self.output_file_name = output_file_name
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
        self.get_submissions()
        self.parse_submissions()
        self.write_output()

    def write_output(self, path="./"):
        """
        Writes the links to the submissions whose title passed the parsing criteria to file.
        """

        if len(self.submissions) == 0:
            print("ERROR: Submission list is empty!")
            return

        with open(f"{path}{self.output_file_name}", "w") as out:
            count = 0
            for sub in self.submissions:
                count+=1
                out.write(f"{count}. [{sub.link_flair_text}]{sub.title}\n")
                out.write(f"{count}. {self.get_reddit_url()}{sub.permalink}\n")
                out.write(f"{count}. {sub.url}\n\n")

    def parse_submissions(self, subs=None, regex=None):
        """
        Parses each submission according to given regex
        """

        # for sub in self.submissions:
        #     if "100%" in sub.title:
        #         self.subs_100_off.append(sub)

        pass

    def get_submissions(self):
        """
        Fetches and filters submissions from preconfigured subreddit.
        """

        for submission in self.reddit.subreddit(self.subreddit).new(limit=1000):
            if submission.link_flair_text is None:
                self.submissions.append(submission)
            else:
                if not helpers.contains_forbidden_flairs(submission):
                    self.submissions.append(submission)

    def get_reddit_url(self):
        return self.reddit.config.reddit_url
