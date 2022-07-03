import pickle

import cv2
import numpy as np
import tensorflow as tf
from keras.backend import set_session
from keras.preprocessing.image import img_to_array

sess = tf.Session()
graph = tf.get_default_graph()
model_label_path = "base/static/adminResources/models/"
model_name = 'plant_disease_classification_model.pkl'
model_file = model_label_path + model_name
set_session(sess)
model_dump = pickle.load(open(model_file, 'rb'))
label_name = 'plant_disease_label_transform.pkl'
label_file = model_label_path + label_name
label_dump = pickle.load(open(label_file, 'rb'))
DEFAULT_IMAGE_SIZE = tuple((256, 256))


def load_classification(input_file):
    print("input_file=", input_file)
    result_class = predict_disease(input_file)
    print(result_class)
    return result_class


def predict_disease(input_file):
    img = cv2.imread(input_file)
    image_array = img_to_array(cv2.resize(img, DEFAULT_IMAGE_SIZE))
    np_image = np.array(image_array, dtype=np.float16) / 225.0
    np_image = np.expand_dims(np_image, 0)
    global sess
    global graph
    with graph.as_default():
        set_session(sess)
        result_class = model_dump.predict_classes(np_image)
    return label_dump.classes_[result_class][0]
