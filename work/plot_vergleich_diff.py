import os
import csv
import math
from geopy.distance import geodesic
import matplotlib.pyplot as plt

data_path = os.path.abspath('/workspaces/gnss-ins-sim/work/demo_saved_data/2023-08-11-13-41-55//')


def read_ref_pos(ref_pos_filename):
    with open(ref_pos_filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        ref_pos_lat = []
        ref_pos_lon = []
        ref_pos_alt = []
    

        for row in csvreader:
            ref_pos_lat.append(float(row[0]))
            ref_pos_lon.append(float(row[1]))
            ref_pos_alt.append(float(row[2]))

        
    return ref_pos_lat, ref_pos_lon, ref_pos_alt

def read_pos(pos_filename):
    with open(pos_filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        pos_lat = []
        pos_lon = []
        pos_alt = []
    

        for row in csvreader:
            pos_lat.append(float(row[0]))
            pos_lon.append(float(row[1]))
            pos_alt.append(float(row[2]))

        
    return pos_lat, pos_lon, pos_alt

def read_ref_vel(ref_vel_filename):
    with open(ref_vel_filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        ref_vx = []
        ref_vy = []
        ref_vz = []
    

        for row in csvreader:
            ref_vx.append(float(row[0]))
            ref_vy.append(float(row[1]))
            ref_vz.append(float(row[2]))

        
    return ref_vx, ref_vy, ref_vz

def read_vel(vel_filename):
    with open(vel_filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        vx = []
        vy = []
        vz = []
    

        for row in csvreader:
            vx.append(float(row[0]))
            vy.append(float(row[1]))
            vz.append(float(row[2]))

        
    return vx, vy, vz

def read_ref_att(ref_att_filename):
    with open(ref_att_filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        ref_yaw = []
        ref_pitch = []
        ref_roll = []
    

        for row in csvreader:
            ref_yaw.append(float(row[0]))
            ref_pitch.append(float(row[1]))
            ref_roll.append(float(row[2]))

        
    return ref_yaw, ref_pitch, ref_roll

def read_att(att_filename):
    with open(att_filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        yaw = []
        pitch = []
        roll = []
    

        for row in csvreader:
            yaw.append(float(row[0]))
            pitch.append(float(row[1]))
            roll.append(float(row[2]))

        
    return yaw, pitch, roll

def read_time(timefilename):
    with open(timefilename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        time = []
        
        for row in csvreader:
            time.append(float(row[0]))

    return time

def haversine_distance(lat1, lon1, lat2, lon2):
    
    R = 6371000  

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance


if __name__ == "__main__":
    timefilename = data_path + "//time.csv"
    ref_pos_filename = data_path + "//ref_pos.csv"
    pos_filename = data_path + "//pos-algo0_0.csv" 
    ref_vel_filename = data_path + "//ref_vel.csv"
    vel_filename = data_path + "//vel-algo0_0.csv"
    ref_att_filename = data_path + "//ref_att_euler.csv"
    att_filename = data_path + "//att_euler-algo0_0.csv"
    
    time = read_time(timefilename)

    ref_pos_lat, ref_pos_lon, ref_pos_alt = read_ref_pos(ref_pos_filename)
    pos_lat, pos_lon, pos_alt = read_pos(pos_filename)

    ref_vx, ref_vy, ref_vz = read_ref_vel(ref_vel_filename)
    vx, vy, vz = read_vel(vel_filename)

    ref_yaw, ref_pitch, ref_roll = read_ref_att(ref_att_filename)
    yaw, pitch, roll = read_att(att_filename)
    diff_pos_m = [haversine_distance(lat1, lon1, lat2, lon2) for lat1, lon1, lat2, lon2 in zip(ref_pos_lat, ref_pos_lon, pos_lat, pos_lon)]

    diff_pos_alt = list()
    for item1, item2 in zip(ref_pos_alt, pos_alt):
        item = item1 - item2
        diff_pos_alt.append(item)
    
    plt.figure()
    plt.plot(time, diff_pos_m, color = 'g', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_pos(m)')
    plt.plot(time, diff_pos_alt, color = 'b', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_pos_alt (m)')
    plt.xlabel('Time(s)')
    plt.ylabel('pos')
    plt.title('pos Vergleich')  
    plt.legend()
    
    diff_vx = list()
    for item1, item2 in zip(ref_vx, vx):
        item = item1 - item2
        diff_vx.append(item)

    diff_vy = list()
    for item1, item2 in zip(ref_vy, vy):
        item = item1 - item2
        diff_vy.append(item)

    diff_vz = list()
    for item1, item2 in zip(ref_vz, vz):
        item = item1 - item2
        diff_vz.append(item)

    plt.figure()
    plt.plot(time, diff_vx, color = 'g', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_vx')
    plt.plot(time, diff_vy, color = 'r', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_vy')
    plt.plot(time, diff_vz, color = 'b', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_vz')
    plt.ylabel('deff_vel (m/s)')
    plt.title('vel Vergleich')  
    plt.legend()

    diff_att_yaw = list()
    for item1, item2 in zip(ref_yaw, yaw):
        item = item1 - item2
        diff_att_yaw.append(item)

    diff_att_pitch = list()
    for item1, item2 in zip(ref_pitch, pitch):
        item = item1 - item2
        diff_att_pitch.append(item)

    diff_att_roll = list()
    for item1, item2 in zip(ref_roll, roll):
        item = item1 - item2
        diff_att_roll.append(item)

    plt.figure()
    plt.plot(time, diff_att_yaw, color = 'g', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_att_yaw')
    plt.plot(time, diff_att_pitch, color = 'r', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_att_pitch')
    plt.plot(time, diff_att_roll, color = 'b', linestyle = 'dashed', marker = '', linewidth= '1', label='diff_att_roll')
    plt.ylabel('deff_att (deg)')
    plt.title('attitude Vergleich')  
    plt.legend()


