import amr_elements


amr_server = amr_elements.AMRServerElement()
amr_server.get_json('/deployment/binaries')

goal = {
    "amr_id": 7,  # AMR ID
    "graph_id": "cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd",  # MAP GRAPH ID
    "waypoint_id": 2,  # WAYPOINT ID
    "created_by": "fleet"  # CREATED BY FLEET AND NOT MISSION
}

amr_server.post_json('/goals', goal)  # SEND AMR TO GOAL
