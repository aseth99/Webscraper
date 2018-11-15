# accessing attributes: v often we look not for tags but for attributes
# <a href=...> <img src=...>   href attribute contains url, src attribute contains target image
# myTag.attrs, myImgTag.attrs['src'] python dictionary of objects

# lambda expression: fxn taht is into another fxn as a var
# f(x,y)-f(g(x),y) or f(g(x),h(x))

# functions as parameters into findAll, tag objects in boolean out

# soup.findAll(lambda tag: len(tag.attrs)==2)
# 	<div class="body"id="content"></div>
# 	<span style="color:red"class="title"></span>

