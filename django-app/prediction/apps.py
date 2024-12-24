import logging

from django.apps import AppConfig

from prediction.utils.ml_handler_new import new_run
from prediction.utils.seg_helper import load_segmentation_model_yolo
from prediction.utils.segmentation import load_segmentation_model_unet

class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prediction'
    segmentation_model_yolo = None
    segmentation_model_unet = None
    new_generator = None
    chosen_segmentation_model = 'yolo'
    segmentation_config_unet = {
        'threshold' : 0.5,
        'target_size' : (256, 256),
    }
    prediction_config = {
        'image_size' : 256,
        'padding' : 10,
    }


    def ready(self):
        logger = logging.getLogger(__name__)
        PredictionConfig.new_generator = new_run()
        PredictionConfig.segmentation_model_yolo = load_segmentation_model_yolo()
        PredictionConfig.segmentation_model_unet = load_segmentation_model_unet()
