import jenkins

server = jenkins.Jenkins('http://192.168.56.102:32769', username='westdoorblowcola',
                         password='ebf8901e193566bc6eb934b8445acc9c')
plugins = server.get_plugins()

print server.get_plugin_info('Ant Plugin')