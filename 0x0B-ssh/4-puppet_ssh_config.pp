#  to set up client SSH configuration file
exec { 'echo -e "\tPasswordAuthentication no \n \tIdentityFile ~/.ssh/holberton" >> /etc/ssh/config':
    command     => 'echo -e "\tPasswordAuthentication no \n \tIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
    provider    => 'shell',
  }
