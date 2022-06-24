from matplotlib import pyplot as plt
import numpy as np
import urllib


def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0' + stock + '/chartdata;type=quote;range=10y/csv'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y%m%d')})

    plt.xlabel('x_label')
    plt.ylabel('y_label')
    plt.title('Plot title')
    plt.legend()
    plt.show()


graph_data(input('enter ticker: '))
