import bpy

# create keymappings for operators

keys = {'MIRROR':[{'label': 'Mirror x', 'keymap': 'Mesh', 'idname': 'mesh.mirror', 'type': 'X', 'value': 'PRESS', "alt": True, "shift": True, "properties": [( "direction","POSITIVE_X" )]},
                  {'label': 'Mirror y', 'keymap': 'Mesh', 'idname': 'mesh.mirror', 'type': 'S', 'value': 'PRESS', "alt": True, "shift": True, "properties": [( "direction","POSITIVE_Y" )]},
                  {'label': 'Mirror z', 'keymap': 'Mesh', 'idname': 'mesh.mirror', 'type': 'Z', 'value': 'PRESS', "alt": True, "shift": True, "properties": [( "direction","POSITIVE_Z" )]},
                  {'label': 'Mirror -x', 'keymap': 'Mesh', 'idname': 'mesh.mirror', 'type': 'X', 'value': 'PRESS', "alt": True, "ctrl": True, "shift": True, "properties": [( "direction","NEGATIVE_X" )]},
                  {'label': 'Mirror -y', 'keymap': 'Mesh', 'idname': 'mesh.mirror', 'type': 'S', 'value': 'PRESS', "alt": True,"ctrl": True, "shift": True, "properties": [( "direction","NEGATIVE_Y" )]},
                  {'label': 'Mirror -z', 'keymap': 'Mesh', 'idname': 'mesh.mirror', 'type': 'Z', 'value': 'PRESS', "alt": True, "ctrl": True, "shift": True, "properties": [( "direction","NEGATIVE_Z" )]}
]}

def register_keymaps():
    print("registering keymaps")
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    keymaps = []

    if kc:
        for mapping in keys:
            for v in keys[mapping]:
                keymap = v.get("keymap")
                space_type = v.get("space_type", "EMPTY")

                if keymap:
                    km = kc.keymaps.new(name=keymap, space_type=space_type)

                    if km:
                        idname = v.get("idname")
                        type = v.get("type")
                        value = v.get("value")

                        shift = v.get("shift", False)
                        ctrl = v.get("ctrl", False)
                        alt = v.get("alt", False)

                        kmi = km.keymap_items.new(idname, type, value, shift=shift, ctrl=ctrl, alt=alt)

                        if kmi:
                            properties = v.get("properties")

                            if properties:
                                for name, value in properties:
                                    setattr(kmi.properties, name, value)

                            keymaps.append((km, kmi))
    else:
        print("Cant register keymaps for QolTools")
    return keymaps

def unregister_keymaps(keymaps):
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)