import numpy as np
import os
import glob
from matplotlib import pyplot as plt

labels = np.arange(1, 20)


def soft_max(x):
    max_values = np.max(x, axis=1, keepdims=True)
    x = x - max_values
    return np.exp(x) / (np.sum(np.exp(x), axis=1, keepdims=True))


def load_by_numpy(file_, d_type=np.float32):
    data_ = np.fromfile(file_, dtype=d_type)
    return data_


def load_label(file_) -> np.ndarray:
    labels = np.fromfile(file_, dtype=np.int32)
    labels = labels & 0xFFFF
    return labels


def collect_files(path_, ext_):
    return sorted(glob.glob(os.path.join(path_, "*" + ext_)))


def map_by_yaml(data_, map_):
    if not isinstance(data_, list):
        data_ = list(data_.flatten())
    data_mapped = map(lambda x: map_[x], data_)
    return list(data_mapped)


def filter_out(labels: np.ndarray, class_):
    if not isinstance(labels, np.ndarray):
        labels = np.array(labels)
    nonzero_mask = np.array(labels) != class_
    labels_sans_zero = labels[nonzero_mask]
    return labels_sans_zero, nonzero_mask.flatten()


def filter_in(labels, class_):
    if not isinstance(labels, np.ndarray):
        labels = np.array(labels)
    nonzero_mask = np.array(labels) == class_
    labels_sans_zero = labels[nonzero_mask]
    return labels_sans_zero, nonzero_mask.flatten()


def find_diff(gt: np.ndarray, labels: np.ndarray):
    if not isinstance(gt, np.ndarray):
        gt = np.array(gt)
    if not isinstance(labels, np.ndarray):
        labels = np.array(labels)
    diff_mask = np.where(gt != labels)[0]
    return gt[diff_mask], diff_mask.flatten()


def find_same(gt: np.ndarray, labels: np.ndarray):
    if not isinstance(gt, np.ndarray):
        gt = np.array(gt)
    if not isinstance(labels, np.ndarray):
        labels = np.array(labels)
    diff_mask = np.where(gt == labels)[0]
    return gt[diff_mask], diff_mask.flatten()

def per_class_iu(hist):
    iou = np.diag(hist) / (hist.sum(1) + hist.sum(0) - np.diag(hist))
    recall = np.diag(hist) / (hist.sum(1))
    precision = np.diag(hist) / (hist.sum(0))
    return iou, precision, recall

def plot_mean(mean_data, label):
    plt.figure()
    plt.plot(labels, mean_data)
    for label_, value_ in zip(labels, mean_data):
        plt.annotate("{}".format(label_),
                     (label_, value_),
                     textcoords="offset points",
                     xytext=(0, 3),
                     ha='center')
    plt.xlabel('Labels')
    plt.ylabel('Confidence')
    plt.title('mean of label {:d}'.format(label))
    plt.grid(True)


def plot_std(std_data, label):
    plt.figure()
    plt.plot(labels, std_data)
    for label_, value_ in zip(labels, std_data):
        plt.annotate("{}".format(label_),
                     (label_, value_),
                     textcoords="offset points",
                     xytext=(0, 3),
                     ha='center')
    plt.xlabel('Labels')
    plt.ylabel('Standard deviation')
    plt.title('std of label {:d}'.format(label))
    plt.grid(True)


def plot_figure(std_data, title, xlabel="Labels", ylabel="Confidence"):
    plt.figure()
    plt.plot(labels, std_data)
    for label_, value_ in zip(labels, std_data):
        plt.annotate("{}".format(label_),
                     (label_, value_),
                     textcoords="offset points",
                     xytext=(0, 3),
                     ha='center')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)










