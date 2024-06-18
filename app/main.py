def calculate_investing(cash, period, age, rate, max_age, base_rate=0):
    res = []
    p = 0
    if period == "month":
        p = 12
    elif period == "day":
        p = 365

    base_sum = p * cash
    print(base_sum * (max_age - age))

    res.append([1, base_sum, age + 1, base_sum])

    def count_year():
        if res[-1][2] == max_age:
            return

        i, cur_sum, cur_age, bs = (
            res[-1][0] + 1,
            res[-1][1],
            res[-1][2] + 1,
            res[-1][3] * (1 + base_rate / 100),
        )
        cur_sum = bs + cur_sum * (1 + rate / 100)
        cur_sum = round(cur_sum, 0)
        res.append([i, cur_sum, cur_age, bs])
        # print([i, cur_sum, cur_age])
        count_year()

    count_year()
    return res


result = calculate_investing(
    cash=20000, period="month", age=21, rate=4, max_age=26, base_rate=10
)

for row in result:
    print(
        f"i = {row[0]}, balance = {row[1]}, age = {row[2]}, add_sum = {row[3]} / add_per_month = {row[3] / 12}"
    )
