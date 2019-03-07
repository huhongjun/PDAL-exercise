A convenient way to get point cloud data to Python is to use the PDAL Python extension. PDAL uses the concept of pipelines (much like a GDAL VRT for point clouds instead of rasters) to allow users to orchestrate the processing of point cloud data. With the PDAL Python extension, you can read a LAZ file into a Numpy array and then do whatever you need to with it. The easiest way to do all this is with Conda.

Here's what it does

constructs a new environment with Conda

installs pdal, python-pdal, and matplotlib modules

reads a LAZ file over the internet using a PDAL pipeline

plots a histogram of all of the dimensions of the file into a file called histogram.png

Run these commands in your shell environment after installing miniconda to create a new environment.

    $ conda env remove -n gisse

    $ conda create -n gisse -c conda-forge pdal python-pdal matplotlib -y

    $ conda activate gisse

==================================================================================

conda create -n pdal3.5 python=3.5

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes

conda install -c conda-forge pdal python-pdal



测试命令
----------------------------------
pdal info pdal\exercises\translation\interesting.las -p 0
pdal translate pdal\exercises\translation\interesting.las interesting.txt
pdal info --metadata pdal\exercises\translation\interesting.las

pdal pipeline -i pipeline-yupont.json