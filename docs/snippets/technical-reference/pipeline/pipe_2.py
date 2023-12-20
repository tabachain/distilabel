# Copyright 2023-present, Argilla, Inc.
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

from datasets import load_dataset

instruction_dataset = (
    load_dataset("HuggingFaceH4/instruction-dataset", split="test[:3]")
    .remove_columns(["completion", "meta"])
    .rename_column("prompt", "input")
)

pipe_dataset = pipe.generate(
    instruction_dataset,
    num_generations=2,
    batch_size=1,
    enable_checkpoints=True,
    display_progress_bar=True,
)