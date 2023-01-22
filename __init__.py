import bpy
import bmesh
from . import keymaps


bl_info = {
    "name": "QolTools",
    "author": "Tomi Vartiainen",
    "version": (1, 0, 0),
    "blender": (3, 5, 0),
    "location": "",
    "description": "Quality of life tools",
    "warning": "",
    "doc_url": "",
    "category": "Mesh"
    }

class MESH_OT_mirror(bpy.types.Operator):
    bl_idname = "mesh.mirror"
    bl_label = "mirror operator"
    bl_options = {'REGISTER', 'UNDO'}
    direction: bpy.props.StringProperty( name="direction", default="POSITIVE_X")

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(direction=self.direction)
            bpy.ops.mesh.select_all()
        return {"FINISHED"}

# add classes to a list
classes = [
    MESH_OT_mirror,
]

# register all classes
def register():
    global keymappings
    print("Registered qol_tools")
    for c in classes:
        bpy.utils.register_class(c)
    keymappings = keymaps.register_keymaps()

# unregister all classes
def unregister():
    print("Unregistering classes!")
    for c in classes:
        bpy.utils.unregister_class(c)
    keymaps.unregister_keymaps(keymappings)