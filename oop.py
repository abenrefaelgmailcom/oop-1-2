import math
from datetime import datetime
import time

class Timer:
    def __init__(self, name, duration):
        print('New Timer Created!')
        self.name = name
        self.duration = duration
        self.started_at = datetime.now().time()  # רק השעה
        self.created_at = datetime.now()         # תאריך מלא

    def __str__(self):
        return f"Timer '{self.name}' set to {self.duration} minutes (started at: {self.started_at.strftime('%H:%M:%S')})"

    def __repr__(self):
        return f"Timer('{self.name}', {self.duration})"

    def __del__(self):
        print(f"[DEL] Timer '{self.name}' is being removed")

# בנאי - constructor
t1 = Timer("Workout", 45)
t2 = Timer("Study", 30)

# תצוגת משתמש
print(t1.__str__())
print(t2)

# תצוגת מפתח
print(t1.__repr__())
print([t1, t2])  # __repr__ יופעל אוטומטית בתוך רשימות

# מאפיין דינמי - dynamic attribute
t1.paused = False
print("Dynamic attribute added: t1.paused =", t1.paused)

# מחיקת המאפיין
del t1.paused
print("Dynamic attribute removed")

# שמירה של כל הטיימרים ברשימה
timer_bag: list[Timer] = [t1, t2]
print("All timers:", timer_bag)  # מופעל __repr__

# הדפסת מבנה אובייקט עם __dict__
print(t1.__dict__)


#########
#########     +---------------------+
#########     |       Timer         |
#########     +---------------------+
#########     | - name: str         |
#########     | - seconds: int      |
#########     | + category: str (*) |
#########     +---------------------+
#########     | + __init__(name, seconds) |
#########     | + __str__() -> str       |
#########     | + __repr__() -> str      |
#########     + __del__()              |
#########     +---------------------+
#########     (*) dynamic attribute
