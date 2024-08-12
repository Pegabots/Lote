
import sys
import time
import csv

from botometer_service import BotometerService

import warnings
warnings.filterwarnings("ignore")

def main(argv):
    
    hashtag = argv[0]

    res = open('./Dados/result_'+hashtag+'.csv', 'a')
    res.write('handle,result,pegabot-version\n')

    user = open('./Dados/user_'+hashtag+'.csv', 'a')
    user.write('created_at;description;followers_count;friends_count;handle;lang;location;name;profile_image;twitter_id;twitter_is_protected;verified;withheld_in_countries\n')

    timeline = open('./Dados/timeline_'+hashtag+'.csv', 'a')
    timeline.write('tweet_author;tweet_contributors;tweet_created_at;tweet_favorite_count;tweet_favorited;tweet_geo;tweet_hashtags;tweet_id;tweet_is_retweet;tweet_lang;tweet_place;tweet_retweeted;tweet_source;tweet_text\n')

    with open('./Dados/handles_'+hashtag+'.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        b = BotometerService()
        for row in spamreader:
            #try:
            dataAnalyzed = b.catch(row[0])
            print(dataAnalyzed)
            #except:
            #    print("Tentando novamente")
            #    dataAnalyzed = b.catch(row[0])
            analise = 'Err'
            try:
                userData = dataAnalyzed[0]
                timelineData = dataAnalyzed[1]
                analise = dataAnalyzed[2]
                user.write(str(userData['id'])+';'+
                            str(userData['handle'])+';'+
                            str(userData['name'])+';'+
                            str(userData['description'].replace('\n', ''))+'";'+
                            str(userData['created_at'])+';"'+
                            str(userData['followers_count'])+';'+
                            str(userData['friends_count'])+';'+
                            str(userData['statuses_count'])+';'+
                            str(userData['favourites_count'])+';'+
                            str(userData['verified'])+'\n')
                for tweet in timelineData:
                    timeline.write(str(tweet['tweet_author_id'])+';'+
                                str(tweet['tweet_author'])+';'+
                                str(tweet['tweet_created_at'])+';'+
                                str(tweet['tweet_favorite_count'])+';'+
                                str(tweet['tweet_hashtags'])+';'+
                                str(tweet['tweet_retweet_count'])+';'+
                                str(tweet['tweet_is_retweet'])+';'+
                                str(tweet['tweet_is_quote'])+';'+
                                str(tweet['tweet_is_retweet'])+';'+
                                str(tweet['tweet_source'])+';'+
                                str(tweet['tweet_retweeted'])+';'+
                                str(tweet['in_reply_to_status_id'])+';'+
                                str(tweet['quoted_status_text'])+';"'+
                                str(tweet['text_user_mentions'])+';"'+
                                str(tweet['tweet_text'].replace('\n', ''))+'"\n')
                res.write(str(analise[2])+'\n')
            except:
                try:
                    res.write(str(dataAnalyzed[2][0])+','+str(dataAnalyzed[2][1])+','+str(dataAnalyzed[2][2])+'\n')
                except:
                    print(dataAnalyzed)
                    res.write(str(row[0])+', '+ str(dataAnalyzed)+', Err'+'\n')
            
            print(analise)
            time.sleep(2)

    user.close()
    timeline.close()
    res.close()

if __name__ == "__main__":
    main(sys.argv[1:])