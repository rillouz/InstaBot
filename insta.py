from instabot import Bot
import time
import random



username = "USERNAME"
password="PASSWORD"
name_to_explore = "USERNAME1"

class MyBot(Bot):
    def __init__(self, username, password):
       self.bot = Bot()
       self.bot.login(username=username, password=password)

    def __to_username(self,list_ids):
        print("Getting insta names with id")
        dictionnary_names = {} #key: id , value: insta name
        for id in list_ids:
            alea = random.random()
            time.sleep(alea)
            print(id)
            user = self.bot.get_username_from_user_id(id)
            print(user)
            dictionnary_names[id] = user
        return(dictionnary_names)


    def get_follower_info(self,name_to_explore,write= True): #writes and returns 
        ######  get follower info #######
        my_followers = self.bot.get_user_followers(name_to_explore)
        my_followings = self.bot.get_user_following(name_to_explore)

        dict_followers = self.__to_username(my_followers)
        dict_followings =self.__to_username(my_followings)

        if write: 
            idontfollow =[]
            for element in dict_followers.values():
                if element not in dict_followings.values():
                    idontfollow.append(element)
            with open('idontfollow.txt', 'w') as f:
                f.write(str(idontfollow))


            dontfollowme =[]
            for element in dict_followings.values():
                if element not in dict_followers.values():
                    dontfollowme.append(element)

            with open('dontfollowme.txt', 'w') as f:
                f.write(str(dontfollowme))
        
        return(dict_followers,dict_followings)



    def get_likers(self, insta_name):

        dict_followers,dict_followings =  self.get_follower_info(name_to_explore,write= True)
        id_medias = self.bot.get_total_user_medias(insta_name) 
        print("GOT MEDIAS of {}".format(insta_name))

        
        followers_by_media = {}

        for media in id_medias:
            time.sleep(1)
            print("Searching followers for media {}".format(media))
            followers_by_media[media]= self.bot.get_media_likers(media)


        names_duplicate= [] ##names but with duplicates
        for idx in followers_by_media.keys():
            names_duplicate+= followers_by_media[idx]
        all_names = list(set(names_duplicate))
        random.shuffle(all_names)

        print("Getting insta names with id")
        dictionnary_names = {} #key: id , value: insta name
        for id in all_names:
            alea = random.random()
            time.sleep(alea/4)
            print(id)
            user = self.bot.get_username_from_user_id(id)
            print(user)
            dictionnary_names[id] = user


        print("Getting urls of medias with id")
        dict_id_media = {} #key : id media, value: url media
        for id in id_medias:
            alea = random.random()
            time.sleep(alea/2)
            print(id)
            media = self.bot.get_link_from_media_id(id)
            print(media)
            dict_id_media[id] = media


        
        link = 'number_like_by_media{}.txt'.format(insta_name)
        with open(link, 'w') as f:
            for media in followers_by_media:
                f.write("{} : {}".format(dict_id_media[media],len(followers_by_media[media])))
                f.write("\n")


        media_by_followers = {} #dictionnary giving the list of media liked by a follower
        for name in all_names:
            media_by_followers[name]=[]
            for media in followers_by_media:
                if name in followers_by_media[media]:
                    media_by_followers[name].append(media)
        
        
        media_by_followers = {k: v for k, v in sorted(media_by_followers.items(), key=lambda item: len(item[1]), reverse=True)} #sort by number of likes


        link = 'media_by_followers{}.txt'.format(insta_name) #gives all the data 
        with open(link, 'w') as f:
            f.write(str(media_by_followers))
            
        count_media_by_followers = {} #key: insta name, value: number of likes

        for id in media_by_followers.keys():
            name = dictionnary_names[id]
            count_media_by_followers[name] = len(media_by_followers[id])



        link = 'count_media_by_followers{}.txt'.format(insta_name)
        with open(link, 'w') as f:
            for pair in count_media_by_followers:
                f.write("{} : {}".format(pair,count_media_by_followers[pair]))
                f.write("\n")


def main():
    my_bot = MyBot(username=username, password=password)
    my_bot.get_likers(name_to_explore)



# Python program to use
# main for function call.
if __name__ == "__main__":
    main()
