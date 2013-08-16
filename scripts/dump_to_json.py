import sys
import json
from map_annotation import TaggedMap
import tf.transformations


try:
    map_file = sys.argv[1]
    json_file = sys.argv[2]
except IndexError:
    print "USAGE: " + sys.argv[0] + " <map file> <json file>"
    sys.exit(1)

tag_map = TaggedMap.load_map(map_file)
all_tags = tag_map._states

tag_pose = {}

for tag in all_tags:
    x, y, t, _, _, _, = tag_map._get_scatter_points(state=tag, limit=0.3)
    coords = zip(x, y, t)
    quad = tf.transformations.quaternion_from_euler(0, 0, coords[0][2])
    tag_pose[tag] = list(coords[0][:2]) + list(quad)[-2:]

with open(json_file, "w") as output:
    json.dump(tag_pose, output)
