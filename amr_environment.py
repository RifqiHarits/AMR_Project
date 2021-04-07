import amr_elements
import threading

#  AMC GRAPH  #
graph_id = 'cd0f463f-17f5-4f35-aa7e-a99c5c28bdfd'

amr = amr_elements.AMRServerElement("192.168.0.249")
amr_6 = amr_elements.AMRElement("192.168.1.248")
amr_7 = amr_elements.AMRElement("192.168.1.249")


def main():
    #  Set True to respective AMR if they will be used  #
    amr6_use = True
    amr7_use = True

    charging_waypoint = 96

    def choice(amr_id):
        ans = input("Do you want to continue task for AMR {}? (Y/N): ".format(amr_id))
        if ans.lower() == "y":
            return True
        else:
            return False

    #  This will loop if AMR Server is offline  #
    while not amr.pingable_result:
        amr.pingable()
        amr.request_token()

    #  Get AMR Statuses  #
    amr.get_json('/amrs/statuses')

    #  Codes for AMR 6 to be written in the while loop inside function amr6()  #
    def amr6():
        if not amr6_use:
            return
        #  This will loop if AMR 6 is offline  #
        while not amr_6.pingable_result:
            amr_6.pingable()

        amr_id = 6
        #  Making sure AMR 6 starts from RC1  #
        if amr.get_waypoint(amr_id) != 1:
            amr.send_goal_auto_release(amr_id, graph_id, 1)

        #  This will let it loop forever if AMR 6 remains online  #
        while amr_6.pingable():
            amr.send_goal_auto_release(amr_id, graph_id, 4)
            amr.wait(4)
            amr.send_idle_wait_reached(amr_id)
            amr.send_goal_auto_release(amr_id, graph_id, 3)
            amr.wait(4)
            if amr_6.get_main_battery_percentage() < 40:
                break
            # if not choice(amr_id):
            #    break
        #  Send to RC1  #
        if amr_6.pingable():
            if amr_6.get_main_battery_percentage() < 40:
                amr.send_goal(amr_id, graph_id, charging_waypoint)
                while amr_6.get_main_battery_percentage() < 95:
                    amr.wait(120)
            amr.send_goal_auto_release(amr_id, graph_id, 1)

    #  Codes for AMR 7 to be written in the while loop inside function amr7()  #
    def amr7():
        if not amr7_use:
            return
        #  This will loop if AMR 7 is offline  #
        while not amr_7.pingable_result:
            amr_7.pingable()

        amr_id = 7
        #  Making sure AMR 7 starts from RC46  #
        if amr.get_waypoint(amr_id) != 46:
            amr.send_goal_auto_release(amr_id, graph_id, 46)

        #  This will let it loop forever if AMR 7 remains online  #
        while amr_7.pingable():
            amr.send_goal_auto_release(amr_id, graph_id, 3)
            amr.wait(4)
            amr.send_idle_wait_reached(amr_id)
            amr.send_goal_auto_release(amr_id, graph_id, 4)
            amr.wait(4)
            if amr_7.get_main_battery_percentage() < 40:
                break
            # if not choice(amr_id):
            #    break
        #  Send to RC46  #
        if amr_7.pingable():
            if amr_7.get_main_battery_percentage() < 40:
                amr.send_goal(amr_id, graph_id, charging_waypoint)
                while amr_7.get_main_battery_percentage() < 95:
                    amr.wait(120)
            amr.send_goal_auto_release(amr_id, graph_id, 46)

    #  The codes below are used for concurrency and parallelism  #
    amr6_thread = threading.Thread(target=amr6)
    amr7_thread = threading.Thread(target=amr7)

    amr6_thread.start()
    amr7_thread.start()


main()
