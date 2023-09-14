import bpy


for material in bpy.data.materials:
    
    if material.use_nodes:
        nodes = material.node_tree.nodes
        for node in nodes:
            if node.type == 'TEX_IMAGE':
                image = node.image

                
                if image.packed_file is not None:
                    
                    image.unpack()

print("Texture unpacking complete.")
