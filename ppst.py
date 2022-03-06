
from random import randint, uniform
from utils import *
import numpy as np

# wp_mean=np.zeros((20,20),dtype=np.float64)
# wp_sigma=np.zeros((20,20),dtype=np.float64)



def wp_static_filter(points,wp_range,ItC):
    # points=np.array((number_of_points,20),dtype=float64)
    # wp_range={'low_bound':wp_mean-wp_sigma,'high_bound':wp_mean+wp_sigma}
    # ItC=index_to_check
    # return: possible wrong points and their resigned classes

    wp=np.zeros((points.shape[0],21),dtype=np.int32)
    # wp[0,0]=-1
    wp_idx=0
    for i in range(points.shape[0]):
        wp[wp_idx,0]=i
        for cl1 in range(len(ItC)):
            wp[wp_idx,cl1+1]=1 # assume all conditions are satisfied, resign class
            for cl2 in ItC[cl1]:
        # j = index_to_check[label[i],0] 
                
                    
                if points[i,cl2]<wp_range['low_bound'][cl1,cl2] or points[i,cl2]>wp_range['high_bound'][cl1,cl2]:
                # point_i not satisfied all condition, not wrong points, ignore and break the loop
                    wp[wp_idx,cl1+1]=0
                    # wp[wp_idx,0]=-1 
                    break
        if np.sum(wp[wp_idx,1:])==0:
            wp[wp_idx,:]=0
        else:
            wp_idx+=1

    return wp


if __name__=='__main__':
    wp_m=np.zeros((20,20),dtype=np.float64)
    wp_s=np.zeros((20,20),dtype=np.float64)

    # index_to_check = {
    #     '1':[1,5,9,10,11,14,15],
    #     '2':[3,11,13,14,15,17],
    #     '3':[1,3,5,9,11,13,15,17],
    #     '4':[1,4,5,6,9,11,13,14,15],
    #     '5':[1,5,13,14,15],
    #     '6':[11,13,15],
    #     '7':[3,6,9,11,15],
    #     '8':[3,6,11,15],
    #     '9':[9,11,17],
    #     '10':[9,11,17],
    #     '11':[9,11,15,17],
    #     '12':[9,11,15,17],
    #     '13':[13,14,15],
    #     '14':[13,15],
    #     '15':[11,13,14,15,16,17,18,19],
    #     '16':[15,16,17],
    #     '17':[11,15,17],
    #     '18':[13,15,16] 
    #     '19':[6,15,18],  
    # }

    ### ignore #0 and #7
    itc = [
    [0],                        #0
    [1,5,9,10,11,14,15],        #1
    [3,11,13,14,15,17],         #2
    [1,3,5,9,11,13,15,17],      #3
    [1,4,5,6,9,11,13,14,15],    #4
    [1,5,13,14,15],             #5
    [11,13,15],                 #6
    # [3,6,9,11,15],              #7
    [7],                        #7
    [3,6,11,15],                #8
    [9,11,17],                  #9
    [9,11,17],                  #10
    [9,11,15,17],               #11
    [9,11,15,17],               #12
    [13,14,15],                 #13
    [13,15],                    #14
    [11,13,14,15,16,17,18,19],  #15
    [15,16,17],                 #16
    [11,15,17],                 #17
    [13,15,16],                 #18  
    [6,15,18]                   #19
]
    
    ### random init
    for i in range(20):
        for j in range(20):
            wp_m[i,j]=uniform(0.3,0.7)
            wp_s[i,j]=uniform(0,0.3)
            if j==0 or j==7:    ### ignore #0 and #7
                wp_m[i,j]=wp_s[i,j]=0
    wp_m=soft_max(wp_m) # do the softmax to make the data right
    n=200
    pts=np.random.uniform(0,1,(n,20)) # points is n*20 dtype=float64
    for i in range(pts.shape[0]):
        pts[i,randint(0,19)]=uniform(1,4)
    pts=soft_max(pts) # do the softmax to make the data right

    wp_static_filter(pts,{'low_bound':wp_m-wp_s,'high_bound':wp_m+wp_s},itc)