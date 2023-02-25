value_invested = 46_567.
factor = .075

#pierwszy rok

value_invested += value_invested * factor

#drugi rok
value_invested += value_invested * factor

#trzeci rok

value_invested += value_invested * factor

print('Przy zainwestowanych środkach 46 567 zł i stałym oprocentowaniu rocznym 7,5%, wartość inwestycji wyniesie ', round(value_invested, 2), ' zł' ', a zysk wyniesie ', round(value_invested, 2) - 46_567, ' zł.', sep='')