import rosbag
bag = rosbag.Bag('Test.bag')
for topic, msg, t in bag.read_messages(topics=['chatter', 'number']):
    print(msg)
bag.close()
