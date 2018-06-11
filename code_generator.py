import re

TemplateFile = 'CodeGenerator/leetcode_py.template'
TemplateTestFile = 'CodeGenerator/test_leetcode_py.template'


def main():
    config = {}
    with open('config.template', 'r', encoding='utf8') as f:
        config['Title'] = f.readline()
        config['TemplateCode'] = f.read()

    # method_name = re.match(r'.*def (\w*)\(.*', config['TemplateCode'], re.S).group(1)
    method_name = re.findall(r'def (\w*)\(', config['TemplateCode'], re.S)[-1]

    code = '{:0>3d}'.format(int(re.match(r'(\d*)\..*', config['Title']).group(1)))
    title = re.match(r'.*\.\s*(.*)', config['Title']).group(1)
    title_name = title.lower().replace(' ', '_')

    file_name = 'q{}_{}'.format(code, title_name)
    hump_name = title.title().replace(' ', '')

    with open(TemplateFile, encoding='utf8') as tp_file:
        with open('{}.py'.format(file_name), 'x', encoding='utf8') as g_file:
            file_lines = tp_file.readlines()

            for file_line in file_lines:
                line = file_line.replace('${TEMPLATE_CODE}', config['TemplateCode'])
                g_file.writelines(line)

    with open(TemplateTestFile, encoding='utf8') as tp_test_file:
        with open('test_{}.py'.format(file_name), 'x', encoding='utf8') as g_test_file:
            file_lines = tp_test_file.readlines()

            for file_line in file_lines:
                line = file_line.replace('${FILE_NAME}', file_name).replace('${METHOD_NAME}', method_name) \
                    .replace('${TITLE_NAME}', title_name).replace('${HUMP_NAME}', hump_name)
                g_test_file.writelines(line)


if __name__ == '__main__':
    main()
