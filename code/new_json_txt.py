import json

def cleaned_data_write(bad_data, infile, outfile):
    idx = 0
    bad_data_num = 0
    for line in open(infile):
        print(idx)
        idx += 1
        if not line.strip():
            continue
        line = line.strip()
        data = json.loads(line)
        if data['article_id'] in bad_data:
            bad_data_num += 1
            pass
        else:
            with open(outfile, 'a')as f:
                f.write(json.dumps(data, sort_keys=True))
                f.write('\n')
    return idx, bad_data_num

def read_bad_data(bad_data_path):
    bad_data = [line.strip() for line in open(bad_data_path, 'r')]
    return bad_data

def test_new_cleaned_data(bad_data, infile):
    idx = 0
    for line in open(infile):
        print(idx)
        idx += 1
        if not line.strip():
            continue
        line = line.strip()
        data = json.loads(line)
        if data['article_id'] in bad_data:
            print "failed!!!!!!!!!!!!!!!!!!!"
    return idx

arxiv_train_bdp = "D:\PythonCode\long-summarization-master\scripts_ljl\data_clear\\arxiv_train_bad_items.txt"
arxiv_train_inf = "D:\PythonCode\long-summarization-master\data\\arxiv-release\\arxiv-release\\train.txt"
arxiv_train_outf = "D:\PythonCode\long-summarization-master\data_cleaned\\arxiv_release\\arxiv_release\\train.txt"
all_data_num, bad_data_num = cleaned_data_write(read_bad_data(arxiv_train_bdp), arxiv_train_inf, arxiv_train_outf)
all_cleaned_data_num = test_new_cleaned_data(read_bad_data(arxiv_train_bdp), arxiv_train_outf)
print all_data_num, bad_data_num, all_cleaned_data_num
if all_data_num - bad_data_num == all_cleaned_data_num:
    print "yes"
else:
    print "NO"

arxiv_valid_bdp = "D:\PythonCode\long-summarization-master\scripts_ljl\data_clear\\arxiv_valid_bad_items.txt"
arxiv_valid_inf = "D:\PythonCode\long-summarization-master\data\\arxiv-release\\arxiv-release\\val.txt"
arxiv_valid_outf = "D:\PythonCode\long-summarization-master\data_cleaned\\arxiv_release\\arxiv_release\\val.txt"
all_data_num, bad_data_num = cleaned_data_write(read_bad_data(arxiv_valid_bdp), arxiv_valid_inf, arxiv_valid_outf)
all_cleaned_data_num = test_new_cleaned_data(read_bad_data(arxiv_valid_bdp), arxiv_valid_outf)
print all_data_num, bad_data_num, all_cleaned_data_num
if all_data_num - bad_data_num == all_cleaned_data_num:
    print "yes"
else:
    print "NO"

arxiv_test_bdp = "D:\PythonCode\long-summarization-master\scripts_ljl\data_clear\\arxiv_test_bad_items.txt"
arxiv_test_inf = "D:\PythonCode\long-summarization-master\data\\arxiv-release\\arxiv-release\\test.txt"
arxiv_test_outf = "D:\PythonCode\long-summarization-master\data_cleaned\\arxiv_release\\arxiv_release\\test.txt"
all_data_num, bad_data_num = cleaned_data_write(read_bad_data(arxiv_test_bdp), arxiv_test_inf, arxiv_test_outf)
all_cleaned_data_num = test_new_cleaned_data(read_bad_data(arxiv_test_bdp), arxiv_test_outf)
print all_data_num, bad_data_num, all_cleaned_data_num
if all_data_num - bad_data_num == all_cleaned_data_num:
    print "yes"
else:
    print "NO"

pubmed_train_bdp = "D:\PythonCode\long-summarization-master\scripts_ljl\data_clear\pubmed_train_bad_items.txt"
pubmed_train_inf = "D:\PythonCode\long-summarization-master\data\pubmed-release\pubmed-release\\train.txt"
pubmed_train_outf = "D:\PythonCode\long-summarization-master\data_cleaned\pubmed_release\pubmed_release\\train.txt"
all_data_num, bad_data_num = cleaned_data_write(read_bad_data(pubmed_train_bdp), pubmed_train_inf, pubmed_train_outf)
all_cleaned_data_num = test_new_cleaned_data(read_bad_data(pubmed_train_bdp), pubmed_train_outf)
print all_data_num, bad_data_num, all_cleaned_data_num
if all_data_num - bad_data_num == all_cleaned_data_num:
    print "yes"
else:
    print "NO"

pubmed_valid_bdp = "D:\PythonCode\long-summarization-master\scripts_ljl\data_clear\pubmed_valid_bad_items.txt"
pubmed_valid_inf = "D:\PythonCode\long-summarization-master\data\pubmed-release\pubmed-release\\val.txt"
pubmed_valid_outf = "D:\PythonCode\long-summarization-master\data_cleaned\pubmed_release\pubmed_release\\val.txt"
all_data_num, bad_data_num = cleaned_data_write(read_bad_data(pubmed_valid_bdp), pubmed_valid_inf, pubmed_valid_outf)
all_cleaned_data_num = test_new_cleaned_data(read_bad_data(pubmed_valid_bdp), pubmed_valid_outf)
print all_data_num, bad_data_num, all_cleaned_data_num
if all_data_num - bad_data_num == all_cleaned_data_num:
    print "yes"
else:
    print "NO"

pubmed_test_bdp = "D:\PythonCode\long-summarization-master\scripts_ljl\data_clear\pubmed_test_bad_items.txt"
pubmed_test_inf = "D:\PythonCode\long-summarization-master\data\pubmed-release\pubmed-release\\test.txt"
pubmed_test_outf = "D:\PythonCode\long-summarization-master\data_cleaned\pubmed_release\pubmed_release\\test.txt"
all_data_num, bad_data_num = cleaned_data_write(read_bad_data(pubmed_test_bdp), pubmed_test_inf, pubmed_test_outf)
all_cleaned_data_num = test_new_cleaned_data(read_bad_data(pubmed_test_bdp), pubmed_test_outf)
print all_data_num, bad_data_num, all_cleaned_data_num
if all_data_num - bad_data_num == all_cleaned_data_num:
    print "yes"
else:
    print "NO"
