import bpy
import sys

# Doc can be found here: https://docs.blender.org/api/current/bpy.ops.export_scene.html
bpy.ops.export_scene.obj(filepath=sys.argv[-1], check_existing=False, use_selection=False, use_animation=False, use_mesh_modifiers=False,
                        use_edges=False, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=False,
                        use_triangles=True, use_nurbs=False, use_vertex_groups=False, use_blen_objects=False, group_by_object=False, group_by_material=False,
                        keep_vertex_order=True)