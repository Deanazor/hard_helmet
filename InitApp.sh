git clone https://github.com/AlexeyAB/darknet

cd darknet/
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/LIBSO=0/LIBSO=1/' Makefile

make

cd data/
find -maxdepth 1 -type f -exec rm -rf {} \;
cd ..

rm -rf cfg/
mkdir cfg

gdown --id 1F8jojUCZUHIcu0ZJD5cWpHbAwIWx651Q
mv ./yolov4-custom.cfg cfg

cd cfg
sed -i 's/batch=64/batch=1/' yolov4-custom.cfg
sed -i 's/subdivisions=16/subdivisions=1/' yolov4-custom.cfg
cd ..

gdown --id 1F3-A0ihiPyLiJ_ItVN8ecwL4CBmSOzZj
gdown --id 1F6KQp8jcLrgmfXZ0Xs-sTBRHMyJ_NvB8
mv ./obj.names data
mv ./obj.data  data

cd ..
mkdir uploads
mkdir uploads

mkdir weights
gdown --id 1FlwerEVNP3sYgI4kAImgcWcUUUKrHT7g
mv ./yolov4-custom_best.weights weights