# -*- encoding: utf-8 -*-

import jenkins
import xmltodict

server = jenkins.Jenkins('')

script = """
import jenkins.model.*
import org.jvnet.hudson.plugins.*


def inst = Jenkins.getInstance();
def desc = inst.getDescriptor("org.jvnet.hudson.plugins.SSHBuildWrapper");
def sites = desc.sites;

def new_sites = [];
for(site in sites) {
    new_sites.add(site);
}


def new_site = new SSHSite(
"1.1.1.1",
"8888",
"westdoorblowcola",
"66666666",
"/root/a/a/da.data",
"0")

new_sites.add(new_site)

print(desc.getHelpFile())

desc.save()
"""
info = server.run_script(script)
print(info)


# {
# "hostname": "1111111",
# "port": "60",
# "username": "hhhhhhhhhhh",
# "password": "5456464564564",
# "keyfile": "erterter\\werwer.pmh",
# "pty": false,
# "serverAliveInterval": ""
# }







