# 文件功能
* **video2img.py** 自动转图片
* **test_and_split.py** 自动划分数据集
* **video** 目录下放拍摄的视频
* **img** 目录下放图片
* **ann** 目录下放置标签
# 准备工作
1. 将拍摄的视频放在video
2. 运行脚本得到图片
3. 启动labellimg标记数据（下面介绍使用方法）

    如果有图片也可以直接启动进行标记
4. 标记完后看情况是否需要转换格式
5. 运行脚本划分数据集
6. 上传服务器，更改配置文件开始训练


# labelImg 教程
在纯英文路径下打开labelImg.exe

* 点Opendir 选img文件夹
* 点 Change save dir 选ann文件夹
* 点Fit Window 放大图片
* 点view -> auto save

按w框物体
按d下一个
按a上一个
选中框按del删除

注意：（要框与物体相切，刚好包含，别打错标签，图片里什么都没有就直接下一张就行了）
