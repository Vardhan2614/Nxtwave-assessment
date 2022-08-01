import mysql.connector as mysql
import crawl_quotes
import json

mydb = mysql.connect(host="localhost",user="root",passwd="2614",db="jsonfiles")

my_cursor = mydb.cursor()

json_object = crawl_quotes.original_json_file

for items in json_object["quote"]:
    quote = items.get("quote")
    author = items.get("author")
    tags = items.get("tags")
    tags_list = ", ".join("?"*len(tags))

    my_cursor.execute("insert into Quotes(quote,author,tags)values(%s,%s,%s)",(quote,author, json.dumps(tags)))

mydb.commit()
mydb.close()