import logging

logger = logging.getLogger(__name__)

def load_segmentation_model_unet():
    import tensorflow as tf

    import os
    model_path = os.path.join('prediction', 'ml_models', 'segmentation','unet_best_model_3.keras')
    try:
        model = tf.keras.models.load_model(model_path, compile=False)
        print('unet model loaded')
        return model
    except Exception as e:
        print('error loading unet model')
        logger.error(f'error loading unet model {e}')
        return None
