from datetime import datetime as dt

def get_current_datetime_hr():
    pass
def get_current_datetime_de():
    pass

current_moment = dt.now()

print(current_moment)

print(current_moment.year)


current_moment_str = current_moment.strftime('%d %D')
print(current_moment_str)

 