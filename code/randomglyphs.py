glyphs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

students = {
    "David": [],
    "Nina": [],
    "Hugo": [],
    "Alexandre": [],
    "Slava": [],
    "MarkW": [],
    "James": [],
    "Josh": [],
    "MarkF": [],
    }

for i in range(4):
    for student, studentglyphs in students.iteritems():
        randomglyph = choice(glyphs)
        glyphs = glyphs.replace(randomglyph, "")
        studentglyphs.append(randomglyph)

for student, studentglyphs in students.iteritems():
    print student
    print studentglyphs
