"""
Cash-clearing module
"""
from os import listdir
from os.path import isfile, join
import os


def clear_the_cash(invariant):
    """
    :param invariant: str() unique ip
    :return:
    --------
    Delete unnecessary files
    """
    mypath = os.getcwd()+"/templates/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    ok_ = [f for f in onlyfiles if invariant in f]
    for elm in ok_:
        os.remove(mypath.replace("\\", "/") + elm)
