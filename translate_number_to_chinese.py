# -*- coding: utf-8 -*-

CHINESE_NEGATIVE = '负'
CHINESE_ZERO = '零'
CHINESE_DIGITS = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
CHINESE_UNITS = ['', '十', '百', '千']
CHINESE_GROUP_UNITS = ['', '万', '亿', '兆']


def _enumerate_digits(number):
	"""
	:type number: int|long
	:rtype: collections.Iterable[int, int]
	"""
	position = 0
	while number > 0:
		digit = number % 10
		number //= 10
		yield position, digit
		position += 1


def translate_number_to_chinese(number):
	"""
	:type number: int|long
	:rtype: string
	"""
	# 判断是否为整数
	if not isinstance(number, int) and not isinstance(number, long):
		raise ValueError('必须输入一个整数！！！')

	# 判断是否为零
	if number == 0:
		return CHINESE_ZERO
	words = []

	# 判断是否小于零
	if number < 0:
		words.append(CHINESE_NEGATIVE)
		number = -number

	# Begin core loop.
	# Version 0.2
	group_is_zero = True
	need_zero = False
	for position, digit in reversed(list(_enumerate_digits(number))):
		unit = position % len(CHINESE_UNITS)
		group = position // len(CHINESE_UNITS)

		if digit != 0:
			if need_zero:
				words.append(CHINESE_ZERO)

			words.append(CHINESE_DIGITS[digit])
			words.append(CHINESE_UNITS[unit])

		group_is_zero = group_is_zero and digit == 0

		if unit == 0:
			words.append(CHINESE_GROUP_UNITS[group])

		need_zero = (digit == 0 and (unit != 0 or group_is_zero))

		if unit == 0:
			group_is_zero = True

	# End core loop.
	return ''.join(words)


if __name__ == '__main__':
	print(translate_number_to_chinese(520647))