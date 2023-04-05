#!/usr/bin/env python
# Copyright 2022-2023 William Long
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

import streamlit as st

st.title('PetroEng: About')

st.markdown('''
This Streamlit App uses the funcitonality of [PetroEng](https://github.com/WR-Long/PetroEng): a python package of functions for pertoleum engineering.

## Modules
Try out the modules in the menut to the left...
- Convert: Unit Conversion using the Energistics Unit of Measure Dictionary V1.0. Useable with numerics, Numpy arrays, or Pandas series and DataFrames.
''')
