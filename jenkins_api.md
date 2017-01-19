# Jenkins Api Example
使用[python-jenkins](http://python-jenkins.readthedocs.io/en/latest/)
使用前先进行安装:```pip install python-jenkins```


## 登录jenkins

为了安全起见,

## 插件操作

http://192.168.56.102:32769/pluginManager/api/xml?depth=3
或
http://192.168.56.102:32769/pluginManager/api/json?depth=3

安装插件:
http://stackoverflow.com/questions/9765728/how-to-install-plugins-in-jenkins-with-the-help-of-jenkins-remote-access-api

官方文档说明:
http://192.168.56.102:32769/pluginManager/api/

Whereas prevalidateConfig call runs without any side-effect, you can also submit the same XML to installNecessaryPlugins endpoint to install missing plugins and updating old ones. This calls returns immediately after initiating plugin installation process, without waiting for the completion of those.
