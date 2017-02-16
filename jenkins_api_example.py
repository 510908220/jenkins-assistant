import jenkins
import xmltodict
server = jenkins.Jenkins('http://192.168.56.102:32769', username='westdoorblowcola',
                         password='ebf8901e193566bc6eb934b8445acc9c')
plugins = server.get_plugins()

print server.get_plugin_info('Ant Plugin')



# 修改job配置

## 打开"触发远程构建"选项，设置"身份验证令牌"
def add_auth_token(job_name,auth_token):
    old_config_xml = server.get_job_config(job_name)
    old_config_dict = xmltodict.parse(old_config_xml)
    old_config_dict['project']["authToken"] = auth_token
    server.reconfig_job(job_name.encode("utf-8"), xmltodict.unparse(old_config_dict, pretty=True))
    
for job in server.get_jobs():
    add_auth_token(job['name'], 'TOKEN_NAME')

  
# 视图操作

## 创建视图
def create_view(view_name):
    view_name = view_name.strip()
    if server.view_exists(view_name):
        server.delete_view(view_name)
    
    view_template_dict = xmltodict.parse(jenkins.EMPTY_VIEW_CONFIG_XML)
    view_template_dict['hudson.model.ListView']['name'] = view_name
    view_template_dict['hudson.model.ListView']['includeRegex'] = view_name
    server.create_view(view_name, xmltodict.unparse(view_template_dict, pretty=True))

