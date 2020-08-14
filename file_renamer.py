import os
import sys
import pickle
import numpy as np
from progress.bar import ShadyBar
import csv

def pickle_files(pkl_path, no_files):

    
    bar = ShadyBar('Pickling Data', max=no_files)
    # retrieving data from multiple files
    for i in range(no_files):
        filename = f"./trial{(i+1):07d}.csv"
        file_list = []
        try:
            with open(filename, "r") as f:
                f_data = csv.reader(f)
                for row in f_data:
                    file_list.append(row)
            
            with open(pkl_path, "ab") as fileobj:
                pickle.dump(file_list, fileobj)
        except :
            pass
        
        bar.next()

   
    bar.finish()


def pickle_seperate(pkl_path, no_files):
    # with pickle.load(open(pkl_path,'rb')) as f:
    with open(pkl_path, 'rb') as f:
        count = 0
        while 1:
            try:
                # print(np.array(pickle.load(f)).astype(float))
                # sys.exit(1)
                # print(len(pickle.load(f)))
                pickle.dump(f"train_data{count:06d}.pkl")
                count +=1
            except EOFError:
                break  # no more data in the file


def normalize_data2(x, max=0, min=0, train=True):
    if train:
        max = np.max(x)
        min = np.min(x)

    normalized = (2*(x-min/(max-min)) - 1)
    return normalized


def normalize_data(x, max=0, min=0, train=True):
    if train:
        max = np.max(x)
        min = np.min(x)

    normalized = (x-min)/(max-min)
    return normalized


def normalize_train():
    pkl_path = "normalized_data.pkl"
    os.system("touch " + pkl_path)
    with open("train_data.pkl", 'rb') as f:
        max = [6.0000000e+02, 1.0000000e+00, 2.2400000e+02, 6.0950000e+02, 9.4987500e+02,
               1.0000000e+00, 1.1130000e+03, 2.2200000e+02, 1.1130000e+03, 2.3550000e+01,
               6.7000000e+01, 7.8813584e+01, 1.9753013e+02, 2.2400000e+02]
        min = [0.00000000e+000, 0.00000000e+000,  0, 0.00000000e+000,
               0.00000000e+000, - 1.00000000e+000,  0.00000000e+000,  0.00000000e+000,
               0.00000000e+000,  0.00000000e+000,  0.00000000e+000,  0.00000000e+000,
               0.00000000e+000,  1]
        
        while 1:
            try:
                file = np.array(pickle.load(f)).astype(float)
                if file.shape[0] == 0: continue
                for i in range(len(max)):
                    file[:, i] = normalize_data(file[:, i], max[i],min[i],False)
                
                with open(pkl_path, "ab") as fileobj:
                    pickle.dump(file, fileobj)
               
            except EOFError:
                break  # no more data in the file
            except:
                print(file)
                pass
     
if __name__ == "__main__":
    # count = 0
    # for filename in os.listdir("./"):
    #     if filename.endswith(".csv"):
    #         count += 1
    #         os.rename(filename, f"trial{count:06d}.csv")
    normalize_train()




