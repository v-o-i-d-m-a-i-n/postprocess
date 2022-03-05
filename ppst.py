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
    [3,6,9,11,15],              #7
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
    [6,15,18],                  #19
]


def wp_static_filter(points,label,wp_range={'low_bound':wp_mean-wp_sigma,'high_bound':wp_mean+wp_sigma},index_to_check=index_to_check):
    # return possible wrong points and their resigned classes
    wp_range[i,j]['low_bound']
    for i in range(points.size()[0]):
        # for
        j = index_to_check[label[i],0] 
        if points[i,j+6]<wp_range[i,j]['low_bound'] or points[i,j+6]>wp_range[i,j]['high_bound']:
            # not satisfied all condition, possible wrong points, resign class and break the loop
            break
    return
