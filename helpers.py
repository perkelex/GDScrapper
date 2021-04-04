FORBIDDEN_FLAIRS = ["Console", "US Only", "Expired"]

def contains_forbidden_flairs(submission):
        """
        Checks submission flair for values that would make the submission uninteresting.
        """

        for flair in FORBIDDEN_FLAIRS:
            if flair in submission.link_flair_text:
                return True
        return False