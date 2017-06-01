# jenkins-assistant
整理`jenkins`一些接口使用. 可以基于`jenkins`来实现更高级自动化功能.


## 功能

| 描述                 | 文件                  |
| ------------------ | ------------------- |
| python-jenkins接口整理 | [api](api.md)       |
| jenkins插件修改打包      | [plugin](plugin.md) |
| 证书(Credentials)    | [credentials](credentials.md)         |



基本上通过接口可以实现全部jenkins的操作. 基于此可以利用jenkins实现很多自己想要的功能,比如:

- 一键为项目添加`pylint`代码检查
- 批量增加`SSh Site`,设置远程机器信息以供job使用.
- 管理job、视图管理等
- 管理Credentials