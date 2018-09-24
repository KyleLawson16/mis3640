import math

e = 0.0000001

def mysqrt(a):
    x = 3
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < e:
            break
        x = y
    return float(x)

def test_square_root():
    a_data, mysqrt_data, mathsqrt_data, diff_data = [], [], [], []
    for i in range(1,10):
        a_data.append(float(i))
        mysqrt_data.append(round(mysqrt(i), 11))
        mathsqrt_data.append(round(math.sqrt(i), 11))
        diff_data.append(mysqrt(i) - math.sqrt(i))
    titles = ['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff']
    data = [titles] + list(zip(a_data, mysqrt_data, mathsqrt_data, diff_data))
    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(14) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))

test_square_root()
