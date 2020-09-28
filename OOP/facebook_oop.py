"""
Facebook OOP
"""
import datetime

class FacebookUser:
    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email
        self._following = []
        self._posts = []

    def __str__(self):
        msg = f"{self.user_name} {self.email}"
        return msg
    
    def follow(self, followed_user):
        self._following.append(followed_user)
    
    def unfollow(self, unfollowed_user):
        # TODO : self._following'den silelim.

    def display_timeline(self):
        # TODO : takip edilen kullanıcıların son mesajlarını yazar.
    def post(self, message):
        post1 = Post(message)
        self_posts.append(post1)

class Post:
    def __init__(self, message):
        self.message = message
        self.post_date = datetime.datetime.now


user1 = FacebookUser("egeakertek", "ege.akertek@gmail.com")
user2 = FacebookUser("harrypotter", "wonder.wizard@gmail.com")
user3 = FacebookUser("hermionegranger","into.ron.not.harry@gmail.com")

print(user1)
print(user2)

user1.follow(user2)
user3.follow(user1)

user1.post("Abi Harry hermione'ye çılgınlar gibi aşıkmış")
user2.post("Mk aptal ege ne karıştırıyorsun ortalığı")
user3.post("NE?!")
