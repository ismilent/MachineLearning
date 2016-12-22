from numpy import *
import operator

'''
kNN
'''

def create_dataset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inx, dataset, labels, k):
    # 计算距离
    dataset_size = dataset.shape[0]
    diff_mat = tile(inx, (dataset_size, 1)) - dataset
    sqdiff_mat = diff_mat ** 2
    sq_distances = sqdiff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_dist_indicies = distances.argsort()

    # 选择距离最小的k个点
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_dist_indicies[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1

    # 排序
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return  sorted_class_count[0][0]

group, labels = create_dataset()
print classify0([0,0], group, labels, 3)
