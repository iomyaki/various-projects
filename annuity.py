def annuityPaymentSchedule():
    import pandas as pd

    loanPrincipal = int(input('Введите сумму кредита, руб.: '))
    interest = float(input('Введите ставку, %: ')) / 100
    term = int(input('Введите срок выплаты кредита, месяцев: '))

    payment = loanPrincipal * (1 + interest / term) ** term / sum([(1 + interest / term) ** i for i in range(term)])

    df = pd.DataFrame(data={'Месяц':                   [n + 1 for n in range(term)],
                            'Ежемесячный платёж':      [round(payment, 2) for n in range(term)],
                            'Основной долг':           ['' for n in range(term)],
                            'Долг по процентам':       ['' for n in range(term)],
                            'Остаток основного долга': ['' for n in range(term)]
                            }
                      )

    for i in range(term):
        df.iloc[i, 2] = round(payment - loanPrincipal * interest / term, 2)
        df.iloc[i, 3] = round(loanPrincipal * interest / term, 2)
        df.iloc[i, 4] = abs(round(loanPrincipal - payment + loanPrincipal * interest / term, 2))
        loanPrincipal += loanPrincipal * interest / term - payment

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)


annuityPaymentSchedule()
