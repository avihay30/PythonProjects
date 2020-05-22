import threading
from time import sleep

from rami_levi import rami_levi_double_process
from shufersal import shufersal_double_process
# from victory import victory_double_process


def run_all_shops_simultaneously():
    p1 = threading.Thread(target=shufersal_double_process)
    p1.start()
    p2 = threading.Thread(target=rami_levi_double_process)
    sleep(1)
    p2.start()
    # p3 = threading.Thread(target=victory_double_process)
    # sleep(1)
    # p3.start()
    # shufersal_double_process()
    # rami_levi_double_process()


if __name__ == '__main__':
    run_all_shops_simultaneously()
