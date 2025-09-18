

import datetime

fname=f"logfile_{datetime.date.today()}.txt"

with open(fname, "w") as fic:
    fic.write("The end")
