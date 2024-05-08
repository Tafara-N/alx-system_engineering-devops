# Manifest replaces a line in a file on a server

$edit_file = '/var/www/html/wp-settings.php'

# Editing the line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${edit_file}",
  path    => ['/bin','/usr/bin']
}
