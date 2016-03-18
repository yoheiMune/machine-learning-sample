# -*- coding: utf-8 -*-
# Word2Vec sample via Python.


# refs:
#   https://code.google.com/archive/p/word2vec/


# install.
"""
$ svn checkout http://word2vec.googlecode.com/svn/trunk/
$ cd trunk

$ make
gcc distance.c -o distance -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result
distance.c:18:10: fatal error: 'malloc.h' file not found
#include <malloc.h>
         ^
1 error generated.


$ grep "<malloc.h>" *.c
compute-accuracy.c:#include <malloc.h>
distance.c:#include <malloc.h>
word-analogy.c:#include <malloc.h>

$ sed -ie 's/#include <malloc.h>//g' *.m

$ make
いくつかワーニングがでるけど気にしない・・・



#  $ cp word2vec /usr/local/bin/

# お試し利用
$ curl http://mattmahoney.net/dc/text8.zip > text8.zip
$ unzip text8.zip
$ word2vec -train text8 -output vectors.bin -cbow 1 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -binary 1 -iter 15

$ ./distance vectors.bin
judo


# お試し2個目（やめた、750MBもあるし・・・）
$ curl http://www.statmt.org/wmt14/training-monolingual-news-crawl/news.2012.en.shuffled.gz > news.2012.en.shuffled.gz
$ gunzip news.2012.en.shuffled.gz


$ ./word-analogy vectors.bin

"""












































