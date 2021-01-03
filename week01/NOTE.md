# 学习心得

今天尝试用vscode来写python，感觉很好用。
第一周的作业相对较为简单，logging包使用网络上也有很多的代码，此次作业代码没有用一开始自己写的简单的，后面在网络上找到这部分代码，封装的很全了。后续项目中可以使用这部分代码用于记录日志。

<font style="color:red">整体进度较慢，需要进一步的加强视频学习，以及及时完成作业！</font>


学号
```text
    G20200389070088
```

# GitHub使用

## 关于Fork

将远程仓库复制一份到自己的GitHub仓库。远程仓库的更改不会导致自己Fork过来库的更改，反之亦然。适用于研究优秀的开源项目。

## 关于代码仓库的Https和SSH方式

推荐日常工作中尽量使用SSH的方式。主要是可以避免每次提交代码之后都需要输入用户名和密码。二者主要区别是：
* Https方式：
>
>   需要每次都输入用户名和密码，对于开发场景不适用。虽然可以通过以下命令来避免，但是在windows的下会将密码明文保存在本地，极不安全（MAC系统可以）。
```
    git config --global credential.helper store
```
>
* SSH方式
>
>   在安装完Git之后需要在命令行执行以下的步骤来生成一个SSH密钥，并将密钥中的公钥添加到自己的Git中SSH下。
>
> 生成SSH
```
    ssh-keygen -t rsa -C "2476449618@qq.com"
```
> 检查ssh建立状态

```
    ssh -T [responsities-address]
```
>
> 执行完之后打开生成密钥的路径下将 `.pub` 文件中的内容复制并配置在Github中
>


## 将本地仓库同步到一个已经创建好的Git仓库

* 同步本地仓库到一个已有的远程仓库，并指定分支的名字
```
    git remote add [yourname] [responsities-address]
```

* 检查远程仓库的添加状态

```
    git remote
```



