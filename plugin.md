# Jenkins基本使用



##  插件打包

> 有时jenkins里的插件不能满足需求时,可能需要修改插件. 要让jenkins加载我们打包的插件,就需要了解插件是如何打包的.

插件的打包是用`Maven`进行的. 关于`Maven`的安装可以参考官网步:[install](http://maven.apache.org/install.html),我是在windows下装的,步骤为:

1. 下载[Maven](http://maven.apache.org/download.cgi)
2. 解压下载的压缩包,并将`bin`目录配置到环境变量`Path`下.
3. 安装`jdk`, 创建用户环境变量`JAVA_HOME`,值为`jdk`安装目录(注意不是bin目录)
4. 执行`mvn -v`确认安装是否成功.

然后下载要修改的插件或者自己编写的插件,插件个税为`jenkins`规定的格式. 如下我要修改[**ssh-plugin**](https://github.com/jenkinsci/ssh-plugin):

1. 下载最新版的插件:https://github.com/jenkinsci/ssh-plugin/releases/tag/ssh-2.4

2. 解压,进入目录`ssh-plugin-ssh-2.4`

3. 修改插件, 我这里是增加了一个增加`SSHSite`对象的函数:

   1. 打开文件`ssh-plugin-ssh-2.4\src\main\java\org\jvnet\hudson\plugins\SSHBuildWrapper.java`

   2. 在类`DescriptorImpl`里增加接口:

      ```java
      		public void addSSHSite(final SSHSite sshsite) {
      			sites.add(sshsite);
      		}
      ```

4. 执行`mvn package`,执行完后会在当前目录生成`target`目录, 可以看到目录里有一个`ssh.hpi`文件,这就是jenkins可以识别的插件文件了.

5. 卸载jenkins已经安装的`ssh-plugin`插件, 手动上传新生成的`ssh.hpi`或者将`ssh.hpi`拷贝到`/var/lib/jenkins/plugins`目录,重启jenkins(`service jenkins restart`)



## 参考

[programmatically-getting-jenkins-configuration-for-a-plugin](http://stackoverflow.com/questions/29085710/programmatically-getting-jenkins-configuration-for-a-plugin)

[修改ssh plugin就是参考这里的方法](https://github.com/jenkinsci/publish-over-ssh-plugin/blob/master/src/main/java/jenkins/plugins/publish_over_ssh/descriptor/BapSshPublisherPluginDescriptor.java)