def calculate_investing(cash, period, age, rate, max_age):
    res = []
    p = 0
    if period == "month":
        p = 12
    elif period == "day":
        p = 365

    base_sum = p * cash
    print(base_sum * (max_age - age))

    res.append([1, base_sum, age + 1])

    def count_year():
        if res[-1][2] == max_age:
            return

        i, cur_sum, cur_age = res[-1][0] + 1, res[-1][1], res[-1][2] + 1
        cur_sum = base_sum + cur_sum * (1 + rate / 100)
        cur_sum = round(cur_sum, 0)
        res.append([i, cur_sum, cur_age])
        print([i, cur_sum, cur_age])
        count_year()

    count_year()
    return res


result = calculate_investing(cash=10000, period="month", age=21, rate=4, max_age=35)

for row in result:
    print(f"i = {row[0]}, balance = {row[1]}, age = {row[2]}")
