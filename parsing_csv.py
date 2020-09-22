import csv
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
work_dir = os.path.join(base_dir, 'cmdb_consolidation')
cmdb_chef_file = os.path.join(work_dir, 'mercado.txt')
cmdb_now_file = os.path.join(work_dir, 'quitanda.txt')


chefdb = []
nowdb = []

with open(cmdb_chef_file, 'r') as cmdb_chef:
    cmdb_chef_reader = csv.reader(cmdb_chef, delimiter=',')
    for chef_line in cmdb_chef_reader:
        chefdb.append(chef_line)


with open(cmdb_now_file, 'r') as cmdb_now:
    cmdb_now_reader = csv.reader(cmdb_now, delimiter=',')
    for now_line in cmdb_now_reader:
        nowdb.append(now_line)

print(chefdb)
print(nowdb)
print([ double_checked for double_checked in chefdb[1] if double_checked in nowdb[0] ])
