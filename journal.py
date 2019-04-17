from datetime import datetime
import subprocess 

def create_and_start():
    t = str(datetime.now()).split()
    with open(t[0] + ".txt", "a") as journ:
        journ.write("\n" + t[1] + " " + t[0] + "\n")
    subprocess.run(["vim", t[0] + ".txt"])

create_and_start()
