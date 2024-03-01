# prompt_builder_app/template_processors/process.py

from prompt_builder_app.models import DataSet, Template

def process_template(template_id, data_set_id):
    template = Template.objects.get(id=template_id)
    data_set = DataSet.objects.get(id=data_set_id)
    
    processed_text = template.template_text
    for key, value in data_set.data.items():
        placeholder = f"<{key}>"
        processed_text = processed_text.replace(placeholder, value)

    return processed_text
