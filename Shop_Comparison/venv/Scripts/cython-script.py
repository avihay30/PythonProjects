#!C:\Develpment\PycharmProjects\Shop_Comparison\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cython==0.29.14','console_scripts','cython'
__requires__ = 'cython==0.29.14'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cython==0.29.14', 'console_scripts', 'cython')()
    )
