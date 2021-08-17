import pandas as pd
from core_engine import logger

logging = logger(__name__)


def gcp_object_detection_transformation(json_data: dict):
    """[Object Detection Transformation from Label Studio to AutoML format]

    Args:
        json_data (dict): [Annotations]

    Raises:
        error: [Error]

    Returns:
        [list]: [List of Annotations]
    """
    try:
        logging.info(f"Object Detection Transformation: {json_data}")
        all_annotations = []
        for obj in json_data:
            cloud_uri = obj.get("data").get("image")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            for result in results:
                values = result.get("value")
                image_width = result.get("original_width")
                image_height = result.get("original_height")
                top = values.get("x")
                left = values.get("y")
                annotation_width = values.get("width")
                annotation_height = values.get("height")
                label = values.get("rectanglelabels")[0]
                new_xmin = round((top / image_width), 1)
                new_xmax = round((top + annotation_width / image_width), 1)
                new_ymin = round((left / image_height), 1)
                new_ymax = round((left + annotation_height / image_height), 1)
                new_row = [
                    "UNASSIGNED",
                    cloud_uri,
                    label,
                    new_xmin,
                    new_ymin,
                    "",
                    "",
                    new_xmax,
                    new_ymax,
                    "",
                    "",
                ]
                all_annotations.append(new_row)
        annotations_df = pd.DataFrame(all_annotations)
        return annotations_df
    except Exception as error:
        logging.error(f"{error=}")
        raise error
