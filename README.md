## 上海市工程训练综合能力竞赛--智能搬运机器人
### group member :
组员|分工
---|---
朱晨涛|机械设计，搬运方式规划
赵瀚云|运动控制(STM32)
黄凯|运动控制(STM32)
魏新鹏|识别，顶层处理(raspberry pi)

### github 使用

> 如果之前未使用过git、github、gitlab等版本控制工具，建议先从github的[官方教程](https://guides.github.com/activities)开始，如果你十分熟悉github那么你完全可以跳过这节，甚至帮助修改这节​​ 

0. 如果是Windows，要在本地使用`git command line tool`，可能要先安装`git bash`，如果是macOS X，那么安装`Xcode`后便可以在终端中使用`git`，如果是linux，那么`git`往往是预先安装好的。因为本人使用的操作系统为macOS catalina，所以下面介绍的命令可能与Windows上有些许不同。

1. `git version` 查看自己的git版本号，主要是检查git是否能够运行。

2. `git clone ssh (or URl)` 将本仓库clone至本地。（你可能需要先`Add SSH Key`到你的账户中，具体见[远程仓库设置](https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416)）

   [![sgYn2T.png](https://s3.ax1x.com/2021/01/19/sgYn2T.png)](https://imgchr.com/i/sgYn2T)

   ssh 和 url 获取方式

3. 一种比较安全的方式是在`branch`中修改，再`merge`回`main`分支。因此大家最好先`git branch <name of branch>`再`git checkout <name of branch>`再在branch中修改。

4. 一些其他操作：`git status`查看仓库状态，`git fetch`从远端获取最新的仓库，`git push`将本地的改动上传到远端仓库。

当然如果你不太熟悉命令行，那么利用github和vscode的的GUI也可以完成这些事。具体参照github的[hello world guide](https://guides.github.com/activities/hello-world/)

