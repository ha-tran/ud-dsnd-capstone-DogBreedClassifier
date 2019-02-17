import io
from flask import jsonify
from flask import request
from flask_restful import Resource
import json
import numpy as np
from keras.applications import imagenet_utils
from keras.applications import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.models import model_from_json
from keras.preprocessing import image
import tensorflow as tf
from PIL import Image
from app.modules.classifier.utils.path_to_tensor import path_to_tensor


dog_names = ['Affenpinscher', 'Afghan_hound', 'Airedale_terrier', 'Akita', 'Alaskan_malamute', 'American_eskimo_dog', 'American_foxhound', 'American_staffordshire_terrier', 'American_water_spaniel', 'Anatolian_shepherd_dog', 'Australian_cattle_dog', 'Australian_shepherd', 'Australian_terrier', 'Basenji', 'Basset_hound', 'Beagle', 'Bearded_collie', 'Beauceron', 'Bedlington_terrier', 'Belgian_malinois', 'Belgian_sheepdog', 'Belgian_tervuren', 'Bernese_mountain_dog', 'Bichon_frise', 'Black_and_tan_coonhound', 'Black_russian_terrier', 'Bloodhound', 'Bluetick_coonhound', 'Border_collie', 'Border_terrier', 'Borzoi', 'Boston_terrier', 'Bouvier_des_flandres', 'Boxer', 'Boykin_spaniel', 'Briard', 'Brittany', 'Brussels_griffon', 'Bull_terrier', 'Bulldog', 'Bullmastiff', 'Cairn_terrier', 'Canaan_dog', 'Cane_corso', 'Cardigan_welsh_corgi', 'Cavalier_king_charles_spaniel', 'Chesapeake_bay_retriever', 'Chihuahua', 'Chinese_crested', 'Chinese_shar-pei', 'Chow_chow', 'Clumber_spaniel', 'Cocker_spaniel', 'Collie', 'Curly-coated_retriever', 'Dachshund', 'Dalmatian', 'Dandie_dinmont_terrier', 'Doberman_pinscher', 'Dogue_de_bordeaux', 'English_cocker_spaniel', 'English_setter', 'English_springer_spaniel', 'English_toy_spaniel', 'Entlebucher_mountain_dog', 'Field_spaniel', 'Finnish_spitz', 'Flat-coated_retriever', 'French_bulldog', 'German_pinscher', 'German_shepherd_dog', 'German_shorthaired_pointer', 'German_wirehaired_pointer', 'Giant_schnauzer', 'Glen_of_imaal_terrier', 'Golden_retriever', 'Gordon_setter', 'Great_dane', 'Great_pyrenees', 'Greater_swiss_mountain_dog', 'Greyhound', 'Havanese', 'Ibizan_hound', 'Icelandic_sheepdog', 'Irish_red_and_white_setter', 'Irish_setter', 'Irish_terrier', 'Irish_water_spaniel', 'Irish_wolfhound', 'Italian_greyhound', 'Japanese_chin', 'Keeshond', 'Kerry_blue_terrier', 'Komondor', 'Kuvasz', 'Labrador_retriever', 'Lakeland_terrier', 'Leonberger', 'Lhasa_apso', 'Lowchen', 'Maltese', 'Manchester_terrier', 'Mastiff', 'Miniature_schnauzer', 'Neapolitan_mastiff', 'Newfoundland', 'Norfolk_terrier', 'Norwegian_buhund', 'Norwegian_elkhound', 'Norwegian_lundehund', 'Norwich_terrier', 'Nova_scotia_duck_tolling_retriever', 'Old_english_sheepdog', 'Otterhound', 'Papillon', 'Parson_russell_terrier', 'Pekingese', 'Pembroke_welsh_corgi', 'Petit_basset_griffon_vendeen', 'Pharaoh_hound', 'Plott', 'Pointer', 'Pomeranian', 'Poodle', 'Portuguese_water_dog', 'Saint_bernard', 'Silky_terrier', 'Smooth_fox_terrier', 'Tibetan_mastiff', 'Welsh_springer_spaniel', 'Wirehaired_pointing_griffon', 'Xoloitzcuintli', 'Yorkshire_terrier']

def load_model():
    """ Load Kera models
    """
    global ResNet50_model
    ResNet50_model = ResNet50(weights="imagenet")
    global bottleneck_model
    bottleneck_model = ResNet50(weights="imagenet", include_top=False)
    global model
    json_file = open("ml_models/alt_model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights("ml_models/weights.best.DogResnet50Data.hdf5")

    global graph
    graph = tf.get_default_graph()


def ResNet50_predict_labels(img):
    # returns prediction vector for image
    img = preprocess_input(path_to_tensor(img))

    with graph.as_default():
        preds = ResNet50_model.predict(img)
        return np.argmax(preds)

def dog_detector(img):
    """ Detect if image has a dog
    """
    prediction = ResNet50_predict_labels(img)
    return ((prediction <= 268) & (prediction >= 151))

def predict_breed(img):
    """ Predict dog breed
    """
    # extract bottleneck features
    tensor = path_to_tensor(img)
    with graph.as_default():
        bottleneck_feature = bottleneck_model.predict(preprocess_input(tensor))
        # obtain predicted vector
        predicted_vector = model.predict(bottleneck_feature)
        # return dog breed that is predicted by the model
        return dog_names[np.argmax(predicted_vector)]

load_model()


class ClassifierAPI(Resource):
    def post(self):
        # read the image in PIL format
        image = request.files['image'].read()
        image = Image.open(io.BytesIO(image))

        is_dog = dog_detector(image)

        breed = ""

        # find dog breed
        breed = predict_breed(image)

        return {
            "is_dog": "{}".format(is_dog),
            "breed": "{}".format(breed)
        }, 201