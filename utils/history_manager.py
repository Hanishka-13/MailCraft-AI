import json
from datetime import datetime
def save_history(receiver,subject):
    try:
        with open("data/history.json","r") as f:
            history=json.load(f)
    except:
        history=[]
    history.append({
        "receiver":receiver,
        "subject":subject,
        "time":str(datetime.now())
    })
    with open("data/history.json","w") as f:
        json.dump(history,f,indent=4)
def load_history():
    try:
        with open("data/history.json","r") as f:
            return json.load(f)
    except:
        return []