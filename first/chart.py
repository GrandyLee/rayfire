# from pyecharts import Bar,Line,Overlap
# attr = ['A','B','C','D','E','F']
# v1 = [10,20,30,40,50,60]
# v2 = [38,28,35,58,65,70]
# bar = Bar('Line - Bar示例')
# bar.add('bar',attr,v1)
# line = Line()
# line.add('line',attr,v2)
#
# overlop = Overlap()
# overlop.add(bar)
# overlop.add(line)
# overlop.render('./html/line-bar01.html')
#
# from pyecharts import Bar


import pyecharts
# from pyecharts import Bar
#
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.use_theme('dark')                                  #暗色背景色
# bar.add("服装",                                        #注解==label
#         ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"], #横坐标
#         [5, 20, 36, 10, 75, 90])                       #纵坐标
# bar.render('./picture1.html')                          #文件存储路径（默认保存当前文件路径）


# from pyecharts import Map
# value = [155,10,66,78]
# attr = ['太原市','运城市','临汾市','大同市']
# map = Map('山西地图示例',width = 1200,height = 600)
# map.add('',attr,value,maptype = '山西',
#         is_visualmap = True,
#         visual_text_color = '#000',
#         is_label_show = True
#         )
# map.render('./map02.html')

# from pyecharts import Line,EffectScatter,Overlap
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [5,20,36,10,10,90]
# line = Line('线性_闪烁图示例')
# line.add('',attr,v1,is_random = True)
#
# es = EffectScatter()
# es.add('',attr,v1,effect_scale=8)   #闪烁
# overlop = Overlap()
# overlop.add(line)                   #必须先添加line,在添加es
# overlop.add(es)
# overlop.render('G://rayfire/html/line-es01.html')

from pyecharts import Polar
radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("A", [50, 22, 37, 41, 53, 25, 12], radius_data=radius, type='barRadius', is_stack=True)
polar.add("B", [32, 24, 36, 71, 22, 53, 41], radius_data=radius, type='barRadius', is_stack=True)
polar.add("C", [45, 32, 33, 54, 21, 32, 45], radius_data=radius, type='barRadius', is_stack=True)
polar.show_config()
polar.render('G://rayfire/html/polar01.html')
