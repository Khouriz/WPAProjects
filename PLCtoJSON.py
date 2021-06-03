##############################################################################
#This project is going to be used by Wonderful: Pistachios and Almonds to
#for R&D purposes. It is not to be cloned unless by authorized parties.
#This is to test python capabilities to communicate to PLC through an OCP-UA
#Protocol. Then converting them to a .json format and outputting the data
#using an MQTT Protocol to communicate with AWS
#Author: Andrew Zulfa
#Company:Wonderful:Pistachios and Almonds
#Supervisor:Graysen Rowland
#StartDate:06/02/2021
#EndDate:
##############################################################################

#libraries needed(subject to change)
import time
import xmltodict
import json
import sys
from opcua import Client

def main():
    #define variable#

    client = Client("opc.tcp://#insert ip address here#")#may have to be redundant with anaonymous authentification if it comes to it

    #####################

    print(client.application_uri)

    #initial communication#

    try:
        client.connect();#intial ping of to the opcua server

        TagName1 = client.get_node('ns=3;s="storageTempratures"."Temperature1C"')
        TagName2 = client.get_node('#This is for an input similar above to access the info on the client side#')

        #is expandable to however many nodes
        #we need to monitor using possibly a xml to json or values into a single json and sending it out in that fashion

        #below is first method to get values to input into a json file for distribution

        #print(var.get_data_value())
        #Value1 = float(TagName1.get_value())
        #Value2 = float(TagName2.get_value())
        #print("value 1 = " + str(Value1))
        #print("value 2 = " + str(Value2))

        #second method is to test the fethc xml function to use the xml to dict library to convert to dict and then finally dict to json
        
    finally:
        client.disconnect()

    #####################
    
    #initial comunication to json format#

    #####################

    #deletion and output of json file to better save space on the the system that is being run#

    #####################

    print("This is development and will be ready when it is!-Andrew")
    exit
main()
