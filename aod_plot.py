import collections
import csv

import matplotlib.pyplot as plt
import numpy as np

aod_data_by_lc = collections.defaultdict(list)
with open("tab3.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        aod_data_by_lc[row["land_cover"]].append(row)


