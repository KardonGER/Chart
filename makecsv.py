import speedtest
import os.path
from datetime import datetime as dt


cycle = 1
filename = 'file.csv'


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload(pre_allocate=False)
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():
    # CSV check
    check = os.path.isfile(filename)
    # write to csv
    if not check:
        with open(filename, 'w') as f:
            f.write('datetime;download;upload;ping;\n')
            for i in range(cycle):
                print('Making test #{}'.format(i+1))
                t = dt.now()
                d, u, p = test()
                d = d / 1000
                u = u / 1000
                d_str = format(d)
                u_str = format(u)
                p_str = format(p)
                d = d_str[:d_str.find('.')]
                u = u_str[:u_str.find('.')]
                p = p_str[:p_str.find('.')]
                f.write('{};{};{};{}\n'.format(t, d, u, p))
    if check:
        with open(filename, 'a') as f:
            for i in range(cycle):
                print('Making test #{}'.format(i+1))
                t = dt.now()
                d, u, p = test()
                d = d / 1000
                u = u / 1000
                d_str = format(d)
                u_str = format(u)
                p_str = format(p)
                d = d_str[:d_str.find('.')]
                u = u_str[:u_str.find('.')]
                p = p_str[:p_str.find('.')]
                f.write('{};{};{};{}\n'.format(t, d, u, p))


if __name__ == '__main__':
    main()
