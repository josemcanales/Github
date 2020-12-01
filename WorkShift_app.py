
import time
from graphics import *

def start_window():

    win = GraphWin("WorkShift", 900, 700)
    win.setCoords(0, 0, 1000, 1000)

    running = True

    Image(Point(270, 500), "./Logo_WorkShift.png").draw(win)

    Rectangle(Point(550, 300), Point(950, 800)).draw(win)

    Text(Point(750, 740), "Email").draw(win)
    email = Entry(Point(750, 700), 30)
    email.draw(win)

    Text(Point(750, 640), "Password").draw(win)
    password = Entry(Point(750, 600), 30)
    password.draw(win)

    Text(Point(750, 600), "mdphide").draw(win)

    log_in = Rectangle(Point(650, 500), Point(850, 450))
    log_in.setFill("blue")
    log_in.draw(win)
    log_in = Text(Point(750, 475), "Log in")
    log_in.setStyle("bold")
    log_in.draw(win)

    close = Rectangle(Point(650, 150), Point(850, 200))
    close.setFill("red")
    close.draw(win)
    close = Text(Point(750, 175), "Close")
    close.setStyle("bold")
    close.draw(win)

    while running:

        click = win.getMouse()
        if 850 > click.getX() > 650 and 200 > click.getY() > 150:
            running = False
            win.close()
        elif 850 > click.getX() > 650 and 500 > click.getY() > 450:
            user_email = email.getText()
            user_password = password.getText()

            running = False
            win.close()
            calendar_week(user_email, user_password)
        else:
            pass


def calendar_week(user_email, user_password):

    win = GraphWin("WorkShift", 900, 700)
    win.setCoords(0, 0, 700, 700)

    running = True

    data_storing = open("Info_User&Events", "w")

    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday",
            "Mon": [1, "Monday"], "Tue": [2, "Tuesday"], "Wed": [3, "Wednesday"],
            "Thu": [4, "Thursday"], "Fri": [5, "Friday"], "Sat": [6, "Saturday"], "Sun": [7, "Sunday"]}
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    user_info = {user_email: user_password}
    events = {}

    for i in range(1, 8):
        x = Line(Point(24 + (i * 96.5), -1), Point(24 + (i * 96.5), 600))
        x.setWidth(10)
        x.setFill(color_rgb(0, 0, 160))
        x.draw(win)

    left_line = Line(Point(24, -1), Point(24, 601))
    left_line.setWidth(10)
    left_line.setFill(color_rgb(0, 0, 160))
    left_line.draw(win)

    for i in range(1, 12):
        y = Line(Point(24, i * 50), Point(700, i * 50))
        y.setWidth(2)
        y.setFill(color_rgb(0, 0, 160))
        y.draw(win)

    top_line = Line(Point(24, 600), Point(701, 600))
    top_line.setWidth(2)
    top_line.setFill(color_rgb(0, 0, 160))
    top_line.draw(win)

    for i in range(12):
        if i < 5:
            set_hour = Text(Point(10, 600 - (i*50)), f"0{i*2}:00")
            set_hour.setSize(8)
            set_hour.setStyle("bold italic")
            set_hour.draw(win)
        else:
            set_hour = Text(Point(10, 600 - (i * 50)), f"{i * 2}:00")
            set_hour.setSize(8)
            set_hour.setStyle("bold")
            set_hour.draw(win)

    local_time = time.localtime(time.time())

    week_day = local_time.tm_wday
    month_day = local_time.tm_mday
    month = local_time.tm_mon
    year = local_time.tm_year

    if month_day == 1 or month_day == 21 or month_day == 31:
        today = Text(Point(350, 670), f"Today: {days[week_day+1]} {month_day}st {months[month]} {year}")
        today.setSize(30)
        today.setStyle("bold italic")
        today.draw(win)

    elif month_day == 2 or month_day == 22:
        today = Text(Point(350, 670), f"Today: {days[week_day+1]} {month_day}nd {months[month]} {year}")
        today.setSize(30)
        today.setStyle("bold italic")
        today.draw(win)

    elif month_day == 3 or month_day == 23:
        today = Text(Point(350, 670), f"Today: {days[week_day+1]} {month_day}rd {months[month]} {year}")
        today.setSize(30)
        today.setStyle("bold italic")
        today.draw(win)

    else:
        today = Text(Point(350, 670), f"Today: {days[week_day+1]} {month_day}th {months[month]} {year}")
        today.setSize(30)
        today.setStyle("bold italic")
        today.draw(win)

    for i in range(7):
        date = Text(Point(24 + ((i+0.5) * 96.5), 620), f"{days[i+1]}")
        date.setSize(20)
        date.draw(win)

    minute = local_time.tm_min
    hour = local_time.tm_hour

    y_now = Line(Point(24, 600 - (hour*25)), Point(700, 600 - (hour*25)))
    y_now.move(0, -minute * 25 / 60)
    y_now.setWidth(2)
    y_now.setFill(color_rgb(255, 0, 0))
    y_now.draw(win)

    add_event_button = Rectangle(Point(40, 650), Point(80, 690))
    add_event_button.setOutline("blue")
    add_event_button.setFill("red")
    add_event_button.draw(win)

    add_event_txt = Text(Point(60, 670), "Add\nEvent")
    add_event_txt.setStyle("bold")
    add_event_txt.draw(win)

    Line(Point(10, 670), Point(30, 670)).draw(win)
    Line(Point(25, 660), Point(30, 670)).draw(win)
    Line(Point(25, 680), Point(30, 670)).draw(win)

    Line(Point(90, 670), Point(110, 670)).draw(win)
    Line(Point(90, 670), Point(95, 660)).draw(win)
    Line(Point(90, 670), Point(95, 680)).draw(win)

    quit_button = Rectangle(Point(620, 650), Point(660, 690))
    quit_button.setOutline("red")
    quit_button.draw(win)
    quit_txt = Text(Point(640, 670), "Quit")
    quit_txt.setStyle("bold")
    quit_txt.draw(win)

    while running:
        click = win.getMouse()

        if 80 > click.getX() > 40 and 690 > click.getY() > 650:
            event = add_event_window()

            title = event[0]
            wday = event[1]
            start_hour = int(event[2][:2])
            end_hour = int(event[3][:2])
            start_min = int(event[2][2:])
            end_min = int(event[3][2:])

            events[title] = (event[2], event[3])

            x = 24 + ((days[wday][0]-0.5) * 96.5)
            y_start = 600 - (start_hour*25) - (start_min * 25 / 60)
            y_end = 600 - (end_hour*25) - (end_min * 25 / 60)
            y_centered = (y_start + y_end) / 2

            event_rect = Rectangle(Point(24 + ((days[wday][0] - 1) * 96.5), y_start), Point(24 + (days[wday][0] * 96.5), y_end))
            event_rect.setFill("red")
            event_rect.draw(win)

            event_txt = Text(Point(x, y_centered), f"{title}\n{start_hour}h{event[2][2:]} - {end_hour}h{event[3][2:]}")
            if end_hour - start_hour < 2:
                event_txt.setSize(12)
            else:
                event_txt.setSize(18)
            event_txt.setStyle("bold")
            event_txt.draw(win)
        elif 660 > click.getX() > 620 and 690 > click.getY() > 650:
            running = False
            print(f"{user_email}, {user_info[user_email]}", file=data_storing)
            for event in events.keys():
                print(f"{event}, {events[event]}", file=data_storing)
            data_storing.close()
        else:
            pass

    win.close()


def add_event_window():

    win = GraphWin("Add Event", 400, 500)
    win.setCoords(0, 0, 100, 100)
    running = True

    Text(Point(50, 90), "Event Title").draw(win)
    title = Entry(Point(50, 85), 30)
    title.draw(win)

    Text(Point(50, 70), "Event Week Day (e.g Mon/Tue/Wed...)").draw(win)
    wday = Entry(Point(50, 65), 30)
    wday.draw(win)

    Text(Point(50, 50), "Event Start Time (e.g 0945 for 9h45)").draw(win)
    start = Entry(Point(50, 45), 30)
    start.draw(win)

    Text(Point(50, 30), "Event End Time (e.g 1830 for 18h30)").draw(win)
    end = Entry(Point(50, 25), 30)
    end.draw(win)

    add_button = Rectangle(Point(35, 15), Point(65, 5))
    add_button.setFill("blue")
    add_button.draw(win)
    add = Text(Point(50, 10), "Add")
    add.setStyle("bold")
    add.draw(win)

    while running:

        click = win.getMouse()
        if 65 > click.getX() > 35 and 15 > click.getY() > 5:
            E_title = title.getText()
            E_wday = wday.getText()
            E_start = start.getText()
            E_end = end.getText()
            win.close()
            return [E_title, E_wday, E_start, E_end]
        else:
            pass


if __name__ == '__main__':
    start_window()



