# sphere to wav
Batch convert sphere format files in a directory to wav files.
Note that the files will be overwritten.


## 0. Preparation

You can download sph2pipe software [here](http://www.openslr.org/3/)
But, Already installed in repository root

```
cd <REPOSITORY_ROOT>/sph2pipe_v2.5/
gcc -o sph2pipe sph2pipe.c shorten_x.c file_headers.c -lm
```

## 1. Implementation
Note that the files will be overwritten.
```
cd <REPOSITORY_ROOT>
python sphere2wav.py -i <PATH_TO_csr_1folder>
```
