#!/usr/bin/env python3
"""Script to initialize YOLOv3"""
import tensorflow.keras as K
import numpy as np


class Yolo():
    """
    Class YOLOv3
    """
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """
        Method init for Yolov3
        Args:
            model_path: path to where a Darknet Keras model is stored
            classes_path: path to where the list of class names used for
                          the Darknet model, listed in order of index,
                          can be found
            class_t: the box score threshold for the initial filtering step
            nms_t: the IOU threshold for non-max suppression
            anchors: the anchor boxes
        """
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'r') as f:
            self.class_names = [line.strip() for line in f]
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def sigmoid(self, x):
        """sigmoid function"""
        return 1 / (1 + np.exp(-x))

    def process_outputs(self, outputs, image_size):
        """
        Method containing the predictions from the darknet_model
        Args:
            outputs: list of numpy.ndarrays containing the predictions from
                     the Darknet model for a single image:
                     (grid_height, grid_width, anchor_boxes, 4 + 1 + classes)
            image_size: numpy.ndarray containing the image's original size
                        [image_height, image_width]
        Returns: (boxes, box_confidences, box_class_probs)
        """
        boxes = [pred[:, :, :, 0:4] for pred in outputs]
        for ipred, pred in enumerate(boxes):
            for grid_h in range(pred.shape[0]):
                for grid_w in range(pred.shape[1]):
                    bx = ((self.sigmoid(pred[grid_h,
                                        grid_w, :,
                                        0]) + grid_w) / pred.shape[1])
                    by = ((self.sigmoid(pred[grid_h,
                                        grid_w, :,
                                        1]) + grid_h) / pred.shape[0])
                    anchor_tensor = self.anchors[ipred].astype(float)
                    anchor_tensor[:, 0] *= \
                        np.exp(pred[grid_h, grid_w, :,
                               2]) / self.model.input.shape[1]
                    anchor_tensor[:, 1] *= \
                        np.exp(pred[grid_h, grid_w, :,
                               3]) / self.model.input.shape[2]
                    pred[grid_h, grid_w, :, 0] = \
                        (bx - (anchor_tensor[:, 0] / 2)) * \
                        image_size[1]
                    pred[grid_h, grid_w, :, 1] = \
                        (by - (anchor_tensor[:, 1] / 2)) * \
                        image_size[0]
                    pred[grid_h, grid_w, :, 2] = \
                        (bx + (anchor_tensor[:, 0] / 2)) * \
                        image_size[1]
                    pred[grid_h, grid_w, :, 3] = \
                        (by + (anchor_tensor[:, 1] / 2)) * \
                        image_size[0]

        box_confidences = [self.sigmoid(pred[:, :, :,
                                        4:5]) for pred in outputs]
        box_class_probs = [self.sigmoid(pred[:, :, :,
                                        5:]) for pred in outputs]
        return boxes, box_confidences, box_class_probs

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """
        Method to filter boxes based on class scores
        Args:
            boxes: list of numpy.ndarrays of shape
                   (grid_height, grid_width, anchor_boxes, 4)
            box_confidences: list of numpy.ndarrays of shape
                             (grid_height, grid_width, anchor_boxes, 1)
            box_class_probs: list of numpy.ndarrays of shape
                             (grid_height, grid_width, anchor_boxes, classes)
        Returns:
            (filtered_boxes, box_classes, box_scores)
        """
        all_boxes = []
        all_classes = []
        all_scores = []

        for boxes_i, confidences_i, probs_i in zip(boxes,
                                                    box_confidences,
                                                    box_class_probs):
            box_scores = confidences_i * probs_i
            box_classes = np.argmax(box_scores, axis=-1)
            box_class_scores = np.max(box_scores, axis=-1)
            mask = box_class_scores >= self.class_t
            all_boxes.append(boxes_i[mask])
            all_classes.append(box_classes[mask])
            all_scores.append(box_class_scores[mask])

        filtered_boxes = np.concatenate(all_boxes, axis=0)
        box_classes = np.concatenate(all_classes, axis=0)
        box_scores = np.concatenate(all_scores, axis=0)

        return filtered_boxes, box_classes, box_scores
