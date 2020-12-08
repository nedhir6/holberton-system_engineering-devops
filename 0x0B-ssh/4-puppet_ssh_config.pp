#  to set up client SSH configuration file
exec { 'echo -e "\tPasswordAuthentication no \n \tIdentityFile ~/.ssh/holberton"" > ~.ssh/config':
    provider    => 'shell',
  }
