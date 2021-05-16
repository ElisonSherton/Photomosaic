import json
import numpy as np

def get_distance(src_dict, component_dict):
    sR, sG, sB = src_dict["meanR"], src_dict["meanG"], src_dict["meanB"]
    cR, cG, cB = component_dict["meanR"], component_dict["meanG"], component_dict["meanB"]

    dR = sR - cR
    dG = sG - cG
    dB = sB - cB

    d = np.sqrt(dR ** 2 + dG ** 2 + dB ** 2)

    return d

def compute_closest(src_dict):
    with open("../artefacts/photo_stats.json", "r") as f:
        color_dict = json.load(f)
        f.close()
    
    distance_dict = {}
    for k, v in color_dict.items():
        distance_dict[k] = get_distance(src_dict, v)
    
    closest = sorted(distance_dict, key = lambda x: distance_dict[x])[0]

    return closest