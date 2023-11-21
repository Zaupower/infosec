#!/bin/bash
#search users 
user_array=($(sudo awk -F':' '$1 !~ /^#/ {print $1}' /etc/shadow))
for user in "${user_array[@]}"; do

    expiration_date=$(sudo chage -l "$user" | awk -F':' '$1 ~ /^Password expires/{ print $2 }')
    # Check if expiration_date is not "never"
	if [ "$expiration_date" != " never" ]; then
		# expire date in seocnds
		expiration_epoch=$(date -d "$expiration_date" "+%s")
		#current date in seconds
		current_date_epoch=$(date +%s)
		# three days in seconds
		three_days_epoch=$((3 * 24 * 60 * 60))
		#Subtract three days 
		exp_date_less_three_days=$((expiration_epoch - three_days_epoch))
		if [ "$expiration_epoch" -le "$current_date_epoch" ]; then
                        echo "password expired: $user"
             	elif [ "$exp_date_less_three_days" -le "$current_date_epoch" ]; then
			reamining_days=$(((current_date_epoch - exp_date_less_three_days)/ (24 * 60 * 60)))
			echo "$reamining_days days for $user to expire"
		fi
	fi 
done

: '
exportar script
sudo cp passmon.sh /usr/local/bin/
dar permissões
sudo chmod +x /usr/local/bin/passmon.sh (agora e possivel correr o script sem especificar o path)
adicionar ao cron
sudo crontab -e
add line
55 23 * * * passmon.sh >> ~/password_notices.log 2>&1 (2>& to add stdin like echo)
para ver o conteúdo do ficheiro password_notices.log 
sudo su 
cd 
cat password_notices.log
'
