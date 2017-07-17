import os

output_path = './output/'
input_path = './input/'
replace_to = 'stroke="#2F80ED"'

def replaceFileString( your_file, str_to_find ):
    data = your_file.readlines()
    new_data = ''
    for i in range(0, len(data)):
        line = data[i]
        stroke_index_start = line.find(str_to_find, 0, len(line))
        if(stroke_index_start != -1):
            stroke_index_end = stroke_index_start + len(str_to_find)
            data[i] = line[0: stroke_index_start] + replace_to + line[stroke_index_end: len(line)]
        new_data += data[i]
    return new_data;

def createNewFile( output_file_name, output_file_string):
    f = open(output_path + output_file_name, 'w+')
    f.write(output_file_string)
    f.close()

def createNewFileName(orginal_file_name, name_modifier):
    ex_index = orginal_file_name.find('.', 0, len(orginal_file_name))
    file_name = orginal_file_name[0:ex_index] + name_modifier + orginal_file_name[ex_index:len(orginal_file_name)]
    return file_name

fileName_list = list = os.listdir(input_path)
for i in range(0, len(fileName_list)):
    file = open(input_path + fileName_list[i], 'r')
    new_file_string = replaceFileString(file, 'stroke="#000"')
    new_file_name = createNewFileName(fileName_list[i], '-selected')
    createNewFile(new_file_name, new_file_string)
