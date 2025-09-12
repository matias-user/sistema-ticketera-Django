class BootstraClassespMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            old_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{old_classes} form-control".strip