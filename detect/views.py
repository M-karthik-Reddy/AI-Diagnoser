from django.shortcuts import render
from django.core.files.storage import default_storage
import numpy as np
import os
import cv2  # Ensure OpenCV is installed: pip install opencv-python
from django.conf import settings
# from django.core.files.storage import default_storage
from django.shortcuts import render
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.layers import Flatten, Dense, Dropout, BatchNormalization, Activation
from keras.preprocessing.image import img_to_array
from .models import DiseaseRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth


def build_model():
    vgg16 = VGG16(input_shape=(224, 224, 3), weights='imagenet', include_top=False)
    for layer in vgg16.layers[:-2]:
        layer.trainable = False
    x = Flatten()(vgg16.output)
    x = Dense(256, kernel_initializer='he_uniform')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)

    x = Dense(512, kernel_initializer='he_uniform')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)

    x = Dense(1024, kernel_initializer='he_uniform')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)

    x = Dense(512, kernel_initializer='he_uniform')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)

    x = Dense(256, kernel_initializer='he_uniform')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)

    output = Dense(5, activation='softmax')(x)

    model = Model(inputs=vgg16.input, outputs=output)

    # Load trained weights
    model.load_weights('vgg16_trained.weights.h5')

    return model


# Load model once globally
model = build_model()

# Home page
def index(request):
    return render(request, 'detect_page.html')


# Upload page
def detect_retinopathy(request):
    return render(request, 'upload_retinopathy.html')

@login_required
def retino_result(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        
        # Save image to media/tmp folder
        file_path = default_storage.save('tmp_image.jpg', image_file)
        # full_path = os.path.join(default_storage.location, file_path)
        
        #save the image to media folder.
        # saved_path=default_storage.save(f'/tmp/{image_file.name}',image_file)
        full_path=os.path.join(settings.MEDIA_ROOT,file_path)

        # Prepare image for model
        img = cv2.imread(full_path)
        img = cv2.resize(img, (224, 224))
        img = img.astype('float32') / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict
        preds = model.predict(img)
        pred_label = np.argmax(preds)

        labels = ['No_DR', 'Mild', 'Moderate', 'Severe', 'Proliferative_DR']
        condition = labels[pred_label]
        
        # save to database
        DiseaseRecord.objects.create(
            user=request.user,
            disease='DR',
            image=file_path,
            result=condition
        )

        # Generate image URL for template
        image_url = os.path.join(settings.MEDIA_URL, file_path).replace("\\", "/")

        return render(request, 'result_retinopathy.html', {
            'condition': condition,
            'image_url': image_url
        })

    return render(request, 'upload_retinopathy.html')


@login_required(login_url='/accounts/login')  # Redirect to login if not authenticated
def get_history(request):
    records = DiseaseRecord.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'get_history.html', {'records': records})
