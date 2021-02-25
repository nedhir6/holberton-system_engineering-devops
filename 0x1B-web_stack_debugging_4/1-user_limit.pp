# User limit
exec {'UserLimit':
  command => 'sed -i "s/nofile 5/no file 4096/; s/nofile 4/nofile 1024/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin'],
}
