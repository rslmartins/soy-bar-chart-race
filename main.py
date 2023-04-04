import pandas as pd
import bar_chart_race as bcr

# Load data from Our World in Data
"https://ourworldindata.org/soy"
df = pd.read_csv("soybean-production.csv")

# Change the columns' name
df.columns = ["Entity", 'Code', 'Year', "Tonnes"]

# Transform the dataframe 
df_pivoted = df.pivot(index="Year", columns="Entity", values="Tonnes")

# Regions to be deleted that do not represent a country
cols_to_drop = ["Africa","Africa (FAO)","Americas (FAO)","Asia","Asia (FAO)","Central America (FAO)","Central Asia (FAO)","China","Eastern Africa (FAO)","Eastern Asia (FAO)","Eastern Europe (FAO)","Europe","Europe (FAO)","European Union (27)","European Union (27) (FAO)", "High-income countries", "Land Locked Developing Countries (FAO)","Least Developed Countries (FAO)","Low Income Food Deficit Countries (FAO)","Low-income countries","Lower-middle-income countries","Middle Africa (FAO)","Net Food Importing Developing Countries (FAO)","Northern Africa (FAO)","Northern America (FAO)","Northern Europe (FAO)","Small Island Developing States (FAO)","North America","South America","South America (FAO)","South-eastern Asia (FAO)","Southern Africa (FAO)","Southern Asia (FAO)","Southern Europe (FAO)","Upper-middle-income countries", "Oceania", "Oceania (FAO)","Western Africa (FAO)","Western Asia (FAO)","Western Europe (FAO)","World"]

df_pivoted.drop(cols_to_drop, axis=1, inplace=True)

# Create video
bcr.bar_chart_race(
        df=df_pivoted, 
        filename='soy.mp4',
        fixed_max=True,
        fixed_order=False,
        n_bars=10,
        steps_per_period=10,
        period_length=750,
         orientation='v',
        title="Soybean production by country (1960 to 2020)")
