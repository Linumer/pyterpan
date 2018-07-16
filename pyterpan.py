#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#import subprocess
import os
import pypandoc
import sys, getopt



### Path to the executable
##PANDOC_PATH = which('pandoc')

class Mdr(object):
    '''Mardown repertory'''

    def __init__(self, ipath):

        # initialise
        self._path = ipath

        # read structure
        index_file = os.path.join(ipath, 'index.md')
        print os.path.exists(index_file)

        list_files = []

        with open(index_file) as f:
            for line in f:
                #root, ext = os.path.splitext(line)
                #print root
                #print ext
                cfile = os.path.join(ipath, line)
                if os.path.exists(cfile):
                    list_files.append(cfile)

        self._files = list_files




def call_pypandoc(ifile, ofmt=None, ofile=None):
    '''create epub from other file using pandoc'''
    if ofmt is None:
        ofmt = 'html'
    output = pypandoc.convert_file(ifile, ofmt, outputfile=ofile)
    print ofile + ' is written.'

def create_mdr(ipath):
    '''create mdr object'''

    print os.path.isdir(ipath)

    my_mdr = Mdr(ipath)




def main(argv):
    inputfile = None
    outputfile = None
    outputformat = None
    mdrep = None
    try:
        opts, args = getopt.getopt(argv,"hi:o:t:m:",["ifile=","ofile=","ofmt=","mdr="])
    except getopt.GetoptError:
        print 'pyterpan.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'pyterpan.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-t", "--ofmt"):
            outputformat = arg
        elif opt in ("-m", "--mdr"):
            mdrep = arg
            #print 'mdr'
            #print mdrep
            #print inputfile
            #
            #sys.exit()

    if mdrep is not None:
        print mdrep

        create_mdr(mdrep)
    
    elif inputfile is not None and outputfile is not None:
        print 'Input file is "', inputfile
        print 'Output file is "', outputfile
        call_pypandoc(inputfile,outputformat,outputfile)

    
if __name__ == "__main__":
    main(sys.argv[1:])

