def cel_to_feh(temp):
    return temp * 1.8 + 32


def feh_to_cel(temp):
    return "%.2f" % (temp - 32 / 1.8)