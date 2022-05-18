import twint

c = twint.Config()

c.Username = "elonmusk"
#c.Custom["tweet"] = ["user_id", "created_at", "name", "username", "tweet", "language", "mentions", "urls", "photos", "", "replies_count" ]
c.Since = "2022-05-03"
c.Until = "2022-05-05"
c.Limit = 1 # number of Tweets to scrape
#c.Limit = 1000 # number of Tweets to scrape
c.Store_json = True       # store tweets in a csv file
c.Lang = "en"
c.Output = "myresearch.json"     # path to json file

twint.run.Search(c)
