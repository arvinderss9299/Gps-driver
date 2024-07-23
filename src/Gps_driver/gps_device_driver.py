#!/usr/bin/env python3
import rospy
import serial
import utm
from Gps_driver.msg import gps_custom_message


if __name__ == '__main__':
    serial_port = rospy.get_param('~port','/dev/ttyUSB0')
    serial_baudrate = rospy.get_param('~baudrate',4800)
    gps = serial.Serial(serial_port, serial_baudrate, timeout=None)
    pub=rospy.Publisher('gps_data_print', gps_custom_message, queue_size=10)
    rospy.init_node('gps_node', anonymous=True)


    try:
        while not rospy.is_shutdown():
            line = gps.readline()
            message_type = line[0:6]
            if line == '':
                rospy.logwarn("GPS: No data")
            else:
                if message_type == b'$GPGGA':
                    try:
                        parts = line.decode().split(",")
                        
                        lati = parts[2]
                        lati_dir = parts[3]
                        DDlati = int(float(lati)/100)
                        MMlati = float(lati) - (DDlati * 100)  
                        if lati_dir == 'S':
                            latidec= -(DDlati+(MMlati/60))
                        else:
                            latidec= DDlati+(MMlati/60)
                        
                        longi = parts[4]
                        longi_dir = parts[5]
                        DDlongi = int(float(longi)/100)
                        MMlongi = float(longi) - (DDlongi * 100)
                        if longi_dir == 'W':
                            longidec= -(DDlongi+(MMlongi/60))
                        else:
                            longidec= DDlongi+(MMlongi/60) 
                        
                        alti = float(parts[9])
                        
                        utm_list = utm.from_latlon(latidec,longidec)
                        eastin = utm_list[0]
                        northin = utm_list[1]
                        zone_numbe = utm_list[2]
                        zone_lettr = utm_list[3]
                        
                        message = gps_custom_message()
                        message.header.frame_id = "GPS_Data"
                        message.header.stamp = rospy.Time.now()
                        message.latitude.data = latidec
                        message.longitude.data = longidec
                        message.altitude.data = alti
                        message.easting.data = eastin
                        message.northing.data = northin
                        message.zone_number.data = zone_numbe
                        message.zone_letter.data = zone_lettr
                        
                        
                        rospy.loginfo(message)
                        pub.publish(message)
                       

                    except:
                        rospy.logwarn(b"Data exception: "+line)
                        continue
    except  rospy.ROSInterruptException:
            gps.close()

