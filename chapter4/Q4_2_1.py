def f(n=0):
    week = ["水", "木", "金", "土", "日", "月", "火"]
    k = "後" if n > 0 else ("前" if n < 0 else "")
    return "今日は水曜日です" if n == 0 else f"{abs(n)}日{k}は{week[n%7]}曜日です"


n = int(input())
print(f(n))
