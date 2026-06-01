from datetime import datetime

def getCurrentDateTime():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')
    