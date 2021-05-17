import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy

def calculate_transmissivity_values(aod_data):
    '''
    returns two lists:
        - the first is a list of mean values for each entry in aod_data
        - the second is a list of pairs (min, max) representing the error range for each entry
    '''

    means = numpy.exp([-d["AOD550_mean"] for d in aod_data])
    return (
        means,
        (
            means - numpy.exp([-(d["AOD550_mean"] + d["AOD550_std"]) for d in aod_data]),
            numpy.exp([-(d["AOD550_mean"] - d["AOD550_std"]) for d in aod_data]) - means
        )
    )

lc_colors = {
    "Forest": "green",
    "Shrubland/Barren": "grey",
    "Savanna/Grassland": "gold",
    "Cropland": "firebrick",
    "Urban": "black",
}

lc_names = {
    "Forest": "Regiões de Floresta",
    "Shrubland/Barren": "Arbustivo",
    "Savanna/Grassland": "Savana",
    "Cropland": "Regiões Agrícolas",
    "Urban": "Regiões Urbanas",
}

aod_data = []
with open("tab3.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row["land_cover"] in lc_colors:
            aod_data.append({
                key: float(value)
                    if key in ["major_lc_percentage", "AOD550_mean", "AOD550_std"]
                    else value
                for key, value in row.items()
            })

# values = [row["AOD550_mean"] for row in aod_data]
# errors = [row["AOD550_std"] for row in aod_data]
values, errors = calculate_transmissivity_values(aod_data)
plt.errorbar(
    [row["AERONET_site"] for row in aod_data],
    values,
    errors,
    fmt="_k",
    ecolor=[lc_colors[row["land_cover"]] for row in aod_data],
    lw=3,
)

# plt.ylabel("Profundidade Óptica")
plt.ylabel("Transmitância")
plt.xlabel("Estação AERONET")
plt.xticks(rotation=45, ha="right")

legend_handles = [
    mpatches.Patch(color=value, label=lc_names[key])
    for key, value in lc_colors.items()
]
plt.legend(handles=legend_handles, bbox_to_anchor=(1, 1), loc="upper left")

plt.show()
