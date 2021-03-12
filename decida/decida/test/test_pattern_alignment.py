#!/usr/bin/env python
from __future__ import print_function
from decida.pattern_alignment import pattern_alignment

map32 = "10000010000101011101101011100101110001110001011010011000001001110111111010000001111110001110010010001110000000010000001110100100"
bin32 = "10000010000101011101101011100101110001110001011010011000001001110111111010000001111110001110010010001110000000010000001110100100"
map16 =  "100000100001010111011010111001011100011100010110100110000010011101111110100000011111100011100100"
map8  = "001000000000010100110110001110011011000101000101101001100100100111011111101000000011111011111001"
map4  = "100000100001010111011010111001011100011100010110100110000010011101111110100000011111100011100100"
map2  = "011011010111001010000010000101010100110010010011110001110001011001111100111100100111111010000001"

print("errors: aligned-patterns:")
pats = [map32, bin32, map16, map8, map4, map2]
for ab in pattern_alignment(pats) :
    print("%2d %s" % (ab[1], ab[0]))