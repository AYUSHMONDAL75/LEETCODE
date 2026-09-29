class Solution(object):
  def reverseBits(self, n):
    binary_str = bin(n)[2:].zfill(32)
    return int(binary_str[::-1], 2)