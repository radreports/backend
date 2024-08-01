from datetime import time
from time import sleep
import requests
from fhirclient import client
from fhirclient.models.observation import Observation
from fhirclient.models.imagingstudy import ImagingStudy
from fhirclient.models.servicerequest import ServiceRequest
from fhirclient.models.bundle import Bundle

# FHIR server settings
settings = {
    'app_id': None,
    'api_base': 'https://ehr.radassist.ai/fhir',  # Replace with your actual FHIR server base URL
}
base_url = 'https://ehr.radassist.ai/fhir'
# Initialize FHIR client
smart = client.FHIRClient(settings=settings)

def get_imagingstudy_ids(resource):
    response = requests.get(f"{base_url}/{resource}")
    response.raise_for_status()  # Ensure we notice bad responses
    data = response.json()

    ids = [entry['resource']['id'] for entry in data.get('entry', [])]
    return ids

def delete_imagingstudy(resource,resource_id):
    response = requests.delete(f"{base_url}/{resource}/{resource_id}")
    if response.status_code == 204:
        print(f"Deleted {resource} with ID: {resource_id}")
    else:
        print(f"Failed to delete {resource} with ID: {resource_id}. Status code: {response.status_code}")

# Get all ImagingStudy IDs
def deletes_study(resource):
    imagingstudy_ids = get_imagingstudy_ids(resource)

# Delete each ImagingStudy by ID
    for resource_id in imagingstudy_ids:
        delete_imagingstudy(resource,resource_id)
        print(f"Deleted {resource} with ID: {resource_id}")

def delete_resource(resource_type):
    search = resource_type.where(struct={})
    resources_bundle = search.perform(smart.server)

    if resources_bundle is not None and isinstance(resources_bundle, Bundle):
        for entry in resources_bundle.entry:
            resource = entry.resource
            print(f"Deleting {resource.resource_type} with ID: {resource.id}")
            resource.delete(smart.server)
    else:
        print(f"No {resource_type.resource_type} resources found or failed to retrieve {resource_type.resource_type} resources.")

    print(f"All {resource_type.resource_type} resources have been deleted.")
# # Perform search for Observation resources
# search = Observation.where(struct={})
# observations_bundle = search.perform(smart.server)

# # Check if the response is a Bundle and iterate through the entries
# if observations_bundle is not None and isinstance(observations_bundle, Bundle):
#     for entry in observations_bundle.entry:
#         observation = entry.resource
#         print(f"Deleting Observation with ID: {observation.id}")
#         observation.delete(smart.server)
# else:
#     print("No observations found or failed to retrieve observations.")

# print("All observations have been deleted.")

if __name__ == "__main__":
    while True:
        deletes_study("Observation")
        # sleep(40)

    # while True:
    #     try:
    #         delete_resource(ImagingStudy)
            
    #     except Exception as e:
    #         print(f"An error occurred for ImagingStudy: {e}")
            
    #     try:
    #         delete_resource(Observation)
    #     except Exception as e:
    #         print(f"An error occurred for Observation : {e}")

    #     # try:
    #     #     delete_resource(ServiceRequest)
    #     # except Exception as e:
    #     #     print(f"An error occurred: {e}")
    #     sleep(60)  # Sleep for 1 minute (60 seconds)
    