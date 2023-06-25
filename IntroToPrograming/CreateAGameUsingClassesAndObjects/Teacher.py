class Teacher:
    def __init__(self, full_name: str, title: str, *args):
        self.full_name = full_name
        self.title = title
        self.name = self.title + " " + self.full_name.split(' ')[-1]
        self.skills = list(args)
        self.courses = list()

    def get_skills(self):
        return self.skills
        
    def add_course(self, course):
        self.courses.append(course)

    def _format_classes(self):
        if len(self.courses) > 1:
            return ', '.join(self.courses)
        elif len(self.courses) == 1:
            return self.courses[0]
        else:
            return "nothing"

    def __repr__(self):
        return "{}. They can teach {}".format(self.name, self._format_classes())
