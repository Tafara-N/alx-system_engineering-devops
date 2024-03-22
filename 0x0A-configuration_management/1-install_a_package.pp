# A Puppet script to install flask from pip3 and ensures the version is '2.1.0'

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package {'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

