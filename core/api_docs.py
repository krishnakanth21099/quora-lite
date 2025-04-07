from django.views.generic import TemplateView
import markdown
import os

class APIDocsView(TemplateView):
    template_name = 'core/api_docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        docs_path = os.path.join(os.path.dirname(__file__), 'templates', 'core', 'api_docs.md')
        
        with open(docs_path, 'r') as f:
            md_content = f.read()
            html_content = markdown.markdown(
                md_content,
                extensions=['fenced_code', 'tables', 'codehilite']
            )
            context['markdown_content'] = html_content
        
        return context
