import subprocess

def run_check(column_number, files,path='/tmp/'):
    col_name = f'-f{column_number}'
    results = []
    for file in files:
        command = f" cut -d',' {col_name} {path}{file} | sort | md5 "
        print(command)
        output = subprocess.check_output(command,shell = True)
        results.append(output)
    return results


if __name__ == '__main__':
    md5_val_dic = {}

    files_names = ['itemMasterPart1_20201125.csv000','itemMasterPart1_v2_20201125.csv000']
    for i in range(1,48+1):
        print(i)
        md5_val_dic[i]  = run_check(i,files_names)
    #print(md5_val_dic)
    for key in md5_val_dic.keys():
        if md5_val_dic[key][0] != md5_val_dic[key][1]:
            print(f"Column {key} differ! ")