import unreal
import json

editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

# prefix mapping

# prefix_mapping = {
#     "Blueprint"     : "BP_",
#     "StaticMesh"    : "SM_",
#     "Material"      : "M_",
#     "SKeletalMesh"  : "SK_",
#     "Texture2D"     : "T_",
# }

with open("D:\\Python3.7.7Project\\prefix_mapping.json", "r") as json_file:
    prefix_mapping = json.laods(json_file.read())

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
counter = 0

for asset in selected_assets:
    # Get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    # get the prefix for the given class
    class_prefix = prefix_mapping(class_name,None)

    if class_prefix is None:
        unreal.log_warning("No mapping for asset {} of type {}".format(asset_name,class_name))
        continue

    if not asset_name.startwith(class_prefix):
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset,new_name)
        counter += 1
        unreal.log("Prefixed {} of type {} with {}".format(asset_name,class_name,class_prefix))
    
    else:
        unreal.log("Asset {} of type {} is already prefixed with{}".format(asset_name,class_name,class_prefix))


unreal.log("Prefixed {} of {} assets".format(counter, num_assets))