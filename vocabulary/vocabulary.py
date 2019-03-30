from scipy.cluster.vq import *
import sift.sift as sift
import numpy as np
import pickle

class Vocabulary(object):
    def __init__(self, name):
        self.name=name
        self.voc=[]
        self.idf=[]
        self.trainingdata=[]
        self.nbr_words=0

    def train(self,featurefiles,k=100,subsampling=10):
        nbr_images=len(featurefiles)
        descr=[]
        descr.append(sift.read_features_from_file(featurefiles[0])[1])
        descriptors=descr[0]
        for i in np.arange(1,nbr_images):
            descr.append(sift.read_features_from_file(featurefiles[i])[1])
            descriptors=np.vstack((descriptors,descr[i]))

        self.voc,distortion=kmeans(descriptors[::subsampling,:],k,1)
        self.nbr_words=self.voc.shape[0]

        imwords=np.zeros((nbr_images,self.nbr_words))
        for i in range(nbr_images):
            imwords[i]=self.project(descr[i])

        nbr_occurences=np.sum((imwords>0)*1,axis=0)
        self.idf=np.log((1.0*nbr_images)/(1.0*nbr_occurences))
        self.trainingdata=featurefiles

    def project(self,descriptors):
        imhist=np.zeros((self.nbr_words))
        words,distance=vq(descriptors,self.voc)
        for w in words:
            imhist[w] += 1
        return imhist

# input: array of .sift path
def create_v(imlist:[]):
    nbr_images = len(imlist)
    featlist =[imlist[i][:-3]+'sift' for i in range(nbr_images)]
    voc=Vocabulary('ukbenchtest')
    voc.train(featlist,1000,10)

    with open('vocabulary.pkl','wb') as f:
        pickle.dump(voc,f)
