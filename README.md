# GPS Device Driver for GNSS Puck

This project involves the development of a GPS device driver for a USB-based GNSS puck. The device driver is designed to collect GPS data, parse it, and convert the latitude and longitude to UTM coordinates using the ROS (Robot Operating System) framework. The data collected is then analyzed to understand the accuracy and reliability of GPS navigation.

## Project Overview

This project focuses on the following key components:
1. **Setting up the GNSS Puck**: Configuring the GNSS puck for data collection.
2. **Writing the Device Driver**: Developing a driver to parse $GPGGA formatted messages from the GNSS puck.
3. **Data Collection**: Gathering stationary and moving data using ROS bags.
4. **Data Analysis**: Analyzing the collected data to evaluate GPS accuracy and errors.

## Setting up the GNSS Puck

To set up the GNSS puck for data collection:
1. Connect the GPS device and identify the device file identifier using the terminal command:
   ```sh
   $ ls -lt /dev/tty* | head

**Note the device file identifier** (e.g., `/dev/ttyUSB2`).

2. Set read and write permissions for the device:
   ```sh
   chmod 666 /dev/ttyUSB2

3. Configure the device settings in Minicom and save the GPS data to a text file using the -C flag:
    ```sh
   minicom -C gps-data.txt

**To stop writing to the file, press Ctrl+C.**

## Writing the Device Driver

The GNSS puck provides messages formatted according to the `$GPGGA` format. The device driver will:

1. **Read serial data from the puck.**
2. **Parse the data for latitude, longitude, and altitude.**
3. **Convert the latitude and longitude to UTM coordinates** using the Python package `utm`.
4. **Publish these values in a custom ROS message** with the following fields:
   - `header`
   - `latitude`
   - `longitude`
   - `altitude`
   - `UTM easting`
   - `UTM northing`
   - `zone`
   - `letter`

## Data Collection

1. **Stationary Data Outdoors**
   - Collected 10 minutes of stationary data at one spot using a ROS bag.

2. **Walk in a Straight Line Outdoors**
   - Recorded a new ROS bag while walking in a straight line for a few hundred meters.

## Data Analysis

1. **Stationary Data Analysis**
   - Analyzed the stationary data by plotting its statistics to understand GPS navigation accuracy and error distribution. Evaluated the sources of errors and provided a good error estimate.

2. **Moving Data Analysis**
   - Analyzed the UTM data collected while walking in a straight line. Assessed how the error estimate changes when moving compared to staying in one spot and examine the noise distribution.

## Report

Documented findings in a report with plots and charts, summarizing the analysis of both stationary and moving data.

## Repository Structure

The directory structure for the project is as follows:
-src/
    -Gps-driver/
    -Report.pdf
    -Analysis-scripts/
    -data/
-README.md


## How to Use

1. **Clone the repository:**
   ```sh
   git clone <repository_url>


2. **Navigate to the source directory:**
   ```sh
   cd src

3. **Run the GPS driver:**
   ```sh
   python3 gps_device_driver.py

4. **Analyze the data:**
   Use the scripts provided in the Analysis scripts directory to analyze the collected data.
