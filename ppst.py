from ast import If
import numpy as np

wp_mean=np.zeros((18,18),dtype=np.float64)
wp_sigma=np.zeros((18,18),dtype=np.float64)
# wp_range[i,j]={'low_bound':wp_mean[i,j]-wp_sigma[i,j],'high_bound':wp_mean[i,j]+wp_sigma[i,j]}

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

index_to_check = [
    [1,5,9,10,11,14,15],        #1
    [3,11,13,14,15,17],         #2
    [1,3,5,9,11,13,15,17],      #3
    [1,4,5,6,9,11,13,14,15],    #4
    [1,5,13,14,15],             #5
    [11,13,15],                 #6
    [3,6,9,11,15],              #8
    [3,6,11,15],                #9
    [9,11,17],                  #10
    [9,11,17],                  #11
    [9,11,15,17],               #12
    [9,11,15,17],               #13
    [13,14,15],                 #14
    [13,15],                    #15
    [11,13,14,15,16,17,18,19],  #16
    [15,16,17],                 #17
    [11,15,17],                 #18
    [13,15,16],                 #19  
    [6,15,18],                  #20
]


def wp_static_filter(points,label,wp_range={'low_bound':wp_mean-wp_sigma,'high_bound':wp_mean+wp_sigma},ItC=index_to_check):
    # return possible wrong points and their resigned classes
    wp=np.zeros((points.size()[0],points.size()[1]+1),dtype=np.int32)
    # wp_range[i,j]['low_bound']
    wp[0,0]=-1
    wp_idx=0
    for i in range(points.size()[0]):
        for cl1 in range(len(ItC)):
            wp[wp_idx,0]=i
            for cl2 in ItC[cl1]:
        # j = index_to_check[label[i],0] 
                
                if points[i,cl2+6]>wp_range['low_bound'][cl1,cl2] and points[i,cl2+6]<wp_range['high_bound'][cl1,cl2]:
                    # possible wrong
                    
                    wp[wp_idx,cl1+1]=1
                else:
                # point_i not satisfied all condition, not wrong points, ignore and break the loop
                    # wp[wp_idx,0]=
                    wp[wp_idx,0]=-1
            
                    
                    break
        if wp[wp_idx]==-1:
            wp[wp_idx,:]=0
        else:
            wp_idx+=1

    return wp
