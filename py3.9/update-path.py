#!/usr/bin/env python
# coding: utf-8
import os, sys
PATH = os.pathsep.join(p for p in os.environ["PATH"].split(":") if p and "3.10" not in p)
print(PATH)

