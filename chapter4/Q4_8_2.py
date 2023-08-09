# カレンダー
import calendar

from colorama import Fore, Style


def colored_calendar(year, month):
    cal = calendar.TextCalendar()
    cal.setfirstweekday(calendar.SUNDAY)
    header = f"{calendar.month_name[month]} {year}"
    weekday_names = [
        Fore.RED + "日",
        Fore.WHITE + "月",
        "火",
        "水",
        "木",
        "金",
        Fore.BLUE + "土" + Style.RESET_ALL,
    ]
    weekdays = " ".join(weekday_names)
    print(header.center(21))
    print(weekdays)

    for week in cal.monthdayscalendar(year, month):
        week_str = [f"{day:2}" if day != 0 else "  " for day in week]
        week_str = [
            f"{Fore.RED}{day}{Style.RESET_ALL}" if idx == 0 and day != "  " else day
            for idx, day in enumerate(week_str)
        ]
        week_str = [
            f"{Fore.BLUE}{day}{Style.RESET_ALL}" if idx == 6 and day != "  " else day
            for idx, day in enumerate(week_str)
        ]
        print(" ".join(week_str))


if __name__ == "__main__":
    year = int(input("年を入力してください: "))
    month = int(input("月を入力してください: "))
    if 1 <= month <= 12:
        colored_calendar(year, month)
    else:
        print("無効な月が指定されました。1から12の間で入力してください。")
