while True:
	height = input('身長(m)?:')
	if len(height) == 0:
		# Enterが押された場合は、終了
		break
	# 入力は文字列なので、少数に変換
	height = float(height)
	weight = float(input('体重(kg)?:'))
	# 組み込み関数powで累乗計算
	bmi = weight / pow(height, 2)

	#　少数点第一位までの出力にフォーマット
	print('BMI値は、{:.1f}です。'.format(bmi))
	if bmi < 18.5:
		print('少し痩せすぎです。')
	elif 18.5 <= bmi < 25.0:
		print('標準的な体系です。')
	elif 25.0 <= bmi < 30.0:
		print('少し太っています。')
	else:
		print('高度の肥満です。')