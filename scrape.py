from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

data = scrape(words=['elon', 'Elon', 'ELON', 'musk', 'Musk', 'MUSK', 'buy twitter', 'buying twitter', 'own twitter'], 
                since="2022-03-14", 
                until="2022-05-14", 
                interval=1, 
                headless=False,  
                lang="en")


# data = scrape(words=['bitcoin','ethereum'], since="2021-10-01", until="2021-10-05", from_account = None,         interval=1, headless=False, display_type="Top", save_images=False, lang="en",
#	resume=False, filter_replies=False, proximity=False, geocode="38.3452,-0.481006,200km")