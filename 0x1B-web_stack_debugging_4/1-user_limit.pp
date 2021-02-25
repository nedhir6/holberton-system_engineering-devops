# User limit
exec { 'file change':
provider => shell,
command  => 'sudo echo "fs.file-max = 65536" >> /etc/sysctl.conf',
}
exec { 'apply the limit':
provider => shell,
command  => 'sudo sysctl -p',
}
