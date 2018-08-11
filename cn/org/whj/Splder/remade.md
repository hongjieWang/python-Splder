# 爬虫简介
- 爬虫定义：网络爬虫（又被成为网络蜘蛛-网络机器人-在FOAF社区中间-更经常的成为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或脚本。
另外一些不常使用的名字还有蚂蚁，自动检索、模拟程序或者蠕虫。
- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤
    - 下载网页
    - 提取正确的信息
    - 根据一定的规则自动跳转的另外的网页上执行两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫
- Python网络包简介
    - Python2.X : urllib,urllib2,urllib3,httplib2,requests
    - Python3.x : urllib,urllib3,httplib2,requests

# 2、urllib使用
- 包含模块
    - urllib.request: 打开和读取URLS
    - urllib.error: 包含urllib.request产生的常见的错误，使用try捕捉
    - urllib.parse: 包含即系URL的方法
    - urllib.robotparse: 解析robots.txt文件
    - 案例 v01
- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是可能有误
    - 需要安装 conda install chardet
    - 案例 v01
- request.data 
    - 访问网页的两种方式
        - get
        - post
            - 一般向服务器传递参数使用post
            - post把信息进行加密
            - 我们如果使用post信息，需要封装data参数
            - 使用post，意味着Http请求头可能需要更改：
                - Content-Type : application/x-www.from-urlencode
                - Content-Length: 数据长度
                - 简而言之，一旦更改请求方式，请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
        - 案例v03
        - 为了更多的设置请求信息，单纯的通过urlopen函数已经不好用了
        - 需要利用request.Request类，模拟请求实体可以通过设置headers进行身份伪装
        - 案例v04

# 3、Error 模块

- urllib.error
    - Urlerror产生的原因：
        - 没网
        - 服务器链接失败
        - 链接不到指定的服务器
        - 是OSError模块
        - 案例v05
    - HttpError,是URLError的一个子类
        - 案例v06
    - 两者区别：
        - httpError 返回是对应的HTTP请求的返回码错误，如果HTTP返回的错误码在400以上，则引发HTTP Error
        - URLError 对应的一般是网络出现问题，包括url问题
        - 关系区别： OS Error-> URLError -> HttpError
        
# 4、UserAgent 身份隐藏
- UserAgent: 用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者身份，
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    
    - 设置UA可以通过两种方式
        - 案例v07
        
# 5、ProxyHandler处理（代理服务器）
- 使用代理IP，是爬虫的常用手段。
- 获取代理服务器的地址：
    - www.xicidaili.com
    - www.goubanjia.com
- 代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多很多
- 基本使用代理步骤：
    - 设置代理地址
    - 创建ProxyHandler
    - 创建Opener
    - 安装Opener
    - 案例v08
# 6、cookie & session
- 由于http协议的无记忆性，人们为了弥补这一缺陷，所采用的一个补充协议
- cookie是发放给用户（即http浏览器）的一段信息，session是保存在服务器上的对应另一半信息，用来记录用户信息
- 区别：
    - 存在位置不同
    - cookie不安全
    - session会保存在服务器上一定时间
    - 单个cookie保存数据不超过4k,很多浏览器限制一个站点最多保存20个
- session存放位置：
    - 存在服务器端，
    - 一般情况下，session是放在内存中或者数据库中
    - 
- 使用cookie登陆
    - 直接把cookie复制下来，然后手动放到请求头中。
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie。
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar（filename,delayload=None,policy=None）：
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar（filename,delayload=None,policy=None）：
            - 创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar（filename,delayload=None,policy=None）：
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 他们的关系是：CookieJar --> FileCookieJar --> MozillaCookieJar & LwpCookieJar
    - 利用cookieJar 访问人人网：v10
        - 自动使用cookie登陆，流程
            - 打开登陆页面后自动通过用户名密码登陆
            - 自动提取反馈回来的cookie
            - 利用提取的cookie登陆隐私页面

- js 加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是取md5值）
    - 经过加密，传输的就是密文，但是加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 破解有道词典 V11