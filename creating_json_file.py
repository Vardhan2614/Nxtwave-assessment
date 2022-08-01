import json 
import crawl_quotes 

def create_json_file(path,filename,data):
    filepath = "./"+path+"/"+filename
    with open(filepath,"w") as fp:
        json.dump(data,fp,indent=4)

path = "./"
filename = "quotes.json"
data = crawl_quotes.original_json_file

create_json_file(path,filename,data)


