keys = {'MIRROR': [{'label': 'Mirror x', 'keymap': 'Mesh', 'idname': 'myscript.mirror_x', 'type': 'X', 'value': 'PRESS', "alt": True, "ctrl":False, "shift": True, "properties":["Direction":"POSITIVE_X"]},
                  {'label': 'Mirror y', 'keymap': 'Mesh', 'idname': 'myscript.mirror_y', 'type': 'Y', 'value': 'PRESS', "alt": True, "ctrl":False, "shift": True,"properties":["Direction":"POSITIVE_X"]},
                  {'label': 'Mirror z', 'keymap': 'Mesh', 'idname': 'myscript.mirror_z', 'type': 'Z', 'value': 'PRESS', "alt": True, "ctrl":False, "shift": True,"properties": ["Direction":"POSITIVE_X"]}
]}

for key in keys["MIRROR"]:
    print(key.get("keymap"))
