listen=YES
listen_ipv6=NO
background=NO

# --- Vulnérabilité 1 : FTP anonyme mal configuré (voir documentation) ---
anonymous_enable=YES
anon_root=/srv/ftp
no_anon_password=YES
hide_ids=YES
anon_mkdir_write_enable=NO
anon_upload_enable=NO

local_enable=NO
write_enable=NO
dirmessage_enable=YES

xferlog_enable=YES
xferlog_std_format=NO
log_ftp_protocol=YES
vsftpd_log_file=/var/log/vsftpd/vsftpd.log
dual_log_enable=YES

pasv_enable=YES
pasv_min_port=21100
pasv_max_port=21110
pasv_address=${PASV_ADDRESS}
seccomp_sandbox=NO
