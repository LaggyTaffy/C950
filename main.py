import datetime

from routing import myHash


def main():
    print('--------------------------------')
    print('----- WGUPS Routing Program ----')
    print('------- Date:',datetime.datetime.now().strftime("%m/%d/%Y"),'-------')
    print('--------------------------------')
    print()
    print('--------------------------------')
    print(myHash.table)


main()
