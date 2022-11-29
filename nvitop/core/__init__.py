# This file is part of nvitop, the interactive NVIDIA-GPU process viewer.
#
# Copyright 2022 Xuehai Pan. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""The core APIs of nvitop."""

from nvitop.core import host, libcuda, libnvml, utils
from nvitop.core.collector import ResourceMetricCollector, collect_in_background, take_snapshots
from nvitop.core.device import (
    CudaDevice,
    CudaMigDevice,
    Device,
    MigDevice,
    PhysicalDevice,
    normalize_cuda_visible_devices,
    parse_cuda_visible_devices,
)
from nvitop.core.libnvml import NVMLError, nvmlCheckReturn
from nvitop.core.process import GpuProcess, HostProcess, command_join
from nvitop.core.utils import *


__all__ = [
    'take_snapshots',
    'collect_in_background',
    'ResourceMetricCollector',
    'libnvml',
    'nvmlCheckReturn',
    'NVMLError',
    'libcuda',
    'Device',
    'PhysicalDevice',
    'MigDevice',
    'CudaDevice',
    'CudaMigDevice',
    'parse_cuda_visible_devices',
    'normalize_cuda_visible_devices',
    'host',
    'HostProcess',
    'GpuProcess',
    'command_join',
]
__all__.extend(utils.__all__)
