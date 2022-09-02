import jinja2
import argparse

parser = argparse.ArgumentParser('generate reset sql')
parser.add_argument('-d', '--delete', action='store_true', help='delete course row')
parser.add_argument('-o', '--out', help='output file')
parser.add_argument('course', help='name of course to delete')
args = parser.parse_args()

template = jinja2.Template(open('anubis-delete-class.sql.jinja2').read())

s = template.render(
    course=args.course,
    delete_course=args.delete,
)

print(s)

if args.out:
    with open(args.out, 'w') as f:
        f.write(s)
