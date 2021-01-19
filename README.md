## 上海市工程训练综合能力竞赛--智能搬运机器人
---
### group member :
组员|分工
---|---
朱晨涛|机械设计，搬运方式规划
赵瀚云|运动控制(STM32)
黄凯|运动控制(STM32)
魏新鹏|识别，顶层处理(raspberry pi)

### 比赛链接
[智能+赛道 命题评分要求](http://www.gcxl.edu.cn/new/index_file2.html)
[第7届工训赛“智能+赛道”评分标准](https://mp.weixin.qq.com/s/R4Q5RDkqcPM0G6eyYqo40w)
### To-Do list
#### raspberry pi
- [ ] 颜色识别
  - [x] demo
  - [ ] 最远距离测试
- [ ] 二维码扫描
  - [x] demo
  - [ ] 距离测试
  - [ ] 偏移角度测试
- [ ] WIFI通信
- [ ] 与STM32间的串口通信
- [ ] LED屏展示
#### STM32
- [ ] 红外循线
- [ ] 陀螺仪
- [ ] 舵机控制
- [ ] 电机控制
---
### github 使用

> 如果之前未使用过git、github、gitlab等版本控制工具，建议先从github的[官方教程](https://guides.github.com/activities)开始，如果你十分熟悉github那么你完全可以跳过这节，甚至帮助修改这节​​ 

0. 如果是Windows，要在本地使用`git command line tool`，可能要先安装`git bash`，如果是macOS X，那么安装`Xcode`后便可以在终端中使用`git`，如果是linux，那么`git`往往是预先安装好的。因为本人使用的操作系统为macOS catalina，所以下面介绍的命令可能与Windows上有些许不同。

1. `git version` 查看自己的git版本号，主要是检查git是否能够运行。

2. `git clone ssh (or URl)` 将本仓库clone至本地。（你可能需要先`Add SSH Key`到你的账户中，具体见[远程仓库设置](https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416)）

   <img src="https://s3.ax1x.com/2021/01/19/sgYn2T.png" style="zoom:30%">

   ssh 和 url 获取方式

3. 一种比较安全的方式是在`branch`中修改，再`merge`回`main`分支。因此大家最好先`git branch <name of branch>`再`git checkout <name of branch>`再在branch中修改。

4. 一些其他操作：`git status`查看仓库状态，`git fetch`从远端获取最新的仓库，`git push`将本地的改动上传到远端仓库。

当然如果你不太熟悉命令行，那么利用github和vscode的的GUI也可以完成这些事。具体参照github的[hello world guide](https://guides.github.com/activities/hello-world/)

#### vscode&github: 
0. 用vscode打开一个git的仓库。（它可以来自本地的git init或是远程git clone的）
1. 比如我对某个文件做了一点修改，那么当我保存后。在这会提示现有的更改。
   <img src="https://s3.ax1x.com/2021/01/19/sgDNW9.png" style="zoom:30%">
2. 点击 + 号，会将更改加入暂存区。（也就是git add的效果）
   <img src="https://s3.ax1x.com/2021/01/19/sgrY0f.png" style="zoom:30%">
3. 在上图中的`消息`框中输入对暂存修改的解释，再点击 :white_check_mark:，则完成了一次commit，及类似与commit -m "explanation"
4. 最后，在vscode的左下角可以看到 `0 ↓ 1 ↑`这意味着，远端有 0 个commit需要pull，本地有 1 个commit可以push，此时单击一下那个像旋转一样的键就可以完成`git push`
   <img src="https://s3.ax1x.com/2021/01/19/sgcLqI.png" style="zoom:30%">
#### git tutorial

1. [Missing semester of your CS education](https://missing.csail.mit.edu)

   MIT的一门课，讲了一些常用的工具的使用，比如shell、vim等，git是其中一节，B站上也有课程视频。

2. [Git-scm.com](https://git-scm.com)

   Git的官网，里面有documention，有十分详细的资料

3. [廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/896043488029600)

   比较浅显易懂，跟着做一遍基本的命令就差不多都知道了

