from multiprocessing import Process

from Shop_helpers import get_progress_percent
from base_end_functions import rami_levi_main


def rami_levi_double_process():
    p1 = Process(target=rami_levi_main)
    p1.start()
    p2 = Process(target=get_progress_percent("source-files\RamiLevi-src-csv.csv", 'out-files\RamiLevi-out-csv.csv',
                                             hebrew_shop_name="Rami Levi"))
    p2.start()


if __name__ == '__main__':
    rami_levi_double_process()
