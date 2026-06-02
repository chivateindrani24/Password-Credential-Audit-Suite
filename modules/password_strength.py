import re
def analyze_password(password):
    score=0
    if len(password)>=12: score+=2
    if re.search("[A-Z]",password): score+=1
    if re.search("[a-z]",password): score+=1
    if re.search("[0-9]",password): score+=1
    if re.search("[^A-Za-z0-9]",password): score+=1
    return {"password":password,"score":score}
