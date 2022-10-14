if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/harigih/THOR-V3.git /THOR-V3
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /THOR-V3
fi
cd /THOR-V3
pip3 install -U -r requirements.txt
echo "THOR-V3 starting⚡...."
python3 bot.py
