from datetime import date

from models import BotProbability
from twitter_handler import TwitterHandler

class BotometerService():
    def __init__(self):
        self.pegabot = BotProbability()  # module which proccess user data and tweets and gives a result
        self.twitter_handler = TwitterHandler()

    def catch(self, handle):
        try:
            '''
            1. verify if the analisis is valid (by same version of the model or cachetime still valid)
            1.1. if stills valid, update times_served for the analisis row
            2. if not, find user on twitter, perform another analisis, save analises to database
            3. return the new analisis to client
            '''
            response = self.twitter_handler.findByHandle(handle=handle) # check on twitter
            if 'api_errors' not in response: # if finds the user on twitter performs the analisis and saves to the database
                timeline = self.twitter_handler.getUserTimeline(response.twitter_id)
                user = self.twitter_handler.getUser(response.twitter_id)
                
                if 'api_errors' in timeline: 
                    if(date.today() == user[0]['created_at'].date()):
                        print("Account created today")
                        return {'api_errors': [{'code': '11', 'message:': 'Account created today.'}], 'codes': '11', 'reason': 'Too litle information available', 'args': 'Account created today.'}
                    return timeline
                probability = self.pegabot.botProbability(handle, timeline, user)  # bot probability

                # return analysis
                analise = [handle, probability.total, probability.pegabot_version]
                return user, timeline, analise
        except Exception as e:
            raise
        else:
            return response

    def botProbability(self, handle, user, timeline):
        p = BotProbability()
        response = p.botProbability(handle=handle, twitterTimeline=timeline, twitterUserData=user)
        return response