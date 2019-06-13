
import os
import re

def get_filenames():
    file_list = os.listdir('./mid_rus_conll')
    print(file_list)
    return file_list

def reading_getting():
    file_list = get_filenames()
    for file in file_list:
        to_open = 'mid_rus_conll/' + file
        with open(to_open, encoding='utf-8') as f:
            lines = f.readlines()


            for line in lines:
                r = re.search('^# newdoc id = (.*?)/(.*?)$', line)
                if r:
                    dir_name = r.group(1)
                    if not os.path.isdir(dir_name):
                        os.mkdir(dir_name)

                    part_of_path = r.group(2)
                    
                    l = re.search('(.*?)/(.*?)$', part_of_path)
                    if l:
                        dir_name2 = l.group(1)
                        path_for_dir2 = dir_name + '/' + dir_name2
                        if not os.path.isdir(path_for_dir2):
                            os.mkdir(path_for_dir2)
                        
                        new_file = './'+ dir_name + '/'+ l.group()
                        with open(new_file, "w", encoding="utf-8") as f:
                            f.write(line)
                    else:
                        new_file = './'+ dir_name + '/'+ r.group(2)
                        with open(new_file, "w", encoding="utf-8") as f:
                            f.write(line)
                        
                else:
                    with open(new_file, "a", encoding="utf-8") as f:
                        f.write(line)
                    
    return line

def main():
    line = reading_getting()
    
        

if __name__ == '__main__':
    main()


