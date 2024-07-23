import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
b = bagreader('/home/arvinder/RSN/src/rosbag_data/stationary_data.bag')

gpsdata= b.message_by_topic(topic="/gps_data_print")


gpsdataread = pd.read_csv(gpsdata)
gpsdf = pd.DataFrame(gpsdataread, columns=["Time", "latitude.data", "longitude.data", "altitude.data", "easting.data", "northing.data"]).astype(float)

gpsdf["Time"] = (gpsdf["Time"] - gpsdf.at[0,"Time"])/60


plotgps = gpsdf.plot.scatter("easting.data","northing.data", label= "UTM(X,Y)")
plotgps.set(xlim=(3.278e5 - 4, 3.278e5+10), ylim = (4.68933e6-2, 4.68933e6+10))

plt.legend(loc="upper left")
plt.xlabel("UTM Easting(m)")
plt.ylabel("UTM Northing(m)")
plt.grid(True)
plt.title("Easting vs Northing (Stationary)")
plt.show()

# easting_mean = gpsdf["easting.data"].mean()
# northing_mean = gpsdf["northing.data"].mean()
# plt.plot(easting_mean,northing_mean,label= "UTM(Average X,Average Y)", marker="o", markersize=10,  markerfacecolor="red")
# alt_mean = gpsdf["altitude.data"].mean()
# lat_mean = gpsdf["latitude.data"].mean()
# lon_mean = gpsdf["longitude.data"].mean()
# easting_mean = gpsdf["easting.data"].mean()
# northing_mean = gpsdf["northing.data"].mean()

# gpsdf["easting.data"] -= easting_mean
# gpsdf["northing.data"] -= northing_mean
# gpsdf["altitude.data"]-= alt_mean
# gpsdf["latitude.data"]-= lat_mean
# gpsdf["longitude.data"]-= lon_mean
# plt.scatter(gpsdf["easting.data"].mean(), gpsdf["northing.data"].mean(), color="red")
#  "altitude.data", "latitude.data", "longitude.data"
