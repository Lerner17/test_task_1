from google.cloud import vision


def localize_objects_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    objects = client.object_localization(
        image=image).localized_object_annotations
    return objects
