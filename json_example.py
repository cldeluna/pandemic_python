#!/usr/bin/python -tt
# Project: scripting_4_neteng
# Filename: json_example.py
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "3/23/20"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse
import json


def load_data(key):

    data_dict = {'shvlan': """
        {
          "ins_api": {
            "type": "cli_show",
            "version": "1.0",
            "sid": "eoc",
            "outputs": {
              "output": {
                "input": "show vlan",
                "msg": "Success",
                "code": "200",
                "body": {
                  "TABLE_vlanbrief": {
                    "ROW_vlanbrief": [
                      {
                        "vlanshowbr-vlanid": "1",
                        "vlanshowbr-vlanid-utf": "1",
                        "vlanshowbr-vlanname": "default",
                        "vlanshowbr-vlanstate": "active",
                        "vlanshowbr-shutstate": "noshutdown",
                        "vlanshowplist-ifidx": [
                          "Ethernet1/3,Ethernet1/4,Ethernet1/6,Ethernet1/7,Ethernet1/8,Ethernet1/9,Ethernet1/10,Ethernet1/11,Ethernet1/12,Ethernet1/13,Ethernet1/14,Ethernet1/15,Ethernet1/16,Ethernet1/17,Ethernet1/18,Ethernet1/19,Ethernet1/20,Ethernet1/21,Ethernet1/22,Ethernet1/23,Ethernet1/24,Ethernet1/25,Ethernet1/26,Ethernet1/27,Ethernet1/28,Ethernet1/29,Ethernet1/30,Ethernet1/31,Ethernet1/32,Ethernet1/33,Ethernet1/34,Ethernet1/35,Ethernet1/36,Ethernet1/37,Ethernet1/38,Ethernet1/39,Ethernet1/40,Ethernet1/41,Ethernet1/42,Ethernet1/43,Ethernet1/44,Ethernet1/45,Ethernet1/46,Ethernet1/47,Ethernet1/48,Ethernet1/49,Ethernet1/50,Ethernet1/51,Ethernet1/52,Ethernet1/53,Ethernet1/54,Ethernet1/55,Ethernet1/56,Ethernet1/57,Ethernet1/58,Ethernet1/59,Ethernet1/60,Ethernet1/61,Ethernet1/62,Ethernet1/63,Ethernet1/64,Ethernet1/65,Ethernet1/66,Ethernet1/67",
                          "Ethernet1/68,Ethernet1/69,Ethernet1/70,Ethernet1/71,Ethernet1/72,Ethernet1/73,Ethernet1/74,Ethernet1/75,Ethernet1/76,Ethernet1/77,Ethernet1/78,Ethernet1/79,Ethernet1/80,Ethernet1/81,Ethernet1/82,Ethernet1/83,Ethernet1/84,Ethernet1/85,Ethernet1/86,Ethernet1/87,Ethernet1/88,Ethernet1/89,Ethernet1/90,Ethernet1/91,Ethernet1/92,Ethernet1/93,Ethernet1/94,Ethernet1/95,Ethernet1/96,Ethernet1/97,Ethernet1/98,Ethernet1/99,Ethernet1/100,Ethernet1/101,Ethernet1/102,Ethernet1/103,Ethernet1/104,Ethernet1/105,Ethernet1/106,Ethernet1/107,Ethernet1/108,Ethernet1/109,Ethernet1/110,Ethernet1/111,Ethernet1/112,Ethernet1/113,Ethernet1/114,Ethernet1/115,Ethernet1/116,Ethernet1/117,Ethernet1/118,Ethernet1/119,Ethernet1/120,Ethernet1/121,Ethernet1/122,Ethernet1/123,Ethernet1/124,Ethernet1/125,Ethernet1/126,Ethernet1/127,Ethernet1/128"
                        ]
                      },
                      {
                        "vlanshowbr-vlanid": "100",
                        "vlanshowbr-vlanid-utf": "100",
                        "vlanshowbr-vlanname": "XML",
                        "vlanshowbr-vlanstate": "active",
                        "vlanshowbr-shutstate": "noshutdown",
                        "vlanshowplist-ifidx": "port-channel11,Ethernet1/1,Ethernet1/2"
                      },
                      {
                        "vlanshowbr-vlanid": "101",
                        "vlanshowbr-vlanid-utf": "101",
                        "vlanshowbr-vlanname": "LL_VLAN_DEMO1",
                        "vlanshowbr-vlanstate": "active",
                        "vlanshowbr-shutstate": "noshutdown",
                        "vlanshowplist-ifidx": "port-channel11,Ethernet1/1,Ethernet1/2"
                      },
                      {
                        "vlanshowbr-vlanid": "102",
                        "vlanshowbr-vlanid-utf": "102",
                        "vlanshowbr-vlanname": "dev",
                        "vlanshowbr-vlanstate": "active",
                        "vlanshowbr-shutstate": "noshutdown",
                        "vlanshowplist-ifidx": "port-channel11,Ethernet1/1,Ethernet1/2"
                      },
                      {
                        "vlanshowbr-vlanid": "103",
                        "vlanshowbr-vlanid-utf": "103",
                        "vlanshowbr-vlanname": "test",
                        "vlanshowbr-vlanstate": "active",
                        "vlanshowbr-shutstate": "noshutdown",
                        "vlanshowplist-ifidx": "port-channel11,Ethernet1/1,Ethernet1/2"
                      },
                      {
                        "vlanshowbr-vlanid": "104",
                        "vlanshowbr-vlanid-utf": "104",
                        "vlanshowbr-vlanname": "security",
                        "vlanshowbr-vlanstate": "active",
                        "vlanshowbr-shutstate": "noshutdown",
                        "vlanshowplist-ifidx": "port-channel11,Ethernet1/1,Ethernet1/2"
                      },
                      {
                        "vlanshowbr-vlanid": "105",
                        "vlanshowbr-vlanid-utf": "105",
                        "vlanshowbr-vlanname": "iot",
                        "vlanshowbr-vlanstate": "active",
                        "vlanshowbr-shutstate": "noshutdown",
                        "vlanshowplist-ifidx": "port-channel11,Ethernet1/1,Ethernet1/2"
                      }
                    ]
                  },
                  "TABLE_mtuinfo": {
                    "ROW_mtuinfo": [
                      {
                        "vlanshowinfo-vlanid": "1",
                        "vlanshowinfo-media-type": "enet",
                        "vlanshowinfo-vlanmode": "ce-vlan"
                      },
                      {
                        "vlanshowinfo-vlanid": "100",
                        "vlanshowinfo-media-type": "enet",
                        "vlanshowinfo-vlanmode": "ce-vlan"
                      },
                      {
                        "vlanshowinfo-vlanid": "101",
                        "vlanshowinfo-media-type": "enet",
                        "vlanshowinfo-vlanmode": "ce-vlan"
                      },
                      {
                        "vlanshowinfo-vlanid": "102",
                        "vlanshowinfo-media-type": "enet",
                        "vlanshowinfo-vlanmode": "ce-vlan"
                      },
                      {
                        "vlanshowinfo-vlanid": "103",
                        "vlanshowinfo-media-type": "enet",
                        "vlanshowinfo-vlanmode": "ce-vlan"
                      },
                      {
                        "vlanshowinfo-vlanid": "104",
                        "vlanshowinfo-media-type": "enet",
                        "vlanshowinfo-vlanmode": "ce-vlan"
                      },
                      {
                        "vlanshowinfo-vlanid": "105",
                        "vlanshowinfo-media-type": "enet",
                        "vlanshowinfo-vlanmode": "ce-vlan"
                      }
                    ]
                  }
                }
              }
            }
          }
        }
    
    
    
    """
 }

    return data_dict[key]


def main():


    # Simple
    if arguments.simple or arguments.all:
        print("\n====== SIMPLE EXAMPLE")

        person_info = '{"fname": "Travis", "lname": "Bickle", "city": "New York", ' \
                      '"occupation": "Taxi Driver", "age": 34, "friends": ["Iris", "Wizard", "Betsy"]}'
        print(f"\nvariable person_info is of type {type(person_info)} and has value: \n\t{person_info}")
        # print(f"{person_info.keys()}")
        try:
            print(f"Get keys:")
            print(f"{person_info.keys()}")
        except Exception as e:
            print(f"\tERROR!!\n\t{e}")

        person_info_json_obj = json.loads(person_info)
        print(f"\nvariable person_info_json_obj is of type {type(person_info_json_obj)} and has value: \n\t{person_info_json_obj}\n")
        print(f"Get keys:\n\t {person_info_json_obj.keys()}\n")
        print(f"Get Full Name:\n\t {person_info_json_obj['fname']} {person_info_json_obj['lname']} \n")
        print(f"Get Age:\n\t {person_info_json_obj['age']} \n")
        print(f"Get Friends:\n\t {person_info_json_obj['friends']} \n")
        print(f"Get First Friend:\n\t {person_info_json_obj['friends'][0]} \n")

    # Complex Example
    if arguments.complex or arguments.all:
        print("\n====== COMPLEX EXAMPLE")

        data = load_data('shvlan')

        print(f"\ndata variable is of type: {type(data)}")
        print(f"\ndata variable has length: {len(data)}")
        print(f"\ndata variable starts with: {data.strip()[0]}")

        json_data = json.loads(str(data))

        print(f"\njson_data variable is of type: {type(json_data)}")
        print(f"\njson_data variable has length: {len(json_data)}")
        print(f"\njson_data variable has keys: {json_data.keys()}")

        if type(json_data) == dict:
            for key in json_data.keys():
                print(f"Value for key {key}:\n{json_data[key]}")
                print("\nAhhhhhh What the heck is that!!!!\n")
                print(json.dumps(json_data, indent=4))
                print()
                print(f"\njson_data with key {key} has keys: {json_data[key].keys()}\n\n")

        print("============")
        print(json_data['ins_api']['outputs']['output']['body']['TABLE_vlanbrief']['ROW_vlanbrief'])

        print(len(json_data['ins_api']['outputs']['output']['body']['TABLE_vlanbrief']['ROW_vlanbrief'][0]['vlanshowplist-ifidx']))

        for line in json_data['ins_api']['outputs']['output']['body']['TABLE_vlanbrief']['ROW_vlanbrief']:
          print()
          print(line)

        print(len(json_data['ins_api']['outputs']['output']['body']['TABLE_vlanbrief']['ROW_vlanbrief'][0]['vlanshowplist-ifidx']))


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python json_example.py' ")

    #parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true', default=False)
    parser.add_argument('-s', '--simple', help='Execute simple example', action='store_true', default=True)
    parser.add_argument('-c', '--complex', help='Execute complex example', action='store_true', default=False)
    arguments = parser.parse_args()
    main()
