import sift.sift

imlist=[]
nbr_images=len(imlist)
featlist=[imlist[i][:-3]+'sift' for i in range(nbr_images)]

for i in range(nbr_images):
    sift.sift.process_image(imlist[i],featlist[i])

