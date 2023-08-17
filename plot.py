import csv
import matplotlib.pyplot as plt

def read_defmotion(deffilename):
    with open(deffilename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvfile)
        next(csvfile)
        header = next(csvfile)

        # motion def
        time = [0]
        time_d = []
        velocity_x_def = []
        velocity_y_def = []
        velocity_z_def = []
    

        for row in csvreader:
            time_d.append(float(row[7]))
            velocity_x_def.append(float(row[4]))
            velocity_y_def.append(float(row[5]))
            velocity_z_def.append(float(row[6]))
            
        for i in range(1,len(time_d)):
            time.append(time_d[i] + time[i-1])

        
    return time, velocity_x_def, velocity_y_def, velocity_z_def

def read_groundtruth(gfilename):
    with open(gfilename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvfile)

        velocity_x_g = []
        velocity_y_g = []
        velocity_z_g = []

        for row in csvreader:
            velocity_x_g.append(float(row[8]))
            velocity_y_g.append(float(row[9]))
            velocity_z_g.append(float(row[10]))
        
        velocity_x_g.pop(0)
        velocity_y_g.pop(0)
        velocity_z_g.pop(0)
        velocity_x_g.pop(-1)
        velocity_y_g.pop(-1)
        velocity_z_g.pop(-1)

    return velocity_x_g, velocity_y_g, velocity_z_g


if __name__ == "__main__":
    deffilename = "/workspaces/gnss-ins-sim/test-motion_def/motion_def-2023-08-09-10-33.csv"
    gfilename = "/workspaces/gnss-ins-sim/vergleich.csv" 

    time, velocity_x_def, velocity_y_def, velocity_z_def = read_defmotion(deffilename)
    velocity_x_g, velocity_y_g, velocity_z_g = read_groundtruth(gfilename)

    plt.figure()
    plt.plot(time, velocity_x_def, color = 'g', linestyle = 'dashed', marker = '', linewidth= '1', label='vx_motiondef')
    plt.plot(time, velocity_x_g, color = 'r', linestyle = 'dashed', marker = '', linewidth= '1', label='vx_groundtruth')
    plt.xlabel('Time(s)')
    plt.ylabel('Velocity(m/s)')
    plt.title('Velocity_x Vergleich')  
    plt.legend()
    plt.xlim(62, 75)
    plt.figure()
    plt.plot(time, velocity_y_def, color='g', linestyle='dashed', marker='', linewidth='1', label='vy_motiondef')
    plt.plot(time, velocity_y_g, color='r', linestyle='dashed', marker='', linewidth='1', label='vy_groundtruth')
    plt.xlabel('Time(s)')
    plt.ylabel('Velocity(m/s)')
    plt.title('Velocity_y Vergleich')
    plt.legend()
    plt.xlim(115, 125)
    plt.figure()
    plt.plot(time, velocity_z_def, color='g', linestyle='dashed', marker='', linewidth='1', label='vz_motiondef')
    plt.plot(time, velocity_z_g, color='r', linestyle='dashed', marker='', linewidth='1', label='vz_groundtruth')
    plt.xlabel('Time(s)')
    plt.ylabel('Velocity(m/s)')
    plt.title('Velocity_z Vergleich')
    plt.legend()


