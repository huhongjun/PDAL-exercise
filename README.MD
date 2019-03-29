# PDAL 使用指南

## 安装PDAL
### 官方指令
    $ conda env remove -n gisse
    $ conda create -n gisse -c conda-forge pdal python-pdal matplotlib -y
    $ conda activate gisse

### 我的安装
    conda create -n pdal3.5 python=3.5
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --set show_channel_urls yes
    conda install -c conda-forge pdal python-pdal

### 测试命令
    pdal info pdal\exercises\translation\interesting.las -p 0
    pdal translate pdal\exercises\translation\interesting.las interesting.txt
    pdal info --metadata pdal\exercises\translation\interesting.las
    pdal pipeline -i pipeline-yupont.json

## 工作记录
### 目录与文件说明
目录或文件|说明
---------|----
workshop|存放点云文件，包括输入、输出
pdal样例.ipynb|
yupont-las.ipynb|
