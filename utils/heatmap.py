from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QPointF

class HeatmapView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.heatmap_pixmap = QGraphicsPixmapItem()
        self.scene.addItem(self.heatmap_pixmap)

        self.scale_factor = 1.0
        self.zoom_increment = 1.25  # Zoom in/out factor
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)  # Allow panning

    def display_heatmap(self, heatmap_image):
        """ Converts OpenCV heatmap to QPixmap and displays it. """
        height, width, channel = heatmap_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(heatmap_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        self.heatmap_pixmap.setPixmap(pixmap)
        self.setSceneRect(self.heatmap_pixmap.boundingRect())

    def mousePressEvent(self, event):
        """ Capture click coordinates and zoom into clicked region. """
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.scenePos()  # PySide6 uses scenePos()
            self.zoom_in(pos)

    def wheelEvent(self, event):
        """ Enable zooming in and out using the mouse wheel. """
        zoom_factor = self.zoom_increment if event.angleDelta().y() > 0 else 1 / self.zoom_increment
        self.scale_factor *= zoom_factor
        self.scale(zoom_factor, zoom_factor)

    def zoom_in(self, pos):
        """ Zoom into the clicked point. """
        self.centerOn(self.mapToScene(pos.toPoint()))
        self.scale(self.zoom_increment, self.zoom_increment)

    def reset_zoom(self):
        """ Reset zoom to default view. """
        self.resetTransform()
        self.scale_factor = 1.0
