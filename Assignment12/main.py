from media import Media

VIDEOS = []

with open("Data.txt", "r") as f:
    for line in f:
        result = line.strip().split(",")
    # .strip() removes  leading and trailing spaces
        obj = Media(result[0], result[1], result[2], result[3], result[4], result[5])
        VIDEOS.append(obj)

# print (VIDEOS): it shows the memory address



def menu():
    print("1- Add")
    print("2- Edit")
    print("3 -Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Exit")


def add():

    name,director,IMDB_score,url,duration,casts = input("Enter the name of the film, the director, the score, the url, the duration, the casts").split(",")
    new_video = Media(name, director, IMDB_score, url, duration, casts)
    VIDEOS.append(new_video)


def edit():
    user_input = input("Enter video name: ")
    for video in VIDEOS:
        if video.name == user_input:
            video.show_inFo()
            break
    new_name = input("Enter a new name: ")
    new_director = input("Enter new director: ")
    new_IMBD_score = input("Enter new score: ")
    video.update({"name": new_name, "director": new_director, "IMDB_score": new_IMBD_score})
    print("Editted successfully")
    video.show_inFo()


def remove():
    datas = []
    user_input = input("Enter video name: ")
    for video in VIDEOS:
        if video.name == user_input:
            video.showinfo()
            confirm = input("confirm delete 'Y' or 'N': ")  
            if confirm == "Y":
                index = datas.index(video.name)
                datas[index] = ''
            with open('Data.txt', 'w') as file:
                for d in datas:
                    file.write(d)
            print('The item has been removed')
            break
            
        else:
            print('Product Not Found')



def search():
    print("Search by name")
    user_input = input("Enter video name: ")
    for video in VIDEOS:
        if video.name == user_input:
            video.show_info()
        else:
            print("name not matched any video")

        

def write_database():
    with open('Data.txt', 'w') as file:
        for video in VIDEOS:
                line = f"{video}"
                file.write(line)
    print("Database updated successfully")

def show():
    for video in VIDEOS:
        video.show_info()
        

while True:
    menu()
    choice = int(input("enter a number: "))
    if choice == 1 :
        add()
    elif choice == 2 :
        edit()
    elif choice == 3 :
        remove()
    elif choice == 4 :
        search()
    elif choice == 5 :
        show()
    elif choice == 6 :
        write_database()
        exit(0)
    else:
        print("Enter correctly!")