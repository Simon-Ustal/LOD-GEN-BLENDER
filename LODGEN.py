bl_info = {
    "name" : "LOD GEN",
    "author" : "Šimon Ustal",
    "version" : (1, 0),
    "blender" : (2, 91 ,1),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Optimize Mesh",
}



import bpy
import math
import os


# Init MyProperties
class MyProperties(bpy.types.PropertyGroup):
    
    my_string : bpy.props.StringProperty(name= "Exported Mesh name")
    
    my_int : bpy.props.IntProperty(name= "Number Of LODS", soft_min= 1, soft_max= 7)
    
    int_of_LOD : bpy.props.IntProperty(name= "LOD Index", soft_min= 1, soft_max= 7)
    
    my_filepath : bpy.props.StringProperty(name= "Filepath")
    
    int_of_LOD_string : bpy.props.StringProperty(name= "LOD")
    
    my_enum : bpy.props.EnumProperty(
        name= "File Format",
        description= "sample text",
        items= [('fbx', ".fbx", ""),
                ('obj', ".obj", ""),
                ('dae', ".dae", "")
        ]
    )
    


   
# Init ObjectCountPanel    
class ObjectCount(bpy.types.Panel):
    bl_label = "Settings to Export"
    bl_idname = "PT_TestPanel2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'LOD Gen'

    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        row = layout.row()
        layout.prop(mytool, "my_string")
        
        row = layout.row()
        layout.prop(mytool, "my_int")
        
        row = layout.row()
        layout.prop(mytool, "my_enum")
        
        row = layout.row()
        layout.prop(mytool, "my_filepath")
        
        row = layout.row()
        row.operator("object.property_example")
        
# Init LODGENPanel 
class LODGENPanel(bpy.types.Panel):
    bl_label = "LOD Gen"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'LOD Gen'
 
    
    
    
    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        
        row = layout.row()
        
        row.label(text = "Select object...", icon = 'OBJECT_DATAMODE')
        
        row = layout.row()
        
        row.prop(obj, "name")
        
            
        
# Export LODs        
class OBJECT_OT_property_example(bpy.types.Operator):
    bl_idname = "object.property_example"
    bl_label = "Export LODS"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        layout = self.layout
        so = bpy.context.active_object
        
        mytool.int_of_LOD = 0
        
        mytool.int_of_LOD_string = str(mytool.int_of_LOD)
        
         
        # FBX
        if mytool.my_enum == 'fbx':
            
            bpy.ops.export_scene.fbx(filepath=mytool.my_filepath+"/"+mytool.my_string+"_LOD"+mytool.int_of_LOD_string+".fbx")
            
            for i in range (0, mytool.my_int):
                    
                    mytool.int_of_LOD += 1
                    
                    mytool.int_of_LOD_string = str(mytool.int_of_LOD) 
                    
                    so.modifiers.new("My Modifier", 'DECIMATE').ratio = 0.5
                    
                    bpy.ops.object.modifier_apply(modifier="My Modifier")
                    
                    bpy.ops.object.select_by_type(type='MESH')
                    
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
                    
                    bpy.ops.export_scene.fbx(filepath=mytool.my_filepath+"/"+mytool.my_string+"_LOD"+mytool.int_of_LOD_string+".fbx") 
                             
            return {'FINISHED'}
        
        #DAE
        if mytool.my_enum == 'dae':
            
            bpy.ops.export_scene.fbx(filepath=mytool.my_filepath+"/"+mytool.my_string+"_LOD"+mytool.int_of_LOD_string+".dae")
            
            for i in range (0, mytool.my_int):
                    
                    mytool.int_of_LOD += 1
                    
                    mytool.int_of_LOD_string = str(mytool.int_of_LOD) 
                    
                    so.modifiers.new("My Modifier", 'DECIMATE').ratio = 0.5
                    
                    bpy.ops.object.modifier_apply(modifier="My Modifier")
                    
                    bpy.ops.object.select_by_type(type='MESH')
                    
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
                    
                    bpy.ops.export_scene.fbx(filepath=mytool.my_filepath+"/"+mytool.my_string+"_LOD"+mytool.int_of_LOD_string+".dae") 
                             
            return {'FINISHED'}
        
        #OBJ
        if mytool.my_enum == 'obj':
            
            bpy.ops.export_scene.obj(filepath=mytool.my_filepath+"/"+mytool.my_string+"_LOD"+mytool.int_of_LOD_string+".obj", check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=False, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
            
            for i in range (0, mytool.my_int):
                    
                    mytool.int_of_LOD += 1
                    
                    mytool.int_of_LOD_string = str(mytool.int_of_LOD) 
                    
                    so.modifiers.new("My Modifier", 'DECIMATE').ratio = 0.5
                    
                    bpy.ops.object.modifier_apply(modifier="My Modifier")
                    
                    bpy.ops.export_scene.obj(filepath=mytool.my_filepath+"/"+mytool.my_string+"_LOD"+mytool.int_of_LOD_string+".obj", check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=False, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO') 
                             
            return {'FINISHED'}
        
        

    
         
# Init Classes             
classes = [MyProperties, ObjectCount, LODGENPanel, OBJECT_OT_property_example]         


 
# Un/Register Objects  
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= MyProperties)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool
 

if __name__ == "__main__":
    register()