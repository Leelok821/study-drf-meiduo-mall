


from celery_tasks.main import celery_app
from django.template import loader
import os
from django.conf import settings
from goods.utils import get_categories

@celery_app.task(name='generate_static_list_search_html')
def generate_static_list_search_html():
    """
    ⽣成静态的商品列表⻚和搜索结果⻚html⽂件
    """
    # 商品分类菜单
    categories = get_categories()
    # 渲染模板，⽣成静态html⽂件
    context = {
    'categories': categories,
    }
    template = loader.get_template('list.html')
    html_text = template.render(context)
    file_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, 'list.html')
    with open(file_path, 'w') as f:
        f.write(html_text)