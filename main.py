
import time
import csv

from botometer_service import BotometerService

import warnings
warnings.filterwarnings("ignore")

hashtag = "#RadiolaoDoPT_1"

res = open('./Dados/result_'+hashtag+'.csv', 'a')
res.write('handle,result,pegabot-version\n')

user = open('./Dados/user_'+hashtag+'.csv', 'a')
user.write('created_at;default_profile;description;followers_count;friends_count;handle;lang;location;name;profile_image;twitter_id;twitter_is_protected;verified;withheld_in_countries\n')

timeline = open('./Dados/timeline_'+hashtag+'.csv', 'a')
timeline.write('tweet_author;tweet_contributors;tweet_created_at;tweet_favorite_count;tweet_favorited;tweet_geo;tweet_hashtags;tweet_id;tweet_is_retweet;tweet_lang;tweet_place;tweet_retweeted;tweet_source;tweet_text\n')

with open('./Dados/handles_'+hashtag+'.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    b = BotometerService()
    for row in spamreader:
        try:
            dataAnalyzed = b.catch(row[0])
        except:
            print("Tentando novamente")
            dataAnalyzed = b.catch(row[0])

        try:
            userData = dataAnalyzed[0]
            timelineData = dataAnalyzed[1]
            analise = dataAnalyzed[2]
            user.write(str(userData[0]['created_at'])+';'+
                        str(userData[0]['default_profile'])+';"'+
                        str(userData[0]['description'].replace('\n', ''))+'";'+
                        str(userData[0]['followers_count'])+';'+
                        str(userData[0]['friends_count'])+';'+
                        str(userData[0]['handle'])+';'+
                        str(userData[0]['lang'])+';'+
                        str(userData[0]['location'])+';'+
                        str(userData[0]['name'])+';'+
                        str(userData[0]['profile_image'])+';'+
                        str(userData[0]['twitter_id'])+';'+
                        str(userData[0]['twitter_is_protected'])+';'+
                        str(userData[0]['verified'])+';'+
                        str(userData[0]['withheld_in_countries'])+'\n')
            for tweet in timelineData:
                timeline.write(str(tweet['tweet_author'])+';'+
                            str(tweet['tweet_contributors'])+';'+
                            str(tweet['tweet_created_at'])+';'+
                            str(tweet['tweet_favorite_count'])+';'+
                            str(tweet['tweet_favorited'])+';'+
                            str(tweet['tweet_geo'])+';'+
                            str(tweet['tweet_hashtags'])+';'+
                            str(tweet['tweet_id'])+';'+
                            str(tweet['tweet_is_retweet'])+';'+
                            str(tweet['tweet_lang'])+';'+
                            str(tweet['tweet_place'])+';'+
                            str(tweet['tweet_retweeted'])+';'+
                            str(tweet['tweet_source'])+';"'+
                            str(tweet['tweet_text'].replace('\n', ''))+'"\n')
            res.write(str(analise[0])+','+str(analise[1])+','+str(analise[2])+'\n')
        except:
            res.write(',,,'+str(dataAnalyzed)+'\n')
        
        print(analise)
        time.sleep(2)

user.close()
timeline.close()
res.close()
