test="ip_change"
if [[ "$test" ]];
then
  while sleep 10
  do
  ipconfig /flushdns
  ipconfig /release
  ipconfig /renew
  echo -e "\033[1;92m changed"
  done
else
    echo -e "\033[1;91m error"
fi