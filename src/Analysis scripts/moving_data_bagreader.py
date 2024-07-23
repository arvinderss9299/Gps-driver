import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

b = bagreader('/home/arvinder/RSN/src/rosbag_data/moving_data.bag')

gpsdata= b.message_by_topic(topic="/gps_data_print")


gpsdataread = pd.read_csv(gpsdata)
gpsdf = pd.DataFrame(gpsdataread, columns=["Time", "latitude.data", "longitude.data", "altitude.data", "easting.data", "northing.data"]).astype(float)

X  = gpsdf["easting.data"].values.reshape(-1, 1)
Y = gpsdf["northing.data"].values.reshape(-1, 1)

linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)  
Y_pred = linear_regressor.predict(X)
print("Coefficient of determination: %.2f" % r2_score(Y, Y_pred))

gpsdf["Distance"] = abs(Y - Y_pred)
print("Maximum Distance(error) from best fit line:", gpsdf["Distance"].max())
plt.title("UTM Easting vs UTM Northing (Moving)")
plot_gps = plt.scatter(X, Y, label= "UTM(X,Y)")
plt.plot(X, Y_pred, color = "r", label= "Regression Line")
plt.legend(loc="upper right")
plt.xlabel("UTM Easting(m)")
plt.ylabel("UTM Northing(m)")
plt.grid(True)
plt.show()

# loop through points
# p-distance between line and datapoint
# sort decreasing order
# pick the first value


# print("Coefficients: \n", linear_regressor.coef_)
# print("Mean squared error: %.2f" % mean_squared_error(Y, Y_pred))
# # The coefficient of determination: 1 is perfect prediction







# gpsdf["Time"] = (gpsdf["Time"] - gpsdf.at[0,"Time"])/60
# point_x = [gpsdf.at[0,"easting.data"],gpsdf["easting.data"].iloc[-1] ]
# point_y = [gpsdf.at[0,"northing.data"], gpsdf["northing.data"].iloc[-1] ]

# plotgps = gpsdf.plot.scatter("Time", "altitude.data")
# plt.plot(point_x,point_y, color="r")
# plt.title("Easting vs Northing (Moving)")
# plt.show()



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
#  "altitude.data", "latitude.data", "longitude.data"
