class Movie():
    def __init__(self,language,num_characters,length_in_minutes):
        self.lang=language
        self.charc=num_characters
        self.duartion=length_in_minutes
    def run(self):
        print("This is a "+self.lang + " movie with "+str(self.charc) +" characters "+" and is "+ str(self.duartion) + " minutes long.")
language=input()
num_characters=int(input())
length_in_minutes=int(input())
movie1=Movie(language,num_characters,length_in_minutes)
movie1.run()
