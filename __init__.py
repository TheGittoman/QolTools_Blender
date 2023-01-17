import bpy
import bmesh
from . import keymaps
from .keymaps import keys


bl_info = {
    "name": "My Addon",
    "author": "Tomi Vartiainen",
    "version": (1, 0, 0),
    "blender": (3, 5, 0),
    "location": "",
    "description": "Quality of life tools",
    "warning": "",
    "doc_url": "",
    "category": "Mesh"
    }

class qol_tools(bpy.types.Operator):
    bl_idname = "object.gol_tools"
    bl_label = "Tool Name"

    def execute(self, context):
        self.context = context
        if context.active_object and context.active_object.mode == "EDIT":
            self.do_stuff()
        return {"FINISHED"}
    
    def do_stuff(self):
        print("this does nothing")

class MESH_OT_mirror(bpy.types.Operator):
    bl_idname = "mesh.mirror_nx"
    bl_label = "mirror negative x"
    bl_options = {'REGISTER', 'UNDO'}
    direction: bpy.props.StringProperty(
        name="direction",
        description="direction of mirror"
    )

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(self.direction)
            bpy.ops.mesh.select_all()
        return {"FINISHED"}

# add classes to a list
classes = [
    qol_tools,
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