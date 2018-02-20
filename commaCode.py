def comma(lv):
    for i in range(0, len(lv) - 1):
        print(str(lv[i]), end = ', ')
    else:
        print('and' + ' ' + str(lv[-1]))
    return

