class WatchlistEntry():
    def __init__(self, submission):
        super().__init__()
        self.keyword = submission.keyword
        self.flair = submission.link_flair_text
        self.url = submission.url
        self.title = submission.title
        self.permalink = submission.permalink
        self.created = submission.created_utc
