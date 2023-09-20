#!/bin/bash
echo "Image compression"
convert bike_original.jpg -quality 10% bike_compressed.jpg
du -h bike_*

