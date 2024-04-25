#!/bin/bash
# The size must be displayed in bytes
curl -s "$1" | wc -c
