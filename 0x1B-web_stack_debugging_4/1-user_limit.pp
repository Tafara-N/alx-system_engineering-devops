# Changing the OS configuration so that it's possible to login with the
# user "holberton" and open a file without any error messages

exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
