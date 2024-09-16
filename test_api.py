import pytest
import logging as logger
from helpers.api import API


def test_add_pet():
    api = API()
    added_pet = api.add_pet(pet_id=666, pet_name="Faust")
    logger.info(f"Added pet: {added_pet.text}")
    assert added_pet.status_code == 200, f"Expected status code 200. Got {added_pet.status_code} status code"


def test_add_pet_invalid_data():
    api = API()
    # Invalid pet ID and missing name
    added_pet = api.add_pet(pet_id=None, pet_name="")
    logger.info(f"Add pet with invalid data response: {added_pet.text}")
    assert added_pet.status_code == 400, f"Expected status code 400 for invalid input. Got {added_pet.status_code} status code"



def test_update_pet():
    api = API()
    updated_pet = api.update_pet(pet_id=666, pet_name="Faust2")
    logger.info(f"Updated pet: {updated_pet.text}")
    assert updated_pet.status_code == 200, f"Expected status code 200. Got {updated_pet.status_code} status code"


def test_update_non_existent_pet():
    api = API()
    updated_pet = api.update_pet(pet_id=999999, pet_name="NonExistent")
    logger.info(f"Update non-existent pet response: {updated_pet.text}")
    assert updated_pet.status_code == 404, f"Expected status code 404 for non-existent pet. Got {updated_pet.status_code} status code"



def test_find_pet():
    api = API()
    found_pets = api.find_pet(status="sold")
    logger.info(f"Status code: {found_pets.status_code}")
    assert found_pets.status_code == 200, f"Expected status code 200. Got {found_pets.status_code} status code"


def test_find_pet_invalid_status():
    api = API()
    found_pets = api.find_pet(status="unknown")
    logger.info(f"Find pet with invalid status response: {found_pets.text}")
    assert found_pets.status_code == 400, f"Expected status code 400 for invalid status. Got {found_pets.status_code} status code"



def test_check_pet():
    api = API()
    pet = api.check_pet(pet_id=666)
    logger.info(f"Pet by id: {pet.text}")
    assert pet.status_code == 200, f"Expected status code 200. Got {pet.status_code} status code"


def test_check_non_existent_pet():
    api = API()
    pet = api.check_pet(pet_id=999999)
    logger.info(f"Check non-existent pet response: {pet.text}")
    assert pet.status_code == 404, f"Expected status code 404 for non-existent pet. Got {pet.status_code} status code"



def test_update_fields():
    api = API()
    updated_pet_fields = api.update_fields(pet_id=666, pet_name="Hans", pet_status="pending")
    logger.info(f"Updated fields: {updated_pet_fields.text}")
    assert updated_pet_fields.status_code == 200, f"Expected status code 200. Got {updated_pet_fields.status_code} status code"


def test_update_fields_invalid_data():
    api = API()
    updated_pet_fields = api.update_fields(pet_id=666, pet_name="Hans", pet_status="invalid_status")
    logger.info(f"Update fields with invalid status response: {updated_pet_fields.text}")
    assert updated_pet_fields.status_code == 400, f"Expected status code 400 for invalid status. Got {updated_pet_fields.status_code} status code"


def test_remove_pet():
    api = API()
    remove_response = api.remove_pet(pet_id=666)
    logger.info(f"Removed pet: {remove_response.text}")
    assert remove_response.status_code == 200, f"Expected status code 200. Got {remove_response.status_code} status code"


def test_remove_non_existent_pet():
    api = API()
    remove_response = api.remove_pet(pet_id=999999)
    logger.info(f"Remove non-existent pet response: {remove_response.text}")
    assert remove_response.status_code == 404, f"Expected status code 404 for non-existent pet. Got {remove_response.status_code} status code"


def test_upload_image():
    api = API()
    # Positive case: Valid image upload
    with open('files/Cane_corso.png', 'rb') as file:
        files = {'file': file}
        response = api.upload_image(pet_id=666, files=files, additional_metadata="additional_test_data")
        logger.info(f"Upload response: {response.text}")
        assert response.status_code == 200, f"Expected status code 200. Got {response.status_code} status code"


def test_upload_image_negative():
    api = API()
    # Negative case: Missing file
    response = api.upload_image(pet_id=666, files={}, additional_metadata="additional_test_data")
    logger.info(f"Negative upload response: {response.text}")
    assert response.status_code == 400, f"Expected status code 400. Got {response.status_code} status code"




