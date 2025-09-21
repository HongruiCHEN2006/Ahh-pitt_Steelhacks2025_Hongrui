from django.shortcuts import render
from PittAPI import news


# 主界面
def index(request):
    return render(request, 'index.html')


# 新闻页面
try:
    from PittAPI import news as pitt_news
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False

def news_view(request):
    if API_AVAILABLE:
        try:
            news_data = pitt_news.get_news()
        except Exception:
            news_data = []

        # 异常时
        if not news_data:
            news_data = [
                {"title": "PittAPI not working", "link": "#"},
                {"title": "I swore", "link": "#"}
            ]

    processed_news = []
    for item in news_data:
        processed_news.append({
            "title": item.get("title", "无标题"),
            "link": item.get("link", "#")
        })

    return render(request, 'news.html', {'news_list': processed_news})


def dining_view(request):
    # Ahh fake data. 
    dining_data = [
        {"name": "The Eatery", "status": "Open", "hours": "8:00 - 20:00"},
        {"name": "Nordy's Place", "status": "Closed", "hours": "11:00 - 15:00"},
        {"name": "Cafe 1811", "status": "Open", "hours": "7:30 - 19:00"},
    ]
    return render(request, 'dining.html', {"dining_list": dining_data})




def grad_requirements(request):
    requirements = {
        "Business School": {
            "Core Courses": ["BUS101", "BUS102", "BUS201"],
            "Social Science": ["ECON101", "PSYC101"],
        },
        "Engineering": {
            "Core Courses": ["ENGR101", "ENGR201"],
            "Math Requirements": ["MATH101", "MATH201"],
        },
        "Arts & Sciences": {
            "Humanities": ["HIST101", "PHIL101"],
            "Social Science": ["ECON101", "PSYC101"],  # 和商学院重合
        },
    }

    return render(request, "requirements.html", {"requirements": requirements})

def pitt_game(request):
    return render(request, 'pitt_game.html')







