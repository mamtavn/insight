import sys, os.path
import wc_utils

# Word Count, which takes in a text file or set of text files from a directory and outputs the number of occurrences for each word

if __name__=="__main__":
        progName = os.path.basename(sys.argv[0])
        if len(sys.argv) == 1:
                inputdirName = wc_utils.DEFAULT_INPUT_DIR
                outputdirName = wc_utils.DEFAULT_OUTPUT_DIR
        elif len(sys.argv) == 2:
                inputdirName = sys.argv[1]
                outputdirName = wc_utils.DEFAULT_OUTPUT_DIR
        elif len(sys.argv) == 3:
                inputdirName = sys.argv[1]
                outputdirName = sys.argv[2]
        else:
                print("Usage: " + progName + " [input directory] [output directory]")
                print("        if no input directory is specified")
                print("        the default directory will be", wc_utils.DEFAULT_INPUT_DIR)
                print("        if no output directory is specified")
                print("        the results are in the directory ", wc_utils.DEFAULT_OUTPUT_DIR)                
                print("        please add your files to be parsed in the " + wc_utils.DEFAULT_INPUT_DIR + " directory")
                sys.exit(-1)
                      
        if not os.path.isdir(inputdirName):
                print("Error: Cannot access the input directory ", inputdirName)
                sys.exit(-1)

        try:
                # create the out directory if it does not exist
                absdirName = os.path.abspath(outputdirName)
                if not (os.path.exists(absdirName)):
                        os.mkdir(absdirName)
                medianoutfile = absdirName + os.sep + wc_utils.DEFAULT_MEDIAN_FILE

                runningmedian = wc_utils.getRunningMedian(inputdirName)
                
                # overwrite the results file
                mf = open(medianoutfile, "w")
                for i in runningmedian:
                    mf.write("{:.1f}".format(i)+ "\n")

                mf.close()
                print("Running Median Count in - ", medianoutfile)                
        except:
                raise
