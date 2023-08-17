import csv
import math
from squaternion import Quaternion
from datetime import datetime

def quaternion_to_euler(qw, qx, qy, qz):
    q = Quaternion(qw, qx, qy, qz)
    e = q.to_euler(degrees=True)

    return e

def read_quaternions(filename):

    quaternions = []
    
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)       

        s_colums = ["q_RS_w []", "q_RS_x []", "q_RS_y []", "q_RS_z []"]
        s_indices = [header.index(column) for column in s_colums]

        for row in csvreader:
            s_row = [float(row[i]) for i in s_indices]
            quaternions.append(tuple(s_row))

    return quaternions

def read_time(filename):
    timestamps = []
    time_changes = []
    
   
    with open (filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)

        t_colum = "#timestamp [ns]"
        if header.index(t_colum) == 1:
            t_indix = header.index(t_colum)
            
            for row in csvreader:
                timestamps.append(row[t_indix])

            for i in range(1, len(timestamps)):
                diff = (float(timestamps[i]) - float(timestamps[i-1]))*1e-9 
                time_changes.append(diff)
        else:
            for row in csvreader:
                timestamps.append(row[0])

            for i in range(1, len(timestamps)):
                diff = 4999936*1e-9
                time_changes.append(diff)
        
    return time_changes

    

def read_position(filename): 

    x_positions = []
    y_positions = []
    z_positions = []

    with open (filename, 'r', newline='') as csvfile:

        csvreader = csv.reader(csvfile)
        header = next(csvreader)       
        
        # x-yostion
        x_colum = "p_RS_R_x [m]"
        y_colum = "p_RS_R_y [m]"
        z_colum = "p_RS_R_z [m]"
        
        x_index = header.index(x_colum)
        y_index = header.index(y_colum)
        z_index = header.index(z_colum)

        for row in csvreader:
            x_positions.append(float(row[x_index]))
            y_positions.append(float(row[y_index]))
            z_positions.append(float(row[z_index]))

    return x_positions, y_positions, z_positions



def calc_velocity(filename):
    x_velocity = []
    y_velocity = []
    z_velocity = []

    x_velocity_l = []
    y_velocity_l = []
    z_velocity_l = []

    time = read_time(filename)
    x_positions, y_positions, z_positions = read_position(filename)

    for i in range(1,len(time)+1):
        x_velocity = (float(x_positions[i])-float(x_positions[i-1]))/float(time[i-1])
        x_velocity_l.append(x_velocity)
        y_velocity = (float(y_positions[i])-float(y_positions[i-1]))/float(time[i-1])
        y_velocity_l.append(y_velocity)
        z_velocity = (float(z_positions[i])-float(z_positions[i-1]))/float(time[i-1])
        z_velocity_l.append(z_velocity)

    return x_velocity_l, y_velocity_l, z_velocity_l

if __name__ == "__main__":
    filename = "/workspaces/gnss-ins-sim/vicon0_data.csv"
    
    # position
    x_positions, y_positions, z_positions = read_position(filename)

    # attitude
    quaternions = read_quaternions(filename)
    roll_l = []
    pitch_l = []
    yaw_l = []
    """
    for qw, qx, qy, qz in quaternions:
        roll, pitch, yaw = quaternion_to_euler(qw, qx, qy, qz)
        roll_l.append(roll)
        pitch_l.append(pitch)
        yaw_l.append(yaw)
    """
    for qw, qx, qy, qz in quaternions:
        e = quaternion_to_euler(qw, qx, qy, qz)
        roll_l.append(e[0])
        pitch_l.append(e[1])
        yaw_l.append(e[2])

     
    # time
    time = read_time(filename)
    time = [x * 1 for x in time]
    

    # command_type
    command_type = [2] * (len(time) -1)
    #command_type = [1, 5, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 5]


    # GPS-visibility
    gps_visibility = [0] * (len(time) -1)
    #gps_visibility = [1] * 18
    # int Pos
    ini_lat = 0
    ini_long = 0
    ini_alt = 0

    # velocity
    x_velocity, y_velocity, z_velocity = calc_velocity(filename)
    
    """
    # test
    ini_lat = 32
    ini_long = 120
    ini_alt = 0
    x_velocity = [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_velocity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_velocity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    yaw_l = [0, 0, 0, 0, 90, 0, 180, 0, -180, 0, 180, 0, -180, 0, 180, 0, -180, 0, 0]
    pitch_l = [0, 0, 45, 0, -45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    roll_l = [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    # csv
    new_filename = datetime.now().strftime('/workspaces/gnss-ins-sim/test-motion_def/motion_def-%Y-%m-%d-%H-%M.csv')
    header1 = ['ini lat (deg)', 'ini lon (deg)', 'ini alt (m)', 'ini vx_body (m/s)', 'ini vy_body (m/s)', 'ini vz_body (m/s)', 'ini yaw (deg)', 'ini pitch (deg)', 'ini roll (deg)']
    header2 = ['command type', 'yaw (deg)', 'pitch (deg)', 'roll (deg)', 'vx_body (m/s)', 'vy_body (m/s)', 'vz_body (m/s)', 'command duration (s)', 'GPS visibility']
    init = [ini_lat, ini_long, ini_alt, x_velocity[0], y_velocity[0], z_velocity[0], yaw_l[0], pitch_l[0], roll_l[0]]

    yaw_l.pop(0)
    pitch_l.pop(0)
    roll_l.pop(0)
    yaw_l.pop(-1)
    pitch_l.pop(-1)
    roll_l.pop(-1)
    #time = [200, 250, 10, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 10]
    
    x_velocity.pop(0)
    y_velocity.pop(0)
    z_velocity.pop(0)

    time.pop(0)

    with open(new_filename, 'w+', encoding='UTF8', newline='', ) as newcsv:
        writer = csv.writer(newcsv)

        writer.writerow(header1)
        writer.writerow(init)
        writer.writerow(header2)
        for i in zip(command_type, yaw_l, pitch_l, roll_l, x_velocity, y_velocity, z_velocity, time, gps_visibility):
             writer.writerow(i)

    print(len(command_type))
    print(len(yaw_l))
    print(len(pitch_l))
    print(len(roll_l))
    print(len(x_velocity))
    print(len(y_velocity))
    print(len(z_velocity))
    print(len(time))
    print(len(gps_visibility))

   
