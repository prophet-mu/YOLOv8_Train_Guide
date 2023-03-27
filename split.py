# 将图片和标注数据按比例切分为 训练集和测试集
import shutil
import random
import os
# 数据集路径
image_original_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/images/'
label_original_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/labels/'
# 训练集路径
train_image_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/train/images/'
train_label_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/train/labels/'
# 验证集路径
val_image_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/val/images/'
val_label_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/val/labels/'
# 测试集路径
test_image_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/test/images/'
test_label_path = '/home/prophetmu/m3axpi_model/ultralytics/ultralytics/datasets/rebar/test/labels/'

# 数据集划分比例，训练集75%，验证集15%，测试集15%，按需修改
train_percent = 0.7
val_percent = 0.15
test_percent = 0.1


# 检查文件夹是否存在
def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)

    if not os.path.exists(val_image_path):
        os.makedirs(val_image_path)
    if not os.path.exists(val_label_path):
        os.makedirs(val_label_path)

    if not os.path.exists(test_image_path):
        os.makedirs(test_image_path)
    if not os.path.exists(test_label_path):
        os.makedirs(test_label_path)


def main():
    mkdir()

    total_txt = os.listdir(label_original_path)
    num_txt = len(total_txt)
    list_all_txt = range(num_txt)  # 范围 range(0, num)

    num_train = int(num_txt * train_percent)
    num_val = int(num_txt * val_percent)
    num_test = num_txt - num_train - num_val

    train = random.sample(list_all_txt, num_train)
    # 在全部数据集中取出train
    val_test = [i for i in list_all_txt if not i in train]
    # 再从val_test取出num_val个元素，val_test剩下的元素就是test
    val = random.sample(val_test, num_val)

    print("训练集数目：{}, 验证集数目：{},测试集数目：{}".format(len(train), len(val), len(val_test) - len(val)))
    for i in list_all_txt:
        name = total_txt[i][:-4]

        srcImage = image_original_path + name + '.jpg'
        srcLabel = label_original_path + name + '.txt'

        if i in train:
            dst_train_Image = train_image_path + name + '.jpg'
            dst_train_Label = train_label_path + name + '.txt'
            shutil.copyfile(srcImage, dst_train_Image)
            shutil.copyfile(srcLabel, dst_train_Label)
        elif i in val:
            dst_val_Image = val_image_path + name + '.jpg'
            dst_val_Label = val_label_path + name + '.txt'
            shutil.copyfile(srcImage, dst_val_Image)
            shutil.copyfile(srcLabel, dst_val_Label)
        else:
            dst_test_Image = test_image_path + name + '.jpg'
            dst_test_Label = test_label_path + name + '.txt'
            shutil.copyfile(srcImage, dst_test_Image)
            shutil.copyfile(srcLabel, dst_test_Label)

if __name__ == '__main__':
	main()