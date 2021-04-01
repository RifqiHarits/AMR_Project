import amr_elements

amr = amr_elements.AMRServerElement("192.168.0.249")
amr_6 = amr_elements.AMRElement("192.168.1.248")
amr_7 = amr_elements.AMRElement("192.168.1.249")
graph_id = 'cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd'

amr.idle_release(7)
amr.get_json('/goals')
