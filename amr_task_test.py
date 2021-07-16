import amr_elements

amr = amr_elements.AMRServerElement()

data = {
    "task_definition_id": 29,
    "goals": [{
        "index": 0,
        "waypoint_id": 13,
    }],
    "priority": 1
}

amr.get_json('/manager/tasks/definitions')
# amr.update_task(data)
