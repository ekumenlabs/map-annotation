Map Annotation Experiments
==========================

Experiments on new map annotation methods using crowd sourcing tools
like Mechanical Turk.

High level procedure
--------------------

We are currently targeting an off-line approach:

1. The robot records a trajectory, saving pairs of photo + pose
   periodically. (using rosbag record)
2. The recording is processed to generate a more processing friendly
   format.
3. We pick some poses randomly or manually. (In our tests the pictures
   were manually filtered to avoid showing undesired images). JPG files
   are generated from these poses.
4. The pictures are served in a web server and a CSV file useful to
   create the HITs in mturk is created.
5. The HITs are manually posted using the generated CSV, in a very simple
   procedure.
6. When the HITs are completed, we manually download the results CSV.
7. Using the results we create a probabilistic grid, containing the
   probability of finding each tag in every tagged cell.
8. We extract a data base which has the most probable location for every
   tag in the map.
10. We serve that information through a web interface, which can send the
    robot to the desired tag.

Scripts
-------

The tools needed for the above described process are:

* `bagfilter.py`: Process the bagfile and generates a pickled list of
  pairs Image+Pose. It can optionally write the JPGs files for a given
  number of poses.
* `mturk_data_creator.py`: Generates the CSV file for mturk. The input
  is the desired JPGs files. It also copies the files to a web server.
* `mturk_data_loader.py`: Takes the mturk results and produces the
  tagged map and the dictionary of tags, most probable pose.
* `dump_to_database.py`: Saves the results into a data base useful for
  the web server.

Visualization scripts:

* `taggedBagViewer.py`: Publishes all the tags assigned to each pose to
  rviz. The tags are showed as a Text Marker per pose.
* `taggedMapViewer.py`: Publishes the tagged map as a MarkerArray. Each
  tag has its own namespace, showing a CubeList per pose. Each pose has
  a different alpha value, indicating the probability of finding the tag
  in that pose.
