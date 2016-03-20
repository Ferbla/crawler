import praw

class reddit:
    def __init__(self, sub):
        self.sub = sub

    def get_sub(self, lim=5):
        try:
            r = praw.Reddit(user_agent='news_reader')
            subs = r.get_subreddit(self.sub).get_hot(limit=lim)
            submission_form = "{}) {}  ({}): <{}>"
            count = 1
            url = ""

            for sub in subs:
                print("--------------------------------------------------------")
                print(submission_form.format(count, sub.title, sub.author, sub.url))
                count += 1
        except praw.errors.NotFound:
            print("Not found")
