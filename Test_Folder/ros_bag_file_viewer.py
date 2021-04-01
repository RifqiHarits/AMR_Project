import pyrosbag
bag = pyrosbag.Bag('Operation_magnusamr1_2021-03-18-09-19-26_0.bag')
for topic, msg, t in bag.read_messages('numbers'):
    print(msg.data)
bag.close();