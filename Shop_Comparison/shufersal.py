from multiprocessing import Process

from Shop_helpers import get_progress_percent
from base_end_functions import shufersal_main


def shufersal_double_process():
    p1 = Process(target=shufersal_main)
    p1.start()
    p2 = Process(target=get_progress_percent("source-files\shufersal-src-csv.csv", "out-files\Sufersal-out-csv.csv",
                                             hebrew_shop_name="Shufersal"))
    p2.start()


if __name__ == '__main__':
    shufersal_double_process()
