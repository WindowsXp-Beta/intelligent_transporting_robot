### 树莓派基本使用
#### linux相关
1. root
   1. `sudo su`进入root用户
      `exit`退出root用户
   2. `sudo reboot`重启树莓派
#### 网络相关：
1. 查看ip
    `ifconfig`其中wlan0是无线IP，eth0是网线连接的IP
#### 连接电脑
1. ssh
   连接：`ssh pi@IP`
   For my raspberry pi,the ip is :
   WIFI | IP
   :---:|:---:
   310|192.168.1.106
   sic-guest|172.18.29.248
   SJTU|169.254.230.168

   For the senior's
   WIFI|IP
   :---:|:---:
   sic-guest|172.18.25.201
   退出：`logout` or `exit`
2. 网线直连
   [树莓派+一根网线直连笔记本电脑](https://shumeipai.nxez.com/2013/10/15/raspberry-pi-and-a-network-cable-directly-connected-laptop.html)
3. 远程桌面
#### 安装OPENCV4.5.0记录
1. 参考帖子：
   - [子豪兄教你在树莓派上安装OpenCV](https://www.jianshu.com/p/56929416b4a1)
   - [树莓派4B安装OPENCV4.0](https://www.cnblogs.com/penuel/p/13720029.html)
   - [树莓派交叉编译opencv3.4.1/pycharm安装opencv/实现人脸识别Demo记录](https://blog.csdn.net/simonforfuture/article/details/101716181)
   >最终完成安装的版本CMAKE使用的是
   cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.7 PYTHON_INCLUDE_DIR=/usr/include/python3.7 PYTHON_LIBRARY=/usr/lib/arm-linux-gnueabihf/libpython3.7m.so PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/.local/lib/python3.7/site-packages/numpy/core/include ..
   路径可能有还有点小问题，要自己再改一下
2. 遇到bug
   1. CMAKE报错
   这个问题解决的比较玄学，在`调整了一波文件路径后，比如严格按照帖子的路径设置`就`configuration done`了
   具体的CMAKEERROR.log文件见[安装opencv](/Users/weixinpeng/Desktop/computer_science/安装opencv/3.4.1.2mis.txt)其中有很多报错，但并没有一一解决:sweat::sweat::sweat:
   2. 发现很多人都遇到了这个问题：缺失下述文件
   boostdesc_bgm.i
   boostdesc_bgm_bi.i
   boostdesc_bgm_hd.i
   boostdesc_lbgm.i
   boostdesc_binboost_064.i
   boostdesc_binboost_128.i
   boostdesc_binboost_256.i
   vgg_generated_120.i
   vgg_generated_64.i
   vgg_generated_80.i
   vgg_generated_48.i
   从网上下载后解压至`opencv_contrib/modules/xfeatures2d/src/`
   3. 安装完成后
      ```
      import cv2
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      ModuleNotFoundError: No module named 'cv2'
      ```
      解决方案(参见[树莓派4B安装OPENCV4.0](https://www.cnblogs.com/penuel/p/13720029.html))
      1. 首先查找自己opencv的安装位置，我在安装结束后提示
      `Set runtime path of "/usr/lib/bin/opencv_version" to "/usr/lib/lib"`
      然后果然在`/usr/lib/lib/python3.7/dist-packages/cv2`找到了opencv
      2. 然后将`cv2.cpython-37m-arm-linux-gnueabihf.so`粘贴至`/usr/lib/python3.7`中
      2. 解决
   4. 使用pip install opencv-python快速安装
      具体见[树莓派简易快速安装OpenCV4](https://blog.csdn.net/ling3ye/article/details/106743847)
   5. debug enlightenment:
      using **[bing(International ver)](https://cn.bing.com/?ensearch=1&FORM=BEHPTB)** instead of baidu as it can lead you to some really helpful websites or forums like `github issues`,`stackoverflow` or `stackexchange`