from account import Account
from bank import Bank


def main():
    a1 = Account(1, 1000, "Alex")
    a2 = Account(2, 2500, "Kate")
    a3 = Account(3, 500, "Vova")

    tpl = (a1, a2, a3)

    print(Bank.show_all_account(tpl))
    print(f"Total is ${Bank.sum_all_balance(tpl)}")
    print(f"After month: {Bank.calc_sum_after_month(tpl)}")


if __name__ == "__main__":
    main()