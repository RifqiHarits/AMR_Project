import amr_elements

amr = amr_elements.AMRServerElement()

data = {
    "task_definition_id": 29,
    "goals": [{
        "index": 0,
        "waypoint_id": 13,
        "pickup": [],
        #"delivery": []
    }, {
        "index": 1,
        "waypoint_id": 4,
        "pickup": [],
        #"delivery": []
    }]
}

data1 = {
    "task_definition_id": 29,
}

# amr.get_json('/manager/tasks/definitions')
amr.create_task(data)
