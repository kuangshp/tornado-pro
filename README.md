### 一、利用`pycharm`新创建一个项目
>注意点,我们用`pycharm`创建一个`django`项目,然后把项目里面的文件夹及文件全部删除

### 二、从之前开发的虚拟空间复制安装包及版本过来
* 1、`pip freeze`

    ```
    Pillow==4.1.1
    PyMySQL==0.7.11
    SQLAlchemy==1.1.9
    argparse==1.2.1
    backports-abc==0.5
    backports.ssl-match-hostname==3.5.0.1
    certifi==2017.4.17
    futures==3.1.1
    olefile==0.44
    pbkdf2==1.3
    pycket==0.3.0
    redis==2.10.5
    singledispatch==3.4.0.3
    six==1.10.0
    tornado==4.5.1
    wsgiref==0.1.2
    ```
    
* 2、在项目文件夹下创建一个`requirements.txt`文件存放上面全部的包

### 三、配置`pycharm`同步到服务器[配置具体步骤](http://blog.csdn.net/kuangshp128/article/details/73867447)

### 四、同步文件安装全部的包`pip install -r requirements.txt`并查看安装情况