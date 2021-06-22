#!/usr/bin/env python  

__author__ ='Raphael Leber'


import rospy 
import actionlib
from std_msgs.msg import String, Int16



class MessageParser():

    def __init__(self):
        rospy.init_node('message_parser_node', anonymous=False)

        # --------------
        # Declare topics
        # --------------
        # * Suscribers
        rospy.Subscriber("/message", String, self.message)
        # * Publishers
        self.pubPerson = rospy.Publisher('/message/person', String, queue_size=1)
        self.pubObject = rospy.Publisher('/message/object', String, queue_size=1)
        self.pubObjectNum = rospy.Publisher('/message/object_num', Int16, queue_size=1)

        # Declare attributes
        self.person = "pending"
        self.object = "pending"
        self.object_num = -1

        self.load_dictionnary()

        rospy.loginfo("MessageParser init")

        rate = rospy.Rate(1) # 1hz
        while not rospy.is_shutdown():
            self.pubPerson.publish(self.person)
            self.pubObject.publish(self.object)
            self.pubObjectNum.publish(self.object_num)
            rate.sleep()        

        rospy.spin()


    # /message Topic callback
    def message(self, msg):

        if("left" in msg.data.lower()):
            self.person = "left"
        elif("right" in msg.data.lower()):
            self.person = "right"
        else:
            self.person = "undefined"

        num, name = self.match_object(msg.data)

        if( num == 0 ):
            self.object = "undefined"
        else:
            self.object = name

        self.object_num = num


    # check if there is an object name of the ycb dataset is in the /message request
    def match_object(self, smsg):

        match = False
        
        for num, names in self.ycb_number_to_ycb_names.items():
            if( len(names) > 0 ):
                for name in names:
                    if( name.lower() in smsg.lower() ):
                        return num, name
                    if( name.replace('_',' ').lower() in smsg.lower() ):
                        return num, name                        
        
        return 0, "undefined"


    # Load YCB label dictionnary
    def load_dictionnary(self):

        self.ycb_number_to_ycb_names =    \
            {
                1:["chips_can"],
                2:["master_chef_can", "coffee"],
                3:["cracker_box", "Cheez-it"],
                4:["sugar_box"],
                5:["tomato_soup_can"],
                6:["mustard_bottle"],
                7:["tuna_fish_can"],
                8:["pudding_box"],
                9:["gelatin_box"],
                10:["potted_meat_can"],
                11:["banana"],
                12:["strawberry"],
                13:["apple"],
                14:["lemon"],
                15:["peach"],
                16:["pear"],
                17:["orange"],
                18:["plum"],
                19:["pitcher_base"],
                20:[],
                21:["bleach_cleanser"],
                22:["windex_bottle"],
                23:["wine_glass"],
                24:["bowl"],
                25:["mug"],
                26:["sponge"],
                27:["skillet"],
                28:["skillet_lid"],
                29:["plate"],
                30:["fork"],
                31:["spoon"],
                32:["knife"],
                33:["spatula"],
                34:[],
                35:["power_drill"],
                36:["wood_block"],
                37:["scissors"],
                38:["padlock"],
                39:["key"],
                40:["large_marker"],
                41:["small_marker"],
                42:["adjustable_wrench"],
                43:["phillips_screwdriver"],
                44:["flat_screwdriver"],
                45:[],
                46:["plastic_bolt"],
                47:["plastic_nut"],
                48:["hammer"],
                49:["small_clamp"],
                50:["medium_clamp"],
                51:["large_clamp"],
                52:["extra_large_clamp"],
                53:["mini_soccer_ball"],
                54:["softball"],
                55:["baseball"],
                56:["tennis_ball"],
                57:["racquetball"],
                58:["golf_ball"],
                59:["chain"],
                60:[],
                61:["foam_brick"],
                62:["dice"],
                63:["marbles", "a_marbles", "b_marbles", "c_marbles", "d_marbles", "e_marbles", "f_marbles"],
                62:[],
                63:[],
                64:[],
                65:["cups", "a_cups", "b_cups", "c_cups", "d_cups", "e_cups","f_cups","g_cups","h_cups","i_cups","j_cups"],
                66:[],
                67:[],
                68:[],
                69:[],
                70:["colored_wood_blocks", "a_colored_wood_blocks", "b_colored_wood_blocks"],
                71:["nine_hole_peg_test"],
                72:["toy_airplane", "a_toy_airplane", "b_toy_airplane", "c_toy_airplane", "d_toy_airplane", "e_toy_airplane", "f_toy_airplane", "g_toy_airplane", "h_toy_airplane", "i_toy_airplane","j_toy_airplane", "k_toy_airplane"],
                73:["a_lego_duplo","b_lego_duplo", "c_lego_duplo", "d_lego_duplo", "e_lego_duplo", "f_lego_duplo", "g_lego_duplo", "h_lego_duplo", "i_lego_duplo", "j_lego_duplo", "k_lego_duplo", "l_lego_duplo", "m_lego_duplo"],
                74:[],
                75:[],
                76:["timer"],
                77:["rubiks_cube"]
            }






if __name__ == '__main__':
    mp = MessageParser()