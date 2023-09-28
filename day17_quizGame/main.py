#!/usr/bin/python3

class User:
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

class Car:
    def __init__(self, seats):
        self.seats

    def enter_race_mode(self):
        self.seats = 2


user1 = User("001", "adelmanp")
user2 = User("002", "oudheusdenm")
user1.follow(user2)
print(f"User 1 followers: {user1.followers}")
print(f"User 1 following: {user1.following}")
print(f"User 2 followers: {user2.followers}")
print(f"User 2 following: {user2.following}")
