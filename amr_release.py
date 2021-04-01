import amr_elements


amr_server = amr_elements.AMRServerElement()
amr_server.get_json('/deployment/binaries')
print(amr_server.token)

print(amr_server.get_json('/amrs/release/station'))

"""
release = {
    "id": 7,  # ID OF AMR
    "status": "released"  # RELEASE AMR
}

amr_server.post_json('/amrs/release/station', release)
"""