import sqlite3

con = sqlite3.connect('Students.db')
cur = con.cursor()

cur.execute('''CREATE TABLE Topic
				(Id integer primary key, Name varchar)''')

cur.execute('''CREATE TABLE Question 
                (Id integer, Question varchar, Selection_A varchar, Selection_B varchar, Selection_C varchar, Selection_D varchar, Answer char, Topic_Id integer, FOREIGN KEY(Topic_Id) REFERENCES Topic(Id))''')


#continue Add the topic
cur.execute("INSERT INTO Topic VALUES(1,'Adjectives and adverbs')")



#https://www.englisch-hilfen.de/en/exercises/adjectives_adverbs/order.htm
#Answer must be in upper case
#Topic Id based on the topic you insert to the Topic table 
#Choose those exercise that have selection
cur.execute("INSERT INTO Question VALUES(1,'_________car','a black new','a new black','-','-','B','1')")





# Save (commit) the changes
con.commit()
con.close()
