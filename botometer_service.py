
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

            user = self.twitter_handler.getUser(handle=handle) # check on twitter

            if user != False: # if finds the user on twitter performs the analisis and saves to the database
                timeline = self.twitter_handler.getUserTimeline(handle)

                if timeline == False:
                    return False
                probability = self.pegabot.botProbability(handle, timeline, user)  # bot probability
                print(probability)
                user = user[0]
                
                analise = [handle, probability.total, probability.pegabot_version]
                
                return user, timeline, analise
               
        except Exception as e:
            raise
        else:
            return -1

    def botProbability(self, handle, user, timeline):
        p = BotProbability()
        user = p.botProbability(handle=handle, twitterTimeline=timeline, twitterUserData=user)
        return user