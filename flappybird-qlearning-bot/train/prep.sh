for i in `seq -f"%02g" 0 19`; do mkdir $i; done
for i in `seq -f"%02g" 0 19`; do cd $i; ln -s ../../assets .; cd ..; done
for i in `seq -f"%02g" 0 19`; do cd $i; ln -s ../../bot.py .; cd ..; done
for i in `seq -f"%02g" 0 19`; do cd $i; ln -s ../flappy_train.py .; cd ..; done
