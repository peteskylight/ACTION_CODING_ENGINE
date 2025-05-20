# heatmap_generator.py

import numpy as np
import cv2

class HeatmapGenerator:
    def __init__(self, base_image, heatmap_shape, opacity=0.4, radius=30):
        self.base_image = cv2.resize(base_image, (heatmap_shape[1], heatmap_shape[0]))
        self.heatmap_shape = heatmap_shape
        self.opacity = opacity
        self.radius = radius
        self.accumulator = np.zeros(heatmap_shape, dtype=np.float32)
        self.blob = self._create_gaussian_blob()

    def _create_gaussian_blob(self):
        size = self.radius * 2
        x = np.linspace(-1, 1, size)
        y = np.linspace(-1, 1, size)
        x, y = np.meshgrid(x, y)
        d = np.sqrt(x**2 + y**2)
        sigma = 0.5
        g = np.exp(-(d**2 / (2.0 * sigma**2)))
        return (g / np.max(g)).astype(np.float32)

    def add_point(self, x, y):
        h, w = self.heatmap_shape
        x, y = int(x), int(y)
        if not (0 <= x < w and 0 <= y < h):
            return
        r = self.radius
        top, bottom = max(0, y - r), min(h, y + r)
        left, right = max(0, x - r), min(w, x + r)
        blob_top, blob_left = r - (y - top), r - (x - left)
        blob_bottom = blob_top + (bottom - top)
        blob_right = blob_left + (right - left)
        self.accumulator[top:bottom, left:right] += self.blob[blob_top:blob_bottom, blob_left:blob_right]

    def get_overlay(self):
        norm = np.clip(self.accumulator / np.max(self.accumulator + 1e-5), 0, 1)
        heatmap_color = cv2.applyColorMap((norm * 255).astype(np.uint8), cv2.COLORMAP_JET)
        return cv2.addWeighted(self.base_image, 1 - self.opacity, heatmap_color, self.opacity, 0)

    def reset(self):
        self.accumulator.fill(0)
