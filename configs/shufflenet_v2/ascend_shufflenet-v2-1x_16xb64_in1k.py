_base_ = [
    '../_base_/models/shufflenet_v2_1x.py',
    '../_base_/datasets/ascend_imagenet_bs64_pil_resize.py',
    '../_base_/schedules/imagenet_bs1024_linearlr_bn_nowd.py',
    '../_base_/default_runtime.py'
]
