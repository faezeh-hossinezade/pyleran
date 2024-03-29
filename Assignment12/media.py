import pytube

class Media:
    def __init__(self, name , director , IMDB_score , url , duration , casts):
        self.name = name
        self.director = director
        self.score = IMDB_score
        self.url = url
        self.duration=duration
        self.casts=casts
        
    
    def showinfo(self):
        print()
        if self.type=="film":
            print("name \t   director \t    IMDBscore \t duration \t\t casts  \t\t production year ")
            print(self.name + "  " +  self.director + " \t " +  self.imdb_score + " \t " + self.duration + "   " + self.casts + "   " + self.productionyear )
            print("\n It is a movie. \n")

        elif self.type=="series":
            print("name \t   director \t    IMDBscore \t\t casts  \t\t production year \t episod number")
            print(self.name + "  " +  self.director + " \t " +  self.imdb_score + "   " + self.casts + "   " + self.productionyear + " \t " + self.episodnumber )
            print("\n It is a series. \n")

        elif self.type=="documentary":
            print("name \t   director \t    IMDBscore \t duration \t\t casts  \t\t production year ")
            print(self.name + "  " +  self.director + " \t " +  self.imdb_score + " \t " + self.duration + "   " + self.casts + "   " + self.productionyear )
            print("\n It is a documentary. \n")

        else:
            print("name \t   director \t    IMDBscore \t\tcasts\t\t production year\t genre")
            print(self.name + "  " +  self.director + " \t " +  self.imdb_score + "   " + self.casts + "   " + self.productionyear + " \t " + self.genre)
            print("\n It is a clip. \n")

        
    def download(self):
        link=self.url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename='file.mp4')