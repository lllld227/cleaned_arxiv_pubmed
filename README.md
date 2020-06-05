# cleaned-data-for-arXiv-PubMed
clean up the dataset arXiv/PubMed on five sides
# bad data include 5 aspects:
# 1> too short summary:sentences num <= 1;
# 2> too long summary: sentences num > 20;some data items
# have a long summary which is not the truth,it always
# transfer other section content to summary
# 3> only one section: data item only have one section
# which is inconsistent with the fact
# 4> one of the sections' content is none,
# 5> section num less than 4 and tokens num less than 2000;

train -*- val -*- test

arXiv(all/clean/left)	203037/25070/171967	  -*-	6436/449/5987	-*- 	6440/455/5985

PubMed(all/clean/left)	119924/46649/73275	 -*-  	6633/2532/4101	-*- 	6658/2472/4186

"all" represents the total num of data of this work: https://github.com/armancohan/long-summarization
"clean" represents the total num of data being cleaned
"left" represents the total num of data after cleaning
the dataset cleaned up can't be uploaded to github because of the size. I share it through baidunetdisk:
链接：https://pan.baidu.com/s/1tlrkIVZ__Q6GExHq35E9wA 
提取码：rmr9 
复制这段内容后打开百度网盘手机App，操作更方便哦