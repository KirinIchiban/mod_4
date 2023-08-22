#1 занятие 
def s_counter(string):
    syms_sounter = {}
    for symbol in string:
        syms_sounter[symbol] = syms_sounter.get(symbol, 0) + 1
    print(syms_sounter)

s_counter('aaabbcddee')