def stock_code_to_wind_code(stock):
    inner_stock = str(stock)
    orig_len = len(inner_stock)
    if orig_len < 6:
       inner_stock = '0'*(6-orig_len) + inner_stock


    if inner_stock[0] == '6':
        return inner_stock[0:6] + '.SH'
    elif inner_stock[0] == '1': #深圳分级基金
        return inner_stock[0:6] + '.SZ'
    elif inner_stock[0] == '5': #上海分级基金
        return inner_stock[0:6] + '.SH'
    elif inner_stock[0] == '0': #深圳主板或中小板
        return inner_stock[0:6] + '.SZ'
    elif inner_stock[0] == '3': # 创业板
        return inner_stock[0:6] + '.SZ'
    else:
        return 'ERROR.STOCK'
    
def string_into_sql(string):
    return '\'' + string + '\''
