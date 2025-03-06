# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:20:39 2025

@author: 18307
"""

import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle

class Layers:
    def __init__(self, name, x_start, y_start, interval, width, height):
        self.name = name

        self.x_start = x_start
        self.y_start = y_start

        self.interval = interval

        self.current_x_start = x_start
        self.current_y_start = y_start

        self.width = width
        self.height = height

        self.layers = []
        self.layer_count = 0

    def add_layer(self, label, color):
        self.layers.append((self.current_x_start, self.y_start, label, color))
        self.current_x_start += self.interval

        self.layer_count += 1

    def print_layers(self):
        for layer in self.layers:
            print(layer)
            
# Function to add layers to the diagram
def draw_layer(ax, x, y, width, height, label, color, fontsize):
    rect = plt.Rectangle((x, y), width, height, edgecolor='black', lw=1.5, facecolor=color)
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, label, ha='center', va='center', fontsize=fontsize, color='black', rotation=90)

def draw_layers(ax, layers, fontsize=10):
  width = layers.width
  height = layers.height

  for layer in layers.layers:
    draw_layer(ax, layer[0], layer[1], width, height, layer[2], layer[3], fontsize)
    
# Function to add lines to the diagram
def draw_line(ax, x, y, color):
  line = plt.Line2D(x, y, color='black')
  ax.add_line(line)

def draw_lines(ax, layers):
  width = layers.width
  height = layers.height

   # print(layers.x_start)

  for i in range(len(layers.layers)-1):
    x1 = layers.interval * i + layers.x_start
    x2 = layers.interval * (i + 1) + layers.x_start
    y1 = layers.y_start
    y2 = layers.y_start

    x_start = x1 + width
    x_end = x2
    y_start = y1 + height / 2
    y_end = y2 + height / 2

    line = plt.Line2D([x_start, x_end], [y_start, y_end], color='black')
    ax.add_line(line)