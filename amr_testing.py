import amr_elements
import json


amr_server = amr_elements.AMRServerElement()
amr_server.get_json('/deployment/binaries')
amr_server.get_json('/goals')
goal = {
    "amr_id": 7,
    "graph_id": "cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd",
    "waypoint_id": 6,
    "created_by": "fleet"
}
# amr_server.post_json('/goals', goal)
# amr_server.get_json('/manager/actions/trees')

# print(amr_server.get_json('/manager/tasks/definitions')[8]['creation']['goals'])

task_st3_4_6_wait3 = {
    "amr_id": 7,
    "payload_type": 3,
    "slots": 0,
    "goals": [
        {
            'index': 0,
            'destination': {
                'graph_id': 'cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd',
                'waypoint_id': 3
            },
            'action_trees': [{'id': 5, 'name': 'Wait_3s_Action', 'description': '', 'tree': {'name': 'Wait_3s_Action', 'children': [{'id': 5, 'name': 'Wait_2s', 'description': '', 'command': 'Wait', 'parameters': {'command_method': 'timer', 'time': 2}, 'capacity': 1, 'timestamp': '2021-03-18 08:44:52'}, {'id': 6, 'name': 'Wait_1s', 'description': '', 'command': 'Wait', 'parameters': {'command_method': 'timer', 'time': 1}, 'capacity': 1, 'timestamp': '2021-03-18 08:45:33'}], 'control_flow': 'sequence', 'parameters': {}}, 'error': '', 'timestamp': '2021-03-18 09:02:33'}]
        },
        {
            'index': 1,
            'destination':
                {'graph_id': 'cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd',
                 'waypoint_id': 4
                 },
            'action_trees': [{'id': 5, 'name': 'Wait_3s_Action', 'description': '', 'tree': {'name': 'Wait_3s_Action', 'children': [{'id': 5, 'name': 'Wait_2s', 'description': '', 'command': 'Wait', 'parameters': {'command_method': 'timer', 'time': 2}, 'capacity': 1, 'timestamp': '2021-03-18 08:44:52'}, {'id': 6, 'name': 'Wait_1s', 'description': '', 'command': 'Wait', 'parameters': {'command_method': 'timer', 'time': 1}, 'capacity': 1, 'timestamp': '2021-03-18 08:45:33'}], 'control_flow': 'sequence', 'parameters': {}}, 'error': '', 'timestamp': '2021-03-18 09:02:33'}]
        },
        {
            'index': 2,
            'destination':
                {
                    'graph_id': 'cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd',
                    'waypoint_id': 6
                },
            'action_trees': [{'id': 5, 'name': 'Wait_3s_Action', 'description': '', 'tree': {'name': 'Wait_3s_Action', 'children': [{'id': 5, 'name': 'Wait_2s', 'description': '', 'command': 'Wait', 'parameters': {'command_method': 'timer', 'time': 2}, 'capacity': 1, 'timestamp': '2021-03-18 08:44:52'}, {'id': 6, 'name': 'Wait_1s', 'description': '', 'command': 'Wait', 'parameters': {'command_method': 'timer', 'time': 1}, 'capacity': 1, 'timestamp': '2021-03-18 08:45:33'}], 'control_flow': 'sequence', 'parameters': {}}, 'error': '', 'timestamp': '2021-03-18 09:02:33'}]
        }
    ],
    "task_definition_id": amr_server.get_json('/manager/tasks/definitions')[8]['id']
}

# amr_server.post_json('/ensemble/task', task_st3_4_6_wait3)
# amr_server.get_json('/ensemble/task')
# amr_6 = amr_elements.AMRElement()
# amr_7 = amr_elements.AMRElement("192.168.1.249")

# amr_6.get_json('/status/batteries')
# amr_7.get_json('/status/batteries')
# amr_server.get_json('/amrs/statuses')

'''
data = {
    'id': 6,
    'status': 'released'
}

task = {
    'amr_id': 6,
    'payload_type': 2,
    'mission_id': 6,
    'goals': [{
        'index': 0,
        'destination': {
            'graph_id': '410561f4-45d8-407a-b6ba-29348d2eef70',
            'waypoint_id': 3
        },
        'action_trees': [4]
        },
        {
            'index': 1,
            'destination': {
                'graph_id': '410561f4-45d8-407a-b6ba-29348d2eef70',
                'waypoint_id': 4
             },
        'action_trees': [3]
        },
        {
            'index': 2,
            'destination':
                {
                    'graph_id': '410561f4-45d8-407a-b6ba-29348d2eef70',
                    'waypoint_id': 1
                },
            'action_trees': [5]
        },
        {
            'index': 3,
            'destination':
                {
                    'graph_id': '410561f4-45d8-407a-b6ba-29348d2eef70',
                    'waypoint_id': 3
                },
            'action_trees': [5]
        }
    ],
    'task_definition_id': 6,
    'slots': 1
}

# print(json.dumps(task))

# amr_elements.AMRServerElement().put_json('/amrs/pause', data)
# amr_elements.AMRServerElement().put_json('/amrs/release/idle', data)
# amr_elements.AMRServerElement().get_json('/deployment/binaries')
# amr_elements.AMRServerElement().post_json('/ensemble/tasks', {})
 amr_elements.AMRServerElement().get_json('/ensemble/task')
'''