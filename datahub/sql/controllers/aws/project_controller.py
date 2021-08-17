import logging
from sql.crud.project_crud import CRUDProject
from commons.external_call import APIInterface
from sql import config, logger
from datetime import datetime

logging = logger(__name__)


class ProjectController:
    def __init__(self):
        self.CRUDProject = CRUDProject()
        self.core_aws_project_config = (
            config.get("core_engine").get("aws").get("project_router")
        )

    def create_project(self, request: dict):
        """[Controller function to create an AWS Rekognition project]

        Args:
            request ([dict]): [AWS Rekognition project request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [AWS boto3 create project response]
        """
        try:
            logging.info("executing create_project function")
            uuid = str(int(datetime.now().timestamp()))
            project_request = dict(request)
            create_project_url = self.core_aws_project_config.get("create_project")
            response, status_code = APIInterface.post(
                route=create_project_url, data=project_request
            )
            project_request.update(response)
            project_request.update({"uuid": uuid, "status": "CREATED"})
            self.CRUDProject.create(**project_request)
            return project_request
        except Exception as error:
            logging.error(f"Error in create_project function: {error}")
            raise error

    def delete_project(self, request: dict):
        """[Controller function to delete an AWS Rekognition project]

        Args:
            request ([dict]): [AWS Rekognition project request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [AWS boto3 delete project response]
        """
        try:
            logging.info("executing delete_project function")
            project_request = dict(request)
            delete_project_url = self.core_aws_project_config.get("delete_project")
            response, status_code = APIInterface.post(
                route=delete_project_url, data=project_request
            )
            if status_code == 200:
                self.CRUDProject.delete(request.project_arn)
            else:
                raise Exception({"status": "delete project failed"})
            return {
                "project_arn": request.project_arn,
                "status": response.get("project_status"),
            }
        except Exception as error:
            logging.error(f"Error in delete_project function: {error}")
            raise error

    def get_all_projects(self):
        """[Controller function to get all AWS Rekognition project]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [List of all the projects on AWS Rekognition]
        """
        try:
            logging.info("executing get_all_projects function")
            get_all_projects_url = self.core_aws_project_config.get("get_all_projects")
            response, _ = APIInterface.get(route=get_all_projects_url)
            return response
        except Exception as error:
            logging.error(f"Error in get_all_projects function: {error}")
            raise error

    def get_project_description(self, project_arn: str, version_names: str = None):
        """[Controller function to get description of an AWS Rekognition project]

        Args:
            project_arn (str): [Unique identifier for AWS Rekognition project]
            version_names (str, optional): [Unique identifier for project version]. Defaults to None.

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [project description response from AWS Rekognition]
        """
        try:
            logging.info("executing get_project_description function")
            project_description_url = self.core_aws_project_config.get(
                "project_description"
            )
            project_params = {"project_arn": project_arn, "version_name": version_names}
            response, _ = APIInterface.get(
                route=project_description_url, params=project_params
            )
            return response
        except Exception as error:
            logging.error(f"Error in get_project_description function: {error}")
            raise error
