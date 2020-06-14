def  circle_area_func(pi):
  def circle_area(radius):
    return pi * radius * radius
  
  return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(100))

#１行目：アウター関数定義（円周率）,５行目で半径のみ返す
#２〜３行名：インナー関数定義（半径と円の面積の出し方）
#７、８行目：円周率のパターンを設定
#１０行目：半径の長さを指定して円の面積を出力
