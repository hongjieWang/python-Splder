# XPath
- 在XML文件中查找信息的一套规则／语言，根据XML的的元素或属性进行遍历
# XPath 开发工具
- 开源的XPath 表达式工具：XMLQuire
- Chrome 插件： XPath Helper
- Firefox 插件：Xpath Checker
# 选取节点
- nodename : 选取此节点的所有子节点
- ／：从根节点开始选取
- //：选取节点，不考虑位置
    - //bean:选取多个节点，-一般组成列表返回
- . : 选取当前节点
- .. : 选取当前节点的父节点
- @ ：选取属性
- xpath中查找一般按照路径的方式查找
    
    
# 谓语-Predicates
- /breakfast_menu/food[1]:选取breakfast_menu下面第一个food
- /breakfast_menu/food[last()]: 选取breakfast_menu下面最后一个food节点
- /breakfast_menu/food[last()-1]: 选取breakfast_menu倒数第二个节点
- //food[@name]: 选取带有name的food节点
- //food[@name='Beijing Waffles']: 选取name节点等于'Beijing..'的节点
