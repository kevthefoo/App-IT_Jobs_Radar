import json


def locationRoleSelector(job_location):
    with open('./data/tags/locationTag.json', 'r') as f:
        locationTagData = json.load(f)
    
    job_location_elements = job_location.split(',')

    role = None
    
    for element in job_location_elements:
        job_location = element.strip().lower()
        if job_location in locationTagData:
            role = locationTagData[job_location]["Tag"]
            break

    return role

def titleRoleSelector(job_title):
    with open('./data/tags/titleTag.json', 'r') as f:
        titleTagData = json.load(f)
        target_roles = []

    job_title = job_title.lower()
    if job_title in titleTagData:
        role = titleTagData[job_title]["Tag"]
        target_roles.append(role)

    return target_roles