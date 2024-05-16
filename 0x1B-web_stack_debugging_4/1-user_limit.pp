# Changing the OS configuration so that it's possible to login with the
# user "holberton" and open a file without any error messages

# Increase hard file limit for Holberton user.
exec { 'Increase_hard_file_limit_for_holberton_user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user.
exec { 'Increase_soft_file_limit_for_holberton_user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
