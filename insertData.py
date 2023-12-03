from DB import connection,cursor

val = [
    
("Good",	"좋아요"),
("Bad",	"나빠요"),
("Big",	"커요"),
("Small",	"작아요"),
("Long",	"길어요"),
("Short",	"짧아요"),
("Expensive",	"비싸요"),
("Cheap",	"싸요"),
("Busy",	"바빠요"),
("Delicious",	"맛있어요"),
("Difficult",	"어려워요"),
("Easy",	"쉬워요"),
("Far",	"멀어요"),
("Near",	"가까워요"),
("Clean",	"깨끗해요"),
("Dirty","더러워요"),
("Beautiful",	"예뻐요"),
("Kind",	"친절해요"),
("Quiet",	"조용해요"),
("Interesting",	"재미있어요"),
]
 
def add_vocab(kr, en, userid):
    insert_query = '''
            INSERT INTO Vocab(
                kr,
                en,
                userid
            )
            VALUES(
                ?,
                ?,
                ?
            )
        '''
    insert_values = (kr,en,userid)
    try:
        cursor.execute(insert_query, insert_values)
        connection.commit()
        print("data inserted")
        return True
    except:
        print("registered")
        return False
    


# for d in val:
#     succ = add_vocab(d[1], d[0], 1)
    