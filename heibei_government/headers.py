# for i in range(1,691):
#     common_param.update({"__CALLBACKPARAM":f"Load|*|{i}",
#                          "__CALLBACKID": "__Page",
#                          "__EVENTTARGET":"",
#                          "__EVENTARGUMENT":""})
#
#
#     response = requests.post("http://yglz.tousu.hebnews.cn/l-1001-5-",data=common_param,headers=headers)
#     html = response.content.decode("utf-8")
#     print("*"*200)
#
#     tree = etree.HTML(html)  # 解析html
#     divs = tree.xpath('//div[@class="listcon"]')  # 解析列表区域div
#     for div in divs:  # 循环这个区域
#         try:
#             # 注意下面是通过div去进行的xpath查找，同时加上try方式报错
#             shouli = div.xpath('span[1]/p/a/text()')[0]  # 受理单位
#             type = div.xpath('span[2]/p/text()')[0].replace("\n","")  # 投诉类型
#             content = div.xpath('span[3]/p/a/text()')[0]  # 投诉内容
#             datetime = div.xpath('span[4]/p/text()')[0].replace("\n","")  # 时间
#             status = div.xpath('span[6]/p/text()')[0].replace("\n","")  # 时间
#             one_data = {"shouli":shouli,
#                         "type":type,
#                         "content":content,
#                         "datetime":datetime,
#                         "status":status,
#                         }
#             print(one_data)  # 打印数据，方便存储到mongodb里面
#
#         except Exception as e:
#             print("内部数据报错")
#             print(div)
#             continue
#
