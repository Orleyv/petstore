import logging as logger
from typing import Any
import requests
from requests import Response
from settings import HOST


class API:

    def __init__(self) -> None:
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "api_key": "special-key"
        }

    def _url(self, host: str, endpoint: str) -> str:
        return f"{host}{endpoint}"

    def _request(self,
                 method: str,
                 url: str,
                 json_data: dict = None,
                 data: Any = None,
                 params: dict = None,
                 headers: dict = None,
                 files: dict = None,
                 host: str = HOST) -> requests.Response:
        logger.info(f"{method} request sent to {url}")
        return requests.request(
            method,
            url=self._url(host, url),
            headers=headers if headers is not None else self.headers,
            json=json_data,
            data=data,
            params=params,
            files=files,
            timeout=60
        )

    def find_pet(self, status: str) -> Response:
        params = {
            "status": status
        }
        return self._request(
            method="GET",
            url="/v2/pet/findByStatus",
            host=HOST,
            params=params
        )

    def add_pet(self, pet_id: int, pet_name: str) -> requests.Response:
        payload = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": pet_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        return self._request(
            method="POST",
            url="/v2/pet/",
            host=HOST,
            json_data=payload
        )

    def update_pet(self, pet_id: int, pet_name: str) -> requests.Response:
        payload = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": pet_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        return self._request(
            method="PUT",
            url="/v2/pet/",
            host=HOST,
            json_data=payload
        )

    def remove_pet(self, pet_id: int) -> Response:
        return self._request(
            method="DELETE",
            url="/v2/pet/" + str(pet_id),
            host=HOST
        )


    def check_pet(self, pet_id: int) -> Response:
        return self._request(
            method="GET",
            url="/v2/pet/" + str(pet_id),
            host=HOST
        )

    def update_fields(self, pet_id: int, pet_name: str, pet_status: str) -> requests.Response:
        data = {
            "name": pet_name,
            "status": pet_status
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }

        response = self._request(
            method="POST",
            url=f"/v2/pet/{pet_id}",
            data=data,
            headers=headers,
            host=HOST
        )

        return response

    def upload_image(self, pet_id: int, files: dict, additional_metadata: str = None) -> requests.Response:

        data = {}
        if additional_metadata:
            data['additionalMetadata'] = additional_metadata

        headers = {
            "Accept": "application/json"
        }

        return self._request(
            method="POST",
            url=f"/v2/pet/{pet_id}/uploadImage",
            data=data,
            files=files,
            host=HOST,
            headers=headers
        )
