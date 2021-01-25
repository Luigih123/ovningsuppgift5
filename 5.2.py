import datetime
# här importerar jag nu tidens tid
while True:
# Här sätter jag en loop som loopar varje gång det är sant
    DT = datetime.datetime.now()
    pernum = input("Skriv ditt personnummer ÅÅÅÅMMDD: ")
# Här så sätter jag en input så att man kan skriva det den frågar efter
    DTpers = DT.strptime(pernum, '%Y%m%d')

    if (DT.month == DTpers.month and DT.day == DTpers.day):
        print("Grattis på födelsedagen!")
# Här är det en if för om det är det som programet har då får du detta svar
    else: 
        print("Du fyller inte år idag!")
# annars får du det här svaret