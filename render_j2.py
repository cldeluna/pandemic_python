#!/usr/bin/python -tt
# Project: pandemic_python
# Filename: render_j2.py
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/29/21"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse
import os
import datetime
import jinja2


def render_j2template(cfg, j2_template, debug=False):
    """
    Basic Jinja2 Function to render a Jinja2 Template using data in cfg which should be a dictionary
    :param cfg: Dictionary of data
    :param j2_template: Template to use (assumed to be in a subfolder called templates
    :param debug: Boolean to enable or disable print statements for debugging
    :return: rendered configuration in string rendered
    """

    ##############################################
    ### Render the Jinja2 Template with the values
    ##############################################

    cwd = os.path.dirname(os.path.realpath(__file__))
    j2envpath = os.path.join(cwd)
    template_dir_full_path = os.path.join(j2envpath, './templates')
    if debug: print(f"j2envpath: {j2envpath}")
    if debug: print(f"template_full_path: {template_dir_full_path}")
    if debug: print(f"j2_template: {j2_template}")

    J2ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir_full_path))

    template = J2ENV.get_template(j2_template)
    dattim = format(datetime.datetime.now())

    # Its important to note that the Jinja2 template refers to the cfg data structure by that name, cfg
    # A dictionary is expected
    rendered = template.render(dattim=dattim, cfg=cfg, template=j2_template)
    if debug: print(rendered)

    return rendered

def save_file(fn, text):
    """
    Basic function to save text in text to a file of name fn
    :param fn: Filename
    :param text: String of text to save
    :return: fn
    """
    with open(fn, 'w') as f:
        f.write(text)

    return fn


def main():
    """
    Example of generating configlets with Jinja2
    :return:
    """

    # Ecample dictionary of data to use in a Jinja2 template
    cfg = {
        "host": "switch01",
        "no_vlan": [100, 101, 200, 201, 300, 301],
        "new_vlans": [
            {"500": "New Vlan 500"},
            {"600": "New Vlan 600"},
            {"700": "NewvVlan 700"},
        ]
    }

    # Define the template to use for rendering
    template = "vlan_updates.j2"

    # Send the template and the cfg data structure to the render function
    rendered = render_j2template(cfg, template, debug=True)

    # Create a filename based on the hostname so the configlet can be saved
    filename = f"{cfg['host']}_cfglet.txt"
    # Save to file
    save_file(filename, rendered)

    print(f"\nConfiguration file saved to {filename}\n")


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python render_j2.py' ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',
                        default=False)
    arguments = parser.parse_args()
    main()
