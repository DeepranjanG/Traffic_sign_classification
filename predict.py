import numpy as np
from PIL import Image
import cv2
import tensorflow as tf

class traffic:
    def __init__(self,filename):
        self.filename =filename


    def trafficsign(self):

        model_path = "Traffic.h5"
        loaded_model = tf.keras.models.load_model(model_path)

        imagename = self.filename
        image = cv2.imread(imagename)

        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((30, 30))
        expand_input = np.expand_dims(resize_image,axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255
        pred = loaded_model.predict(input_data)
        result = pred.argmax()

        if result == 0:
            prediction = 'Speed limit (20km/h)'
            return [{"image": prediction}]
        elif result == 1:
            prediction = 'Speed limit (30km/h)'
            return [{"image": prediction}]
        elif result == 2:
            prediction = 'Speed limit (50km/h)'
            return [{"image": prediction}]
        elif result == 3:
            prediction = 'Speed limit (60km/h)'
            return [{"image": prediction}]
        elif result == 4:
            prediction = 'Speed limit (70km/h)'
            return [{"image": prediction}]
        elif result == 5:
            prediction = 'Speed limit (80km/h)'
            return [{"image": prediction}]
        elif result == 6:
            prediction = 'End of speed limit (80km/h)'
            return [{"image": prediction}]
        elif result == 7:
            prediction = 'Speed limit (1000km/h)'
            return [{"image": prediction}]
        elif result == 8:
            prediction = 'Speed limit (120km/h)'
            return [{"image": prediction}]
        elif result == 9:
            prediction = 'No passing'
            return [{"image": prediction}]
        elif result == 10:
            prediction = 'No passing veh over 3.5 tons'
            return [{"image": prediction}]
        elif result == 11:
            prediction = 'Right-of-way at intersection'
            return [{"image": prediction}]
        elif result == 12:
            prediction = 'Priority road'
            return [{"image": prediction}]
        elif result == 13:
            prediction = 'Yield'
            return [{"image": prediction}]
        elif result == 14:
            prediction = 'Stop'
            return [{"image": prediction}]
        elif result == 15:
            prediction = 'No vehicles'
            return [{"image": prediction}]
        elif result == 16:
            prediction = 'Veh > 3.5 tons prohibited'
            return [{"image": prediction}]
        elif result == 17:
            prediction = 'No entry'
            return [{"image": prediction}]
        elif result == 18:
            prediction = 'General caution'
            return [{"image": prediction}]
        elif result == 19:
            prediction = 'Dangerous curve left'
            return [{"image": prediction}]
        elif result == 20:
            prediction = 'Dangerous curve right'
            return [{"image": prediction}]
        elif result == 21:
            prediction = 'Double curve'
            return [{"image": prediction}]
        elif result == 22:
            prediction = 'Bumpy road'
            return [{"image": prediction}]
        elif result == 23:
            prediction = 'Slippery road'
            return [{"image": prediction}]
        elif result == 24:
            prediction = 'Road narrows on the right'
            return [{"image": prediction}]
        elif result == 25:
            prediction = 'Road work'
            return [{"image": prediction}]
        elif result == 26:
            prediction = 'Traffic signals'
            return [{"image": prediction}]
        elif result == 27:
            prediction = 'Pedestrians'
            return [{"image": prediction}]
        elif result == 28:
            prediction = 'Children crossing'
            return [{"image": prediction}]
        elif result == 29:
            prediction = 'Bicycles crossing'
            return [{"image": prediction}]
        elif result == 30:
            prediction = 'Beware of ice/snow'
            return [{"image": prediction}]
        elif result == 31:
            prediction = 'Wild animals crossing'
            return [{"image": prediction}]
        elif result == 32:
            prediction = 'End speed + passing limits'
            return [{"image": prediction}]
        elif result == 33:
            prediction = 'Turn right ahead'
            return [{"image": prediction}]
        elif result == 34:
            prediction = 'Turn left ahead'
            return [{"image": prediction}]
        elif result == 35:
            prediction = 'Ahead only'
            return [{"image": prediction}]
        elif result == 36:
            prediction = 'Go straight or right'
            return [{"image": prediction}]
        elif result == 37:
            prediction = 'Go straight or left'
            return [{"image": prediction}]
        elif result == 38:
            prediction = 'Keep right'
            return [{"image": prediction}]
        elif result == 39:
            prediction = 'Keep left'
            return [{"image": prediction}]
        elif result == 40:
            prediction = 'Roundabout mandatory'
            return [{"image": prediction}]
        elif result == 41:
            prediction = 'End of no passing'
            return [{"image": prediction}]
        elif result == 42:
            prediction = 'End no passing veh > 3.5 tons'
            return [{"image": prediction}]
        else:
            return [{"ERROR": "Please select another image. !!!"}]

