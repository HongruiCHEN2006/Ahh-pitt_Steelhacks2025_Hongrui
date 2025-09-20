from django.shortcuts import render

# ----------------------------
# 主界面
# ----------------------------
def index(request):
    return render(request, 'index.html')


# ----------------------------
# 新闻页面
# ----------------------------
def news_view(request):
    # 模拟新闻数据
    news_data = [
        {"title": "新闻1：校园活动更新", "link": "#"},
        {"title": "新闻2：餐厅新菜单上线", "link": "#"},
        {"title": "新闻3：Hackathon 报名截止提醒", "link": "#"},
    ]
    return render(request, 'news.html', {"news_list": news_data})


# ----------------------------
# 餐厅页面
# ----------------------------
def dining_view(request):
    # 模拟餐厅数据
    dining_data = [
        {"name": "The Eatery", "status": "Open", "hours": "8:00 - 20:00"},
        {"name": "Nordy's Place", "status": "Closed", "hours": "11:00 - 15:00"},
        {"name": "Cafe 1811", "status": "Open", "hours": "7:30 - 19:00"},
    ]
    return render(request, 'dining.html', {"dining_list": dining_data})
