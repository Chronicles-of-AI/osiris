from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.monitoring.data_monitoring_request import (
    CreateClassificationDataRecord,
    CreateObjectDetectionRecord,
    CreateNERRecord,
)
from sql.apis.schemas.responses.aws.comprehend_response import (
    CreateDocumentClassifierResponse,
)
from sql.controllers.monitoring.data_monitoring_controller import (
    DataMonitoringController,
)
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
data_monitoring_router = APIRouter()


@data_monitoring_router.post(
    "/osairis/data_monitoring/image_classification/create",
    response_model=CreateDocumentClassifierResponse,
)
async def create_image_classification_record(
    create_image_classification_record_request: CreateClassificationDataRecord,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_data_record_request (CreateDataRecord): [Create Data Record]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        logging.debug(f"Request: {create_image_classification_record_request}")
        if decodeJWT(token=token):
            response = DataMonitoringController().create_image_classification_record_controller(
                request=create_image_classification_record_request
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/data_monitoring/create endpoint: {error}")
        raise error


@data_monitoring_router.post(
    "/osairis/data_monitoring/text_classification/create",
    response_model=CreateDocumentClassifierResponse,
)
async def create_text_classification_record(
    create_text_classification_record_request: CreateClassificationDataRecord,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_data_record_request (CreateDataRecord): [Create Data Record]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        logging.debug(f"Request: {create_text_classification_record_request}")
        if decodeJWT(token=token):
            response = (
                DataMonitoringController().create_text_classification_record_controller(
                    request=create_text_classification_record_request
                )
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/data_monitoring/create endpoint: {error}")
        raise error


@data_monitoring_router.post(
    "/osairis/data_monitoring/object_detection/create",
    response_model=CreateDocumentClassifierResponse,
)
async def create_object_detection_record(
    create_object_detection_record_request: CreateObjectDetectionRecord,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_data_record_request (CreateDataRecord): [Create Data Record]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        logging.debug(f"Request: {create_object_detection_record_request}")
        if decodeJWT(token=token):
            response = (
                DataMonitoringController().create_object_detection_record_controller(
                    request=create_object_detection_record_request
                )
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/data_monitoring/create endpoint: {error}")
        raise error


@data_monitoring_router.post(
    "/osairis/data_monitoring/ner/create",
    response_model=CreateDocumentClassifierResponse,
)
async def create_ner_record(
    create_ner_record_request: CreateNERRecord,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_data_record_request (CreateDataRecord): [Create Data Record]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        logging.debug(f"Request: {create_ner_record_request}")
        if decodeJWT(token=token):
            response = DataMonitoringController().create_ner_record_controller(
                request=create_ner_record_request
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/data_monitoring/create endpoint: {error}")
        raise error
