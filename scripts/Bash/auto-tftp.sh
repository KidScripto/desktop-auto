#!/bin/bash

# The directory to copy and compress
source_dir="/path/to/dir"

# The target directory for the compressed file
target_dir="/path/to/target/dir"

# the name of the compressed file
target_file="archive.tar.gz"

# The IP address to transfer the file to
ftp_server="ftp.example.com"

# The username to use for FTP
username="USERNAME"

# the password to use for FTP
password="PASSWORD"

# Copy and compress the directory
cp -r $source_dir $target_dir
tar -zcvf $target_dir/$target_file $target_dir

# Transfer the file using FTP
ftp -inv $ftp_server << EOF
user $username $password
put $target_dir/$target_file
bye
EOF

# Delete the compressed file after the FTP transfer is completed
rm $target_dir/$target_file
