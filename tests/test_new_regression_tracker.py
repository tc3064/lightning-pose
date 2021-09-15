import os
import torch
import torchvision.transforms as transforms
import pytest
import pytorch_lightning as pl
import shutil
from pose_est_nets.utils.wrappers import predict_plot_test_epoch
from pose_est_nets.utils.IO import set_or_open_folder, load_object
from typing import Optional
from pose_est_nets.models.regression_tracker import RegressionTracker

# TODO: add more tests as we consolidate datasets
_TORCH_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

_BATCH_SIZE = 12
_HEIGHT = 256  # TODO: should be different numbers?
_WIDTH = 256

resnet_versions = [18, 34, 50, 101, 152]

repres_shape_list = [
    torch.Size([_BATCH_SIZE, 512, 1, 1]),
    torch.Size([_BATCH_SIZE, 512, 1, 1]),
    torch.Size([_BATCH_SIZE, 2048, 1, 1]),
    torch.Size([_BATCH_SIZE, 2048, 1, 1]),
    torch.Size([_BATCH_SIZE, 2048, 1, 1]),
]

num_keypoints = 34

fake_image_batch = torch.rand(
    size=(_BATCH_SIZE, 3, _HEIGHT, _WIDTH), device=_TORCH_DEVICE
)
fake_keypoints = torch.rand(_BATCH_SIZE, num_keypoints, device=_TORCH_DEVICE) * _HEIGHT


def test_forward():
    """loop over different resnet versions and make sure that the
    resulting representation shapes make sense."""

    model = RegressionTracker(resnet_version=50, num_targets=34).to(_TORCH_DEVICE)
    representations = model.get_representations(fake_image_batch)
    assert representations.shape == repres_shape_list[2]
    preds = model(fake_image_batch)
    assert preds.shape == fake_keypoints.shape
