if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/harigih/THOR-V3.git /THOR-V3
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /THOR-V3
fi
cd /LUCIFER
pip3 install -U -r requirements.txt
echo "𝐓𝐇𝐎𝐑-𝐕𝟑 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐁𝐨𝐭⚡...."
python3 bot.py
