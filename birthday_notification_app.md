## A birthday app with notification
```python
import os
import datetime

def get_birthdays_list():
    # Sample data
    birthdays = {
        "John Doe": "1990-01-01",
        "Jane Doe": "1992-02-28",
        "Bob Smith": "1993-03-15"
    }
    return birthdays

def send_notification(name, date):
    # Dummy function to simulate sending a birthday message
    print(f"Sending birthday message to {name} on {date}")

def check_birthday():
    today = datetime.datetime.now().strftime("%m-%d")
    birthdays = get_birthdays_list()

    for name, bday in birthdays.items():
        bday_month_day = datetime.datetime.strptime(bday, "%Y-%m-%d").strftime("%m-%d")
        if bday_month_day == today:
            send_notification(name, bday)

if __name__ == "__main__":
    check_birthday()

```