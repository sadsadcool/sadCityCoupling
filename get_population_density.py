#!/usr/bin/env python
# encoding: utf-8

import csv
import time
import numpy as np

# Tokyo
lat_min_t = 35.5
lat_max_t = 35.796
lon_min_t = 139.4
lon_max_t = 139.9
# Osaka
lat_min_o = 34.45
lat_max_o = 34.85
lon_min_o = 135.3
lon_max_o = 135.7
# Fukuoka
lat_min_f = 33.48
lat_max_f = 33.76
lon_min_f = 130.25
lon_max_f = 130.7
# Nagoya
lat_min_n = 35.00
lat_max_n = 35.32
lon_min_n = 136.7
lon_max_n = 137.1

num_time = 72
num_days = 61
dt = 24 * 3600 / num_time

def get_loc_idx(lat, lon, lat_min, lon_min, lat_max, lon_max, num_dislat):
    dis_lat = int((lat - lat_min) / 0.008)
    dis_lon = int((lon - lon_min) / 0.010)

    return dis_lat + dis_lon * num_dislat


# lat_min = lat_min_n
# lon_min = lon_min_n
# lat_max = lat_max_n
# lon_max = lon_max_n
# num_dislat = int((lat_max - lat_min + 1e-6) / 0.008)
# num_dislon = int((lon_max - lon_min + 1e-6) / 0.010)

# population_density = np.zeros([num_dislat * num_dislon, num_time * num_days])
# init_time = time.mktime(time.strptime('2012-05-31 23:50:00','%Y-%m-%d %H:%M:%S'))

# for m in xrange(6, 8):
    # for d in xrange(1, 32):
        # if m == 6 and d == 31:
            # continue
        # with open('/media/fan/HDPC-UT/ZDC/TrainingForMapping/nagano/sorted/2012{:02d}{:02d}.csv'.format(m, d), 'r') as f:
            # for uid_str, lat_str, lon_str, time_str in csv.reader(f):
                # uid = int(uid_str)
                # lat = float(lat_str)
                # lon = float(lon_str)
                # lid = get_loc_idx(lat, lon, lat_min, lon_min, lat_max, lon_max, num_dislat)
                # tstamp = time.mktime(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
                # tid = int((tstamp - init_time) / dt)
                # if tid >= num_time * num_days or tid < 0:
                    # print time_str
                    # continue
                # population_density[lid, tid] += 1.0

# np.savetxt('node_nagano.csv', population_density, delimiter=',')

# lat_min = lat_min_f
# lon_min = lon_min_f
# lat_max = lat_max_f
# lon_max = lon_max_f
# num_dislat = int((lat_max - lat_min + 1e-6) / 0.008)
# num_dislon = int((lon_max - lon_min + 1e-6) / 0.010)

# population_density = np.zeros([num_dislat * num_dislon, num_time * num_days])
# init_time = time.mktime(time.strptime('2012-05-31 23:50:00','%Y-%m-%d %H:%M:%S'))

# for m in xrange(6, 8):
    # for d in xrange(1, 32):
        # if m == 6 and d == 31:
            # continue
        # with open('/media/fan/HDPC-UT/ZDC/TrainingForMapping/fukuoka/sorted/2012{:02d}{:02d}.csv'.format(m, d), 'r') as f:
            # for uid_str, lat_str, lon_str, time_str in csv.reader(f):
                # uid = int(uid_str)
                # lat = float(lat_str)
                # lon = float(lon_str)
                # lid = get_loc_idx(lat, lon, lat_min, lon_min, lat_max, lon_max, num_dislat)
                # tstamp = time.mktime(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
                # tid = int((tstamp - init_time) / dt)
                # if tid >= num_time * num_days or tid < 0:
                    # print time_str
                    # continue
                # population_density[lid, tid] += 1.0

# np.savetxt('node_fukuoka.csv', population_density, delimiter=',')

lat_min = lat_min_t
lon_min = lon_min_t
lat_max = lat_max_t
lon_max = lon_max_t
num_dislat = int((lat_max - lat_min + 1e-6) / 0.008)
num_dislon = int((lon_max - lon_min + 1e-6) / 0.010)

population_density = np.zeros([num_dislat * num_dislon, num_time * num_days])
init_time = time.mktime(time.strptime('2012-05-31 23:50:00','%Y-%m-%d %H:%M:%S'))

for m in xrange(6, 8):
    for d in xrange(1, 32):
        if m == 6 and d == 31:
            continue
        with open('/media/fan/HDPC-UT/ZDC/TrainingForMapping/tokyo/sorted/2012{:02d}{:02d}.csv'.format(m, d), 'r') as f:
            for uid_str, lat_str, lon_str, time_str in csv.reader(f):
                uid = int(uid_str)
                lat = float(lat_str)
                lon = float(lon_str)
                if lat < lat_min or lat >= lat_max or lon < lon_min or lon >= lon_max:
                    continue
                lid = get_loc_idx(lat, lon, lat_min, lon_min, lat_max, lon_max, num_dislat)
                tstamp = time.mktime(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
                tid = int((tstamp - init_time) / dt)
                if tid >= num_time * num_days or tid < 0:
                    print time_str
                    continue
                population_density[lid, tid] += 1.0

np.savetxt('node_tokyo.csv', population_density, delimiter=',')

# lat_min = lat_min_o
# lon_min = lon_min_o
# lat_max = lat_max_o
# lon_max = lon_max_o
# num_dislat = int((lat_max - lat_min + 1e-6) / 0.008)
# num_dislon = int((lon_max - lon_min + 1e-6) / 0.010)

# population_density = np.zeros([num_dislat * num_dislon, num_time * num_days])
# init_time = time.mktime(time.strptime('2012-05-31 23:50:00','%Y-%m-%d %H:%M:%S'))

# for m in xrange(6, 8):
    # for d in xrange(1, 32):
        # if m == 6 and d == 31:
            # continue
        # with open('/media/fan/HDPC-UT/ZDC/TrainingForMapping/osaka/sorted/2012{:02d}{:02d}.csv'.format(m, d), 'r') as f:
            # for uid_str, time_str, lat_str, lon_str in csv.reader(f):
                # uid = int(uid_str)
                # lat = float(lat_str)
                # lon = float(lon_str)
                # if lat < lat_min or lat >= lat_max or lon < lon_min or lon >= lon_max:
                    # continue
                # lid = get_loc_idx(lat, lon, lat_min, lon_min, lat_max, lon_max, num_dislat)
                # tstamp = time.mktime(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
                # tid = int((tstamp - init_time) / dt)
                # if tid >= num_time * num_days or tid < 0:
                    # print time_str
                    # continue
                # population_density[lid, tid] += 1.0

# np.savetxt('node_osaka.csv', population_density, delimiter=',')
