ls *.las | cut -d. -f1 | xargs -P20 -I{} pdal pipeline -i /path/to/
˓→proj.json --readers.las.filename={}.las --writers.las.
˓→filename=output/{}.laz