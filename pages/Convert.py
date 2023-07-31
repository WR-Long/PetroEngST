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

import subprocess
import sys
import streamlit as st

import json

import PetroEng as pe
from PetroEng.convert import UoMdict

UoM = UoMdict()

st.title("PetroEng: Unit Conversion")
fromqty = st.number_input('Input Quantity:')
fromUnit = st.selectbox('Input Units:', UoM['unit'].keys())
toUnit = st.selectbox('Output Units:', UoM['unit'].keys())

st.text('Output Quantity:')
toqty = pe.convert(fromqty, fromUnit, toUnit)
st.text(toqty)
