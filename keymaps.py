import bpy

# create keymappings for operators

keys = {'MIRROR': [{'label': 'Mirror x', 'keymap': 'Mesh', 'idname': 'mesh.mirror_x', 'type': 'X', 'value': 'PRESS', "alt": True, "shift": True},
                  {'label': 'Mirror y', 'keymap': 'Mesh', 'idname': 'mesh.mirror_y', 'type': 'S', 'value': 'PRESS', "alt": True, "shift": True},
                  {'label': 'Mirror z', 'keymap': 'Mesh', 'idname': 'mesh.mirror_z', 'type': 'Z', 'value': 'PRESS', "alt": True, "shift": True},
                  {'label': 'Mirror -x', 'keymap': 'Mesh', 'idname': 'mesh.mirror_nx', 'type': 'X', 'value': 'PRESS', "alt": True, "ctrl": True, "shift": True},
                  {'label': 'Mirror -y', 'keymap': 'Mesh', 'idname': 'mesh.mirror_ny', 'type': 'S', 'value': 'PRESS', "alt": True,"ctrl": True, "shift": True},
                  {'label': 'Mirror -z', 'keymap': 'Mesh', 'idname': 'mesh.mirror_nz', 'type': 'Z', 'value': 'PRESS', "alt": True, "ctrl": True, "shift": True}
]}

def register_keymaps():
    print("registering keymaps")
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    keymaps = []

    for mapping in keys['MIRROR']:
        keymap = mapping.get("keymap")
        space_type = mapping.get("space_type", "EMPTY")

        if keymap:
            km = kc.keymaps.new(name=keymap, space_type=space_type)

            if km:
                idname = mapping.get("idname")
                type = mapping.get("type")
                value = mapping.get("value")

                shift = mapping.get("shift", False)
                ctrl = mapping.get("ctrl", False)
                alt = mapping.get("alt", False)

                kmi = km.keymap_items.new(idname, type, value, shift=shift, ctrl=ctrl, alt=alt)

                if kmi:
                    properties = mapping.get("properties")

                    if properties:
                        for name, value in properties:
                            setattr(kmi.properties, name, value)

                    keymaps.append((km, kmi))
    return keymaps

def unregister_keymaps(keymaps):
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)