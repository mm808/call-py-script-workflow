import datetime

def echo_stuff():
    now = datetime.datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is {formatted_date_time})

Current date and time: 2025-01-20 19:42:16

if __name__ == "__main__":
    echo_stuff()
