import weibopage

name = input("微博昵称:")
p = weibopage.WeiboPage(name)
p.getUserID()
if p.uid == '':
    p.uid = input("获取ID失败，手动输入数字ID：")
p.getUserRss()
p.downloads()