from InstagramAPI import InstagramAPI
import time
from datetime import datetime
import random
from random import randint

def getFollowing(username,pwd):
    API = InstagramAPI(username,pwd)
    API.login()
    API.searchUsername(username)
    user_id=API.LastJson['user']['pk']
    #followersLim  =367# 1 dia 2 000 000 user
    followers = []
    next_max_id = ''

    g = API.getUserFollowings(user_id,next_max_id)
    temp = API.LastJson
    while 1:
        try:
            while g==False:
                print("wait")
                n = randint(50,90)
                time.sleep(3*n)
                g = API.getUserFollowings(user_id,next_max_id)
                temp = API.LastJson
            for item in temp["users"]:

                followers.append(item['pk'])
            if(temp["big_list"] == False):
                return followers
            next_max_id = temp["next_max_id"]
            print(next_max_id)
            g = API.getUserFollowings(user_id,next_max_id)
            temp = API.LastJson
        except Exception as e:
            print(e)
            print('end game')

#'username','full_name','pk','biography','city_name','address_street','public_email','external_lynx_url',
#'follower_count','following_count','media_count','is_verified','is_private','category',
#'public_phone_country_code','contact_phone_number','business_contact_method','is_business'

s1=getFollowing('ingeniero_gualteros','******')
#s1=getFollowing('nicogualteros_','-')

print(s1)