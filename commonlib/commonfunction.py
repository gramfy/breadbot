####Common function for the bot####

#subredit getter
#info: https://www.jcchouinard.com/reddit-api-without-api-credentials/
import requests
import json

def get_subreddit(subreddit, listing, limit, timeframe):
    #format: isGettingData_sucpcess, json_data_from_requests
    data = [False, "json"]
    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}"
        jsondata = requests.post(base_url, headers={"User-agent": "breadbot"})
        data = [True, jsondata.text]
        return data
    except:
        data = [False, "failed"]
        print("An error has occured trying to gather subreddit data.")
        return data


def construct_redditjson(base):
    datadictionary = json.loads(base)
    subreddit = datadictionary["data"]["children"][0]["data"][
        "subreddit_name_prefixed"]
    title = datadictionary["data"]["children"][0]["data"]["title"]
    selftext = datadictionary["data"]["children"][0]["data"]["selftext"]
    url = datadictionary["data"]["children"][0]["data"]["url"]
    upvote = datadictionary["data"]["children"][0]["data"]["ups"]
    downvote = datadictionary["data"]["children"][0]["data"]["downs"]
    nsfw = datadictionary["data"]["children"][0]["data"]["over_18"]
    
    data = {
        "subreddit": subreddit,
        "title": title,
        "selftext": selftext,
        "url": url,
        "upvote": upvote,
        "downvote":downvote,
        "isnsfw":nsfw,
    }
    return data
