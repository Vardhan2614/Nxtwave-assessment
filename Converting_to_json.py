jsonobj = {"quote":[]}

def convert_to_json(description, author, tags):
    jsondata = {
        "quote": description,
        "author": author,
        "tags": tags
    }

    jsonobj["quote"].append(jsondata)

    return jsonobj