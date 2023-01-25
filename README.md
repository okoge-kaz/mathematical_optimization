# 問題解決と意思決定 (Problem Solving and Decision Making)

Tokyo Institute of Technology 2022 4Q
[URL](http://www.ocw.titech.ac.jp/index.php?module=General&action=T0300&GakubuCD=4&GakkaCD=342300&KeiCD=23&KougiCD=202202433&Nendo=2022&lang=JA&vid=03)

## 多目的最適化

$$Minimize f(x) = \{ f_1(x), ..., f_m(x) \}$$
$$x \in X$$

### 完全解

$\forall x \in X$に対して、$f(x) \ge f(x^*), x^* \in X$が成り立つとき、$x^*$を「完全解」と呼ぶ。ここでは、記号$\ge$は$f(x)$のすべての要素について$\ge$であって、かつ、少なくともどれか 1 つについては厳密な不登校関係$>$が成立することを表す。

### パレート解

$\exist x^* $に対し、$f(x^*) \ge f(x)$となるような$x$が存在しないとき、x^*を「パレート解」と呼ぶ。一般にパレート解は複数存在し、パレート解の集合を「パレート最適解集合」と呼ぶ。

### パレート開集合とパレートフロント

![](./img/Screenshot%202023-01-14%20at%2014.28.15.png)

