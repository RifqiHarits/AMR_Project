import amr_elements


amr_server = amr_elements.AMRServerElement()
amr_server.get_json('/deployment/binaries')

task_st3_4_6_wait3 = {
    "amr_id": 7,
    "payload_type": 3,
    "slots": 1,
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

amr_server.post_json('/ensemble/task', task_st3_4_6_wait3)
