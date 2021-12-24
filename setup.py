from sqlite3.dbapi2 import connect
import time, os, sqlite3, json
a = open("config.json", "w")
e = 0
n = "Users.db"
def loop():
    start("yes")

def start(error):
    if error == "no":
        print("")
    else:
        print("there was an error last time you tried answering. please just use y and n \n")  
    a = input("This setup just makes an sqli database to store the keys and ip of users \n do you wish to continue? (y or n) \n @~~>")
    if a =="y":
        con = connect(n)
        c = con.cursor()
        codestufflolxdlmaoxdxdxdxdxdxd ='''CREATE TABLE Users(
           Username CHAR(20) NOT NULL,
           Key CHAR(20) NOT NULL,
           Ip CHAR(20)
        )'''
        c.execute(codestufflolxdlmaoxdxdxdxdxdxd)
        print("done making the database")
        con.commit()
        con.close()
        token = input("if you are going to use the discord bot please input your token below  \n just put the word no if your not gunna use it! \n @~~>")
        if token == "no":
            print(":) enjoy")
        else: 
            serverid = input("Put the id of your server here \n @~~>")
            with open("config.json", "w") as txt:
                x = '{\n    "tokenxxa":"tosk",\n    "sevaidyannoo":"sid"\n}'
                aaaaaaaaaa = x.replace("tosk", token)
                fin = aaaaaaaaaa.replace("sid", serverid)   
                print(fin)
                txt.write(fin)
    elif a =="n":
        print("this will now close")
        time.sleep(1)
        exit()
    else:
        os.system("cls")
        loop()


start("no")