import os
import json

# bad data include 5 aspects:
# 1> too short summary:sentences num <= 1;
# 2> too long summary: sentences num > 20;some data items
# have a long summary which is not the truth,it always
# transfer other section content to summary
# 3> only one section: data item only have one section
# which is inconsistent with the fact
# 4> one of the sections' content is none,
# 5> section num less than 4 and tokens num less than 2000;


def read_resource_and_judge(infile):
    bad_data_IDs = []
    idx = 0
    for line in open(infile):
        print(idx)
        idx += 1
        if not line.strip():
            continue
        line = line.strip()
        data = json.loads(line)
        # too short summary
        if len(data['abstract_text']) <= 1:
            bad_data_IDs.append(data['article_id'])

        # too long summary
        elif len(data['abstract_text']) > 20:
            bad_data_IDs.append(data['article_id'])

        # paper conclude only one section
        elif len(data['sections']) <= 1:
            bad_data_IDs.append(data['article_id'])

        # section num less than 4 and tokens num less than 2000;
        elif len(data['sections']) <= 4:
            length = [count_words_of_str(item) for item in data['sections']]
            if sum(length) < 2000:
                bad_data_IDs.append(data['article_id'])
            else:
                pass
        # one of the sections' content is none
        for item in data['sections']:
            if len(item[0]) == 0:
                bad_data_IDs.append(data['article_id'])
            else:
                pass
    return bad_data_IDs

def write_bad_data(bad_data, file):
    with open(file, 'w')as a:
        for i in bad_data:
            a.write(i + '\n')

def count_words_of_str(sss):
    s = (''.join(sss)).replace('<S>', '').replace('</S>', '').replace('_', '')
    return len([i for i in s.split(' ') if i])

arxiv_infile_train = "D:\PythonCode\long-summarization-master\data\\arxiv-release\\arxiv-release\\train.txt"
pubmed_infile_train = "D:\PythonCode\long-summarization-master\data\pubmed-release\pubmed-release\\train.txt"
arxiv_infile_val = "D:\PythonCode\long-summarization-master\data\\arxiv-release\\arxiv-release\\val.txt"
pubmed_infile_val = "D:\PythonCode\long-summarization-master\data\pubmed-release\pubmed-release\\val.txt"
arxiv_infile_test = "D:\PythonCode\long-summarization-master\data\\arxiv-release\\arxiv-release\\all_test.txt"
pubmed_infile_test = "D:\PythonCode\long-summarization-master\data\pubmed-release\pubmed-release\\all_test.txt"

arxiv_train_bad_items = read_resource_and_judge(arxiv_infile_train)
write_bad_data(arxiv_train_bad_items, "arxiv_train_bad_items.txt")
pubmed_train_bad_items = read_resource_and_judge(pubmed_infile_train)
write_bad_data(pubmed_train_bad_items, "pubmed_train_bad_items.txt")

arxiv_valid_bad_items = read_resource_and_judge(arxiv_infile_val)
write_bad_data(arxiv_valid_bad_items, "arxiv_valid_bad_items.txt")
pubmed_valid_bad_items = read_resource_and_judge(pubmed_infile_val)
write_bad_data(pubmed_valid_bad_items, "pubmed_valid_bad_items.txt")

arxiv_test_bad_items = read_resource_and_judge(arxiv_infile_test)
write_bad_data(arxiv_test_bad_items, "arxiv_test_bad_items.txt")
pubmed_test_bad_items = read_resource_and_judge(pubmed_infile_test)
write_bad_data(pubmed_test_bad_items, "pubmed_test_bad_items.txt")


print len(arxiv_train_bad_items),len(arxiv_valid_bad_items),len(arxiv_test_bad_items)
print len(pubmed_train_bad_items),len(pubmed_valid_bad_items),len(pubmed_test_bad_items)
