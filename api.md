# Jenkins Api Example
使用[python-jenkins](http://python-jenkins.readthedocs.io/en/latest/)
使用前先进行安装:```pip install python-jenkins```


## 登陆

为了安全起见,  jenkins应该设置登陆密码. 在调用jenkins api最好是别暴露原始密码. 设置过登陆密码后,打开`http://127.0.0.1:8080/user/admin/configure`(admin是用户名),找到`API Token` 可以看到有一个`User ID`和`API Token`,用这作为`jenkins`初始话的账号和密码.

```python
import jenkins
server = jenkins.Jenkins('http://127.0.0.0:8080', username='westdoorblowcola',
                         password='ebf8901e193566bc6eb934b8445acc9c')
```

## 创建视图

```python
def create_view(view_name, cover=True):
    """
    :param view_name: 视图名称
    :param cover: 是否覆盖已有的视图
    :return:
    """
    view_name = view_name.strip()
    if server.view_exists(view_name):
        if not cover:
            return
        server.delete_view(view_name)
    
    view_template_dict = xmltodict.parse(jenkins.EMPTY_VIEW_CONFIG_XML)
    view_template_dict['hudson.model.ListView']['name'] = view_name
    view_template_dict['hudson.model.ListView']['includeRegex'] = view_name + ".*"
    server.create_view(view_name, xmltodict.unparse(view_template_dict, pretty=True))
```

## 身份验证令牌

> 当需要远程触发构建时,需要打开"触发远程构建"选项，设置"身份验证令牌"

```python
def add_auth_token(job_name, auth_token):
    """
    :param job_name: 任务名
    :param auth_token: 令牌
    :return:
    """
    old_config_xml = server.get_job_config(job_name)
    old_config_dict = xmltodict.parse(old_config_xml)
    old_config_dict['project']["authToken"] = auth_token
    server.reconfig_job(job_name.encode("utf-8"), xmltodict.unparse(old_config_dict, pretty=True))
```

## Groovy脚本执行

> 当需要对jenkins进行一些高级控制的时候,api可能无法满足我们的需求.

例子一,修改Git Plugin配置:

```python
script = """
import jenkins.model.*
def inst = Jenkins.getInstance()
def desc = inst.getDescriptor("hudson.plugins.git.GitSCM")
desc.setGlobalConfigName("[name to use with git commits]")
desc.setGlobalConfigEmail("[email to use with git commits]")
desc.save()
"""
info = server.run_script(script)
```

例子二,增加SSHSite:

```python
script = """
import jenkins.model.*
import org.jvnet.hudson.plugins.*
def inst = Jenkins.getInstance();
def desc = inst.getDescriptor("org.jvnet.hudson.plugins.SSHBuildWrapper");
def new_site = new SSHSite(
"1.1.1.1",
"8888",
"westdoorblowcola",
"66666666",
"/root/a/a/da.data",
"0")
desc.addSSHSite(new_site)
desc.save()
"""
info = server.run_script(script)
print(info)
```

注意: `SSh Plugin`默认是没有`addSSHSite`接口的,这个是我自己修改了`SSh Plugin`插件后增加的.详细请看`plugin.md`



## 问题

在使用`python-jenkins`时, 去修改job配置时,会报如下错误:
```
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 322: ordinal not in range(128)
> c:\python27\lib\httplib.py(897)_send_output()
    895
    896         if isinstance(message_body, str):
--> 897             msg += message_body
    898             message_body = None
    899         self.send(msg)
​```错误是由于请求头添加了` u'Jenkins-Crumb:`,导致unicode和str相加(有非ascii就会报错). 一种解决是修改`python-jenkins`代码:
```
    def maybe_add_crumb(self, req):
        # We don't know yet whether we need a crumb
        if self.crumb is None:
            try:
                response = self.jenkins_open(Request(
                    self._build_url(CRUMB_URL)), add_crumb=False)
            except (NotFoundException, EmptyResponseException):
                self.crumb = False
            else:
                self.crumb = json.loads(response)
        if self.crumb:
            req.add_header(self.crumb['crumbRequestField'].encode("utf-8"), self.crumb['crumb'].encode("utf-8"))
  ```
  我这里把unicode给encode了一下.
  ```