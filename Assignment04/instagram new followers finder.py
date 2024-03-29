import instaloader
import getpass

with open("currentfollower.txt", "w") as main_file:
    current_follower=[]
    for line in main_file.readlines():
        current_follower.append(line)
    
L=instaloader.Instaloader()

ussername=input('Enter Your Username in Instagram:')
password=getpass.getpass()
profile = instaloader.Profile.from_username(L.context,'geeks_for_geeks')
followers = profile.get_followers()

new_follow=[]
for follower in followers:
    new_follow.append(follower)
    
for follower in new_follow:
    if follower not in current_follower:
        print(f'{follower} is new follower')

with open('new_followers.txt', 'w') as file:
    for follower in new_follow:
        file.write(f'{follower}\n')