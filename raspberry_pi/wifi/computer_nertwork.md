### 网络基础知识
1. 统一资源定位符 URL(Uniform Resource Locator)
   
   > `[协议类型]://[访问资源需要的凭证信息]@[服务器地址]:[端口号]/[资源层级UNIX文件路径][文件名]?[查询]#[片段ID]`
2. 域名 Domain name:由一串用点分隔的名字组成的Internet上某一台计算机或计算机组的名称
3. IP地址:因特网上的每台计算机和其它设备都规定了一个唯一的地址，叫做“IP地址”。
4. DNS(Damain name system):互联网的一项服务，因为IP地址不方便记忆，因此人们设计出域名，并通过DNS将IP地址与域名相互映射。
5. FQDN(Fully Qualified Domain name):
   FQDN = Hostname + Domain name
   >e.g. 一个公司申请了域名`comp.com`，这时候有一台主机名为web，则可以使用`web.comp.com`得到这个主机IP。若还有两台提供邮件和OA服务的主机cmail，oa，则这时候可以用以下FQDN：
   `cmail.comp.com`
   `oa.comp.com`
6. NAT:同个公司，家庭，教师内主机对外通信时，把私有IP转换为公有IP地址。所以你使用百度搜索本机IP查到的IP是公网IP，而通过`设置`，`ifconfig`，`python socket`等得到的是局域网IP，也就是路由器给你分配的IP。
7. Linux/MacOS下 /etc/hosts文件的配置
   `ip fqdn [alias]...`
   第一列为主机ip地址，第二列为主机fqdn地址，第三列以后为别名，可以省略，否则至少要包含hostname
### Python Socket
1. `gethostname()`:获取主机名
   
   >linux下可以`$ hostname`
2. `gethostbyname(host)`:将host转化为IPv4格式的字符串，如果host本身就是一个ipv4格式的字符串，则原值返回。
3. `gethostbyname_ex(host)`:返回一个三元组(hostname,aliaslist,ipaddrlist) 这里：hostname是对应ipaddress的给定的原始主机名。
aliaslist【可能为空】是相同地址可供选择的主机名列表。ipaddrlist是相同主机相同接口对应的ipv4地址列表。
    >The host argument is a string giving a host name or IP number
示例('sjtu-windowsxp.localdomain',['sjtu.windowsxp'],['127.0.1.1'])
4. `gethostbyaddr()`三元组：(hostname,aliaslist,ipaddrlist) 结果和gethostbyname_ex(hostname)一致。支持IPV4和IPV6.
5. [What is Port](https://blog.csdn.net/cto_51/article/details/10086745)
6. [127.0.0.1与localhost与本机IP的区别](https://blog.csdn.net/weixin_36185028/article/details/79855383)
7. [使用shell/python获取hostname/fqdn释疑](https://www.cnblogs.com/fanzhidongyzby/archive/2016/01/24/5154443.html)

