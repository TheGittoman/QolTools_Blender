import bpy
import bmesh
from . import keymaps
from .keymaps import keys


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

class qol_tools(bpy.types.Operator):
    bl_idname = "mesh.gol_tools"
    bl_label = "Tool Name"

    def execute(self, context):
        self.context = context
        if context.active_object and context.active_object.mode == "EDIT":
            self.do_stuff()
        return {"FINISHED"}
    
    def do_stuff(self):
        print("this does nothing")

class mirror_x(bpy.types.Operator):
    bl_idname = "mesh.mirror_x"
    bl_label = "mirror x"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(direction="POSITIVE_X")
            bpy.ops.mesh.select_all()
        return {"FINISHED"}

class mirror_y(bpy.types.Operator):
    bl_idname = "mesh.mirror_y"
    bl_label = "mirror y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(direction="POSITIVE_Y")
            bpy.ops.mesh.select_all()
        return {"FINISHED"}

class mirror_z(bpy.types.Operator):
    bl_idname = "mesh.mirror_z"
    bl_label = "mirror z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(direction="POSITIVE_Z")
            bpy.ops.mesh.select_all()
        return {"FINISHED"}

class mirror_nx(bpy.types.Operator):
    bl_idname = "mesh.mirror_nx"
    bl_label = "mirror negative x"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(direction="NEGATIVE_X")
            bpy.ops.mesh.select_all()
        return {"FINISHED"}

class mirror_ny(bpy.types.Operator):
    bl_idname = "mesh.mirror_ny"
    bl_label = "mirror negative y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(direction="NEGATIVE_Y")
            bpy.ops.mesh.select_all()
        return {"FINISHED"}

class mirror_nz(bpy.types.Operator):
    bl_idname = "mesh.mirror_nz"
    bl_label = "mirror negative z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == "EDIT":
            bpy.ops.mesh.select_all(action="DESELECT")
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.symmetrize(direction="NEGATIVE_Z")
            bpy.ops.mesh.select_all()
        return {"FINISHED"}
# add classes to a list
classes = [
    qol_tools,
    mirror_x,
    mirror_y,
    mirror_z,
    mirror_nx,
    mirror_ny,
    mirror_nz,
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