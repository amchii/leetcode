import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

doc_pattern = re.compile(r'^"""(.*?)""".*', flags=re.DOTALL)


def main():
    for dirpath, dirnames, filenames, in os.walk(base_dir):
        for filename in filenames:
            if not filename.endswith(".py"):
                continue
            with open(os.path.join(dirpath, filename)) as fp:
                content = fp.read()
            m = doc_pattern.match(content)
            if not m:
                continue
            with open(os.path.join(dirpath, "description.txt"), 'w') as fp:
                fp.write(m.group(1).strip())


if __name__ == '__main__':
    main()
