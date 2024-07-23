import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
b = bagreader('/home/arvinder/RSN/src/rosbag_data/moving_data.bag')

gpsdata= b.message_by_topic(topic="/gps_data_print")


gpsdataread = pd.read_csv(gpsdata)
gpsdf = pd.DataFrame(gpsdataread, columns=["Time", "latitude.data", "longitude.data", "altitude.data", "easting.data", "northing.data"]).astype(float)

gpsdf["Time"] = (gpsdf["Time"] - gpsdf.at[0,"Time"])/60


plotgps = gpsdf.plot.scatter("Time","altitude.data", label= "Altitude at time t")
plt.legend(loc="upper left")
plt.xlabel("Time(min)")
plt.ylabel("Altitude(m)")
plt.grid(True)
plt.title("Time vs Altitude (Moving)")
plt.show()
