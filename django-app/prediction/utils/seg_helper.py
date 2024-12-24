def load_segmentation_model_yolo():
    from ultralytics import YOLO
    import os

    model_path = os.path.join('prediction', 'ml_models', 'segmentation')
    try:
        model = YOLO(os.path.join(model_path, 'best.pt'))
        print('Yolo segmentation Model loaded successfully')
        return model
    except Exception as e:
        print(f'Yolo segmentation Error occurred: {e}')
        return None
