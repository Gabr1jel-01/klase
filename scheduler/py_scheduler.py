from datetime import datetime as dt



current_moment = dt.now()

print(current_moment)

print(current_moment.year)


current_moment_str = current_moment.strftime('%d %D')
print(current_moment_str)