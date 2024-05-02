query = input('Overtime? y/n ')
hr = input('Enter Hours:')
rt = input('Enter Rate:')
if str(query.lower()) == 'y':
    try:
        hr2 = float(hr)
        rt2 = float(rt)
        fin2 = (hr2*1.5) * rt2
        print('Pay:', fin2)
    except:
        print('I am sorry, please input a numerical value')
if str(query.lower()) == 'n':
    try:
        hr2 = float(hr)
        rt2 = float(rt)
        fin = hr2 * rt2
        print('Pay:', fin)
    except:
        print('I am sorry, please input a numeric value')