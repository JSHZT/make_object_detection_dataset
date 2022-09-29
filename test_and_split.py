import xml.etree.ElementTree as ET
import os
import random
import shutil

label = ["person"]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    # for name in os.listdir("ann"):
    #     domTree = ET.parse("./ann/" + name)
    #     # 文档根元素
    #     rootNode = domTree.getroot()
    #     for obj in rootNode.iter('object'):
    #         cls_name = obj.find('name').text.strip().lower()
    #         if cls_name not in label:
    #             print("label error, name : " + name)
    #             exit()
                
    print("check pass")
    name_list = []
    for name in os.listdir(BASE_DIR + "/img/"):
        name_list.append(name)
    
    random.shuffle(name_list)
    length = len(name_list)

    split_list = [name_list[:int(length*0.9)], name_list[int(length*0.9):]]
    dir_list = ["train", "test"]

    if os.path.exists(BASE_DIR + "/dataset"):
        shutil.rmtree(BASE_DIR + "/dataset")
    for split in dir_list:
        os.makedirs(BASE_DIR + "/dataset/" + split + "/img")
        os.makedirs(BASE_DIR + "/dataset/" + split + "/ann")

    print("copying")

    
    for i in range(2):
        for name in split_list[i]:
            shutil.copyfile(BASE_DIR + "/img/" + name, BASE_DIR + "/dataset/" + dir_list[i] + "/img/" + name)
            prename = name.split(".")[0]
            if os.path.isfile(BASE_DIR + "/ann/" + prename + ".txt"):
                shutil.copyfile(BASE_DIR + "/ann/" + prename + ".txt", BASE_DIR + "/dataset/" + dir_list[i] + "/ann/" + prename + ".txt")
    

if __name__ == "__main__":
    img = os.listdir(BASE_DIR + "/img")

    for i in range(len(img)):
        img[i] = img[i].split(".")[0]

    for name in os.listdir(BASE_DIR + "/img"):
        if len(name.split(".")) > 2:
            os.remove(BASE_DIR + "/img/" + name)

    for name in os.listdir(BASE_DIR + "/ann"):
        if len(name.split(".")) > 2:
            os.remove(BASE_DIR + "/ann/" + name)

    for file in os.listdir("ann/"):
        if file.split(".")[0] not in img:
            print(file + " remove")
            os.remove("./ann/" + file)
    main()


