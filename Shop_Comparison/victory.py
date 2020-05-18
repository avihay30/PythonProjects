from multiprocessing import Process

from Shop_helpers import get_progress_percent
from base_end_functions import victory_main


def victory_double_process():
    p1 = Process(target=victory_main)
    p1.start()
    p2 = Process(
        target=get_progress_percent("source-files\Victory-src-csv.csv", 'out-files\Victory-out-csv.csv',
                                    hebrew_shop_name="Victory"))
    p2.start()


if __name__ == '__main__':
    victory_double_process()
