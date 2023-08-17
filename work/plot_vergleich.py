import os
import csv
from gnss_ins_sim.sim import sim_data_plot as sim
import matplotlib.pyplot as plt

data_path = os.path.abspath('/workspaces/gnss-ins-sim/work/demo_saved_data/2023-08-11-09-41-50//')


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


    
    plt.figure()
    plt.plot(time, ref_pos_lat, color = 'g', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_pos_lat')
    plt.plot(time, ref_pos_lon, color = 'r', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_pos_lon')
    plt.plot(time, ref_pos_alt, color = 'b', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_pos_alt')
    plt.plot(time, pos_lat, color = 'm', linestyle = 'dashed', marker = '', linewidth= '1', label='pos_lat')
    plt.plot(time, pos_lon, color = 'y', linestyle = 'dashed', marker = '', linewidth= '1', label='pos_lon')
    plt.plot(time, pos_alt, color = 'k', linestyle = 'dashed', marker = '', linewidth= '1', label='pos_alt')
    plt.xlabel('Time(s)')
    plt.ylabel('pos')
    plt.title('pos Vergleich')  
    plt.legend()
    plt.xlim(180)
    
    plt.figure()
    plt.plot(time, ref_vx, color = 'g', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_vx')
    plt.plot(time, ref_vy, color = 'r', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_vy')
    plt.plot(time, ref_vz, color = 'b', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_vz')
    plt.plot(time, vx, color = 'm', linestyle = 'dashed', marker = '', linewidth= '1', label='vx')
    plt.plot(time, vy, color = 'y', linestyle = 'dashed', marker = '', linewidth= '1', label='vy')
    plt.plot(time, vz, color = 'k', linestyle = 'dashed', marker = '', linewidth= '1', label='vz')
    plt.xlabel('Time(s)')
    plt.ylabel('vel')
    plt.title('vel Vergleich')  
    plt.legend()
    plt.xlim(180)

    plt.figure()
    plt.plot(time, ref_yaw, color = 'g', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_yaw')
    plt.plot(time, ref_pitch, color = 'r', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_pitch')
    plt.plot(time, ref_roll, color = 'b', linestyle = 'dashed', marker = '', linewidth= '1', label='ref_roll')
    plt.plot(time, yaw, color = 'm', linestyle = 'dashed', marker = '', linewidth= '1', label='yaw')
    plt.plot(time, pitch, color = 'y', linestyle = 'dashed', marker = '', linewidth= '1', label='pitch')
    plt.plot(time, roll, color = 'k', linestyle = 'dashed', marker = '', linewidth= '1', label='roll')
    plt.xlabel('Time(s)')
    plt.ylabel('att [deg]')
    plt.title('att Vergleich')  
    plt.legend()
    plt.xlim(180, 700)

