import amr_elements
import threading

amr = amr_elements.AMRServerElement("192.168.0.249")
amr_6 = amr_elements.AMRElement("192.168.1.248")
amr_7 = amr_elements.AMRElement("192.168.1.249")
graph_id = 'cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd'


def main():
    #  Get AMR Statuses  #
    amr.get_json('/amrs/statuses')

    #  Codes for AMR 6 to be written in the while loop inside function amr6()  #
    def amr6():
        amr_id = 6
        if amr.get_waypoint(amr_id) != 1:
            amr.send_goal_auto_release(amr_id, graph_id, 1)
        amr.send_goal_auto_release(amr_id, graph_id, 65)

    #  Codes for AMR 7 to be written in the while loop inside function amr7()  #
    def amr7():
        amr_id = 7
        amr.send_goal_auto_release(amr_id, graph_id, 8)

    #  The codes below are used for concurrency and parallelism  #
    #  amr6_thread = threading.Thread(target=amr6)
    amr7_thread = threading.Thread(target=amr7)

    #  amr6_thread.start()
    amr7_thread.start()


main()
