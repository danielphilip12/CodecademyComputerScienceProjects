class Teacher:
    def __init__(self, full_name, title, *args):
        self.full_name = full_name
        self.title = title
        self.name = self.title + " " + self.full_name.split(' ')[-1]
        self.classes = list(args)

    def _format_classes(self):
        if len(self.classes) > 1:
            return ', '.join(self.classes)
        elif len(self.classes) == 1:
            return self.classes[0]
        else:
            return "nothing"

    def __repr__(self):
        return "{}. They teach {}".format(self.name, self._format_classes())
