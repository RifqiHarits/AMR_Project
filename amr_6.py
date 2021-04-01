import amr_elements

amr_6 = amr_elements.AMRElement()
amr_6.get_json('/status/batteries')

amr = amr_elements.AMRServerElement()
amr.get_json('/amrs/statuses')
