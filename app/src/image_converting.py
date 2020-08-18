import numpy as np
import cv2

def Kmeans(img, clusterN):
    z=img.reshape((-1,3))
    z=np.float32(z)

    #criteriaの定義とクラスタ数、k-meansの実行
    criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    ret, label, center=cv2.kmeans(z,clusterN,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    center=np.uint8(center)
    res=center[label.flatten()]
    res2=res.reshape((img.shape))

    #各色のピクセル数を数える
    each_color=[]
    total=label.size
    color_label=[]
    for i in range(clusterN):
        if i!=clusterN-1:
            num=np.count_nonzero(label==i)
            per=int(round(1000*num/total))
            each_color.append(per)
            color_label+=[i]*(per*800)
        else:
            per=1000-np.sum(each_color)
            each_color.append(per)
            color_label+=[i]*(per*800)

    res_s=center[color_label]
    res_s2=res_s.reshape(((1000,800,3)))



    return ret, res2, res_s2