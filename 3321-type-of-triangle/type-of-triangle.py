class Solution(object):

  def triangleType(self, nums):
    """:type nums: List[int]

    :rtype: str
    """
    a, b, c = nums[0], nums[1], nums[2]
    if a + b <= c or a + c <= b or b + c <= a:
      return "none"
    if a == b == c:
      return "equilateral"
    elif a == b or b == c or a == c:
      return "isosceles"
    else:
      return "scalene"