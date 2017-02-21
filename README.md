# jenkins-assistant
提供一个管理系统,方便对jenkins的管理.



##  概述

平时使用jenkins作为升级来用. 随着job的增多管理起来比较麻烦. 而且操作远程机器时,每次还得在jenkins ssh相关设置上填一堆秘钥信息等挺麻烦的.

## 目标

- 提供任务模板:可以快速创建job
- 同时修改多个job信息
- 其他

## 技术

| 前端   | vuejs                                    |
| ---- | ---------------------------------------- |
| 后端   | [django-rest-framework](http://www.django-rest-framework.org/) |
| 数据库  | mysql                                    |

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
```错误是由于请求头添加了` u'Jenkins-Crumb:`,导致unicode和str相加(有非ascii就会报错). 一种解决是修改`python-jenkins`代码:
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


## 高级

http://pghalliday.com/jenkins/groovy/sonar/chef/configuration/management/2014/09/21/some-useful-jenkins-groovy-scripts.html