# coding=utf-8
import cv2
import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn
import numpy as np
from PIL import Image, ImageFont, ImageDraw


from ..scripts.load_config import PROJECT_APP_DIR
# 创建模型对象并加载保存的参数
model = torchvision.models.resnet18(pretrained=False)
num_classes = 4
model.fc = nn.Linear(model.fc.in_features, num_classes)

state_dict = torch.load(PROJECT_APP_DIR / "vision" / 'plant_classifier_new4.7.pth', map_location=torch.device('cpu'))

# 修正键的名称
new_state_dict = {}
for key in state_dict.keys():
    if key.startswith('fc.1'):
        new_key = key.replace('fc.1', 'fc')
    else:
        new_key = key.replace('fc.weight', 'fc.0.weight').replace('fc.bias', 'fc.0.bias')
    new_state_dict[new_key] = state_dict[key]

# 加载修正后的state_dict
model.load_state_dict(new_state_dict)

model.eval()
# 数据预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def get_label(class_index):
    if class_index == 0:
        return "番茄叶斑病"
    elif class_index == 1:
        return "苹果锈病"
    elif class_index == 2:
        return "苹果黑星病"
    elif class_index == 3:
        return "葡萄黑腐病"
    else:
        return "未知"


def analyze_video(video_path, output_path):
    """
    将待识别视频经过处理后输出到指定目录下
    :param video_path: 需要识别的视频
    :param output_path: 结果视频输出目录
    :return: None
    """
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建视频编写器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, 30.0, (frame_width, frame_height))

    # 字体文件路径
    font_path = PROJECT_APP_DIR / "vision" / 'SimHei.ttf'  # 替换为支持中文字符的字体文件路径

    # 加载字体文件
    font = ImageFont.truetype(font_path.__str__(), size=20)
    font_face = cv2.FONT_HERSHEY_COMPLEX

    for frame_index in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        # 对帧图像进行预处理
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame)
        frame_tensor = transform(frame_pil)
        frame_tensor = frame_tensor.unsqueeze(0)

        # 使用模型进行推理
        with torch.no_grad():
            outputs = model(frame_tensor)
            _, predicted = torch.max(outputs.data, 1)

        # 获取预测结果
        label = get_label(predicted.item())

        # 在帧上绘制文本和矩形框
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)
        draw.text((0, 10), "类别: " + label, font=font, fill=(0, 0, 255))

        # 在这里添加识别框绘制代码
        # 假设您已经获取了矩形框的坐标 (x, y, w, h)
        # 可以使用以下代码来绘制矩形框
        x, y, w, h = 30, 30, 180, 180  # 替换为实际的矩形框坐标
        draw.rectangle([(x, y), (x + w, y + h)], outline=(0, 255, 0), width=2)

        frame = np.array(image)

        # 将帧写入输出视频
        output_video.write(frame)

    cap.release()
    output_video.release()
