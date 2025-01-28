# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:21:59 2025

@author: 18307
"""
import matplotlib.pyplot as plt

from custom_utils import Layers, draw_layer, draw_layers, draw_line, draw_lines

def draw_cnn_2layers_cv_3_mxp_3_glbmp(fontsize=12):
    SimpleCNN = Layers('SimpleCNN', 0, 0, 2, 1.5, 1)
    
    SimpleCNN.add_layer("Input", 'lightgrey'),  
    
    SimpleCNN.add_layer("Conv\n3 x 3 @ 32", '#4682B4'),
    SimpleCNN.add_layer("Max Pooling\n3 x 3", 'lightgreen'),
    
    SimpleCNN.add_layer("Conv\n3 x 3 @ 64", '#4682B4'),
    SimpleCNN.add_layer("Global\nMax Pooling", 'lightgreen'),
    
    SimpleCNN.add_layer("Flatten", '#FF6347'),
    
    SimpleCNN.add_layer("Fully Connected\n 64", 'orange'),
    SimpleCNN.add_layer("Fully Connected\n 32", 'orange'),
    SimpleCNN.add_layer("Fully Connected\n 3", 'orange'),
    
    SimpleCNN.add_layer("Class Output", '#FF6347')
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 4));
    
    draw_layers(ax, SimpleCNN, fontsize=fontsize)
    draw_lines(ax, SimpleCNN)
    
    # Set axis limits and remove axis
    ax.set_xlim(-0.5, 20)
    ax.set_ylim(-0.5, 1.5)
    ax.axis('off')
    
    # Title
    plt.title('Neural Network Architecture Diagram', fontsize=14)
    plt.show()

def draw_mscnn_2layers_cv_357_mxp_3_glbmp(fontsize=10):
    # Branch 0; Main
    SimpleMSRN = Layers('SimpleMSRN', 0, 0, 2, 1.5, 1) # Create an instance of Layers
    SimpleMSRN.add_layer("Input", 'lightgray') 
    SimpleMSRN.add_layer("Conv\n5 x 5 @ 32", '#4682B4')  # 卷积层 - 深蓝色
    SimpleMSRN.add_layer("Max Pooling\n 3 x 3", '#90EE90')  # 池化层 - 浅绿色
    
    SimpleMSRN.add_layer("Conv\n5 x 5 @ 64", '#4682B4')  # 卷积层 - 深蓝色
    SimpleMSRN.add_layer("Global\n Max Pooling", '#90EE90')  # 池化层 - 浅绿色
    
    SimpleMSRN.add_layer("Concat", 'lightblue')  # 特征融合
    SimpleMSRN.add_layer("Flatten", '#FF6347')  # 展平层
    SimpleMSRN.add_layer("Fully\nConnected\n64x3", '#FFA500')  # 全连接层 - 橙色
    SimpleMSRN.add_layer("Fully\nConnected\n128", '#FFA500')  # 全连接层 - 橙色
    SimpleMSRN.add_layer("Fully\nConnected\n3", '#FFA500')  # 全连接层 - 橙色
    
    SimpleMSRN.add_layer("Class Output", '#FF6347')  # 输出层
    
    # Branch 1
    SimpleMSRNs1 = Layers('SimpleMSRNs1', 2, 1.2, 2, 1.5, 1)
    
    SimpleMSRNs1.add_layer("Conv\n3 x 3 @ 32", '#4682B4')  # 卷积层 - 深蓝色
    SimpleMSRNs1.add_layer("Max Pooling\n 3 x 3", '#90EE90')  # 池化层 - 浅绿色
    
    SimpleMSRNs1.add_layer("Conv\n3 x 3 @ 64", '#4682B4')  # 卷积层 - 深蓝色
    SimpleMSRNs1.add_layer("Global\n Max Pooling", '#90EE90')  # 池化层 - 浅绿色
    
    # Branch 2
    SimpleMSRNs2 = Layers('SimpleMSRNs2', 2, -1.2, 2, 1.5, 1)
    
    SimpleMSRNs2.add_layer("Conv\n7 x 7 @ 32", '#4682B4')  # 卷积层 - 深蓝色
    SimpleMSRNs2.add_layer("Max Pooling\n 3 x 3", '#90EE90')  # 池化层 - 浅绿色
    
    SimpleMSRNs2.add_layer("Conv\n7 x 7 @ 64", '#4682B4')  # 卷积层 - 深蓝色
    SimpleMSRNs2.add_layer("Global\n Max Pooling", '#90EE90')  # 池化层 - 浅绿色
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 5))
    
    draw_layers(ax, SimpleMSRN, fontsize=fontsize)
    draw_layers(ax, SimpleMSRNs1, fontsize=fontsize)
    draw_layers(ax, SimpleMSRNs2, fontsize=fontsize)
    
    draw_lines(ax, SimpleMSRN)
    draw_lines(ax, SimpleMSRNs1)
    draw_lines(ax, SimpleMSRNs2)
    
    # Connect branches
    draw_line(ax, [1.5, 2], [0.5, 1.7], 'black')
    draw_line(ax, [1.5, 2], [0.5, -0.7], 'black')
    draw_line(ax, [9.5, 10], [1.7, 0.5], 'black')
    draw_line(ax, [9.5, 10], [-0.7, 0.5], 'black')
    
    # Set axis limits and remove axis
    ax.set_xlim(-0.5, 22)
    ax.set_ylim(-1.5, 2.5)
    ax.axis('off')
    
    # Title
    plt.title('Neural Network Architecture Diagram', fontsize=14)
    plt.show()
    
if __name__ == "__main__":
    draw_cnn_2layers_cv_3_mxp_3_glbmp()
    draw_mscnn_2layers_cv_357_mxp_3_glbmp(fontsize=10)