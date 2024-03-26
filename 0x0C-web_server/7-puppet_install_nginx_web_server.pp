# Adding a stable version of nginx

exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Updating software packages
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Installing nginx
package { 'nginx':
  ensure     => 'installed',
}

# Allowing HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# Changing folder permissions
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Create an index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Creates an index file
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Adding redirection and an error page
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }

        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/ permanent;
        }
}
",
}
# Restarts Nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# Starts service Nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
