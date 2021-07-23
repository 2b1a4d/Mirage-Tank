# 图片隐写术之幻影坦克
一张PNG图在黑色背景与白色背景显示内容的不同实现了两张图的信息存入一张图中
因为该图片的特性与游戏红色警戒中的幻影坦克特性相似，故将该隐写术称为幻影坦克

#Steganography of MirageTank
The difference between the content of a PNG image on a black background and a white background realizes that the information of the two images is stored in one image

Because the characteristics of the picture are similar to those of the MirageTank in the game Red Alert, the steganography is called MirageTank

#原理
利用PNG格式图片的透明通道混合公式，将里图与表图混合为一张PNG图，该混合图在黑色背景与白色背景下显示的内容不同

PNG混合公式为 P显示 = P图片 * alpha + P背景 * (1 - alpha)
alpha为透明度

依黑白图下的显示图片可推出混合图片的透明度alpha和像素色彩值

alpha混合 = 1 - P表图 + P里图
P混合 =  P里图 / alpha混合

但在python导入PIL的环境下透明度(alpha)的取值范围为 [0,255] 且为 整数
所以在python中混合图片的透明度alpha和像素色彩值为

alpha混合 = 255 - P表图 + P里图
P混合 =  P里图 * 255 // alpha混合 

#principle
Using the transparent channel mixing formula of the PNG format picture, the inside picture and the table picture are mixed into a PNG picture, and the content of the mixed picture is different on the black background and the white background.

The PNG blending formula is Pixel_display = Pixel_picture * alpha + Pixel_background * (1-alpha)
alpha is transparency

According to the displayed picture under the black and white picture, the transparency alpha and pixel color value of the mixed picture can be derived

alpha_blend = 1 - Pixel_above_image + Piexl_below_image
Pixel_blend = Pixel_below_image / alpha_blend

But in the environment where python imports PIL, the value range of alpha is [0,255] and is an integer
So in python, the transparency alpha and pixel color value of the mixed picture are

alpha_blending = 255 - Pixel_above_image + Piexl_below_image
Pixel_blend = Pixel_below_image * 255 // alpha_blend

